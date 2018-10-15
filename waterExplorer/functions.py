# helper functions for capstone-django

import sys
from django.http import HttpResponse
import matplotlib as mpl
mpl.use('Agg') # Required to redirect locally
import matplotlib.pyplot as plt
import numpy as np
from numpy.random import rand

import cStringIO



def chart_object_areas(X, Y, slope, intercept):
    print X # years
    print Y # areas
    print slope

    plt.ylim(0.0, np.max(Y)+(np.mean(Y)/3))
    plt.xlim(np.min(X)-1, np.max(X)+1)
    plt.ylabel('Area ($km^2$)')
    plt.xlabel('Year')
    plt.bar(X, Y)

    # plot the best fit line too
    fitY = [(slope*x + intercept) for x,d in enumerate(X)]
    print fitY
    plt.plot(X, fitY, color='black')


    #plt.show()
    plt.savefig('/att/gpfsfs/briskfs01/ppl/mwooten3/capstone/capstone-django/waterExplorer/static/plot.png')
    f = cStringIO.StringIO() # redirect
    plt.savefig(f, format="png", facecolor=(0.95,0.95,0.95))
    plt.clf()        
    



    return f.getvalue() 
