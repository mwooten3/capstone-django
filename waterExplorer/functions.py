# helper functions for capstone-django

import sys
from django.http import HttpResponse
import matplotlib as mpl
mpl.use('Agg') # Required to redirect locally
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import rand

import cStringIO
import io
from django.contrib.staticfiles.templatetags.staticfiles import static


def chart_object_areas(X, Y, slope, intercept, objId):
#    print X # years
#    print Y # areas
#    print slope

    plt.ylim(0.0, np.max(Y)+(np.mean(Y)/3))
    plt.xlim(np.min(X)-1, np.max(X)+1)
    plt.ylabel('Area ($km^2$)')
    plt.xlabel('Year')
    plt.title('Area over time and best fit line, ID {}'.format(objId))
    plt.scatter(X, Y)

    # plot the best fit line too
    fitY = [(slope*x + intercept) for x,d in enumerate(X)]
#    print fitY
    plt.plot(X, fitY, color='black')


    #plt.show()
#    figPath = static('area_plot_new.png')#.format(objId))
    figPath = '/att/gpfsfs/briskfs01/ppl/mwooten3/capstone/capstone-django/static/plot_new.png'
#    print 'figPath:'
#    print figPath
    plt.savefig(figPath)
#    f = cStringIO.StringIO() # redirect
#    plt.savefig(f, format="png", facecolor=(0.95,0.95,0.95))
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    plt.clf()    
    return buf       
    



#    return f#.getvalue() 
#    return figPath

#def chart_sizes_histogram(): 

# list of size classes for drop down choices
def size_class_tuples():
    # display, value
    return [('', '-------'),
     ('0-62.5', '0 - 62.5'),
     ('62.5-100', '62.5 - 100'),
     ('100-1000', '100 - 1,000'),
     ('1000-10000', '1,000 - 10,000'),
     ('10000-100000', '10,000-100,000')]     
