# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render, redirect

from django.http import HttpResponse
from django.template import loader

from django.db.models import Q, Max, Min, Avg

from django.forms import ModelForm

from .models import MaxExtent
from .forms import NameForm, AggSearchForm
from .functions import chart_object_areas

# get lakes will include the search form AND the output of that search
def getLakes(request):
    context = {}
    if request.method == 'POST':

        print request.POST
        # populate results into context to be rendered in the template (like with viewer)
        
        # same pattern as below
        # template
        form = AggSearchForm(request.POST)
#        print '1'
#        print form
#        print '2'
#        print dir(form)

        if form.is_valid():
            # get objects from form
            search_country = form.cleaned_data['country_name']
            search_region = form.cleaned_data['region_name']
            search_subregion = form.cleaned_data['subregion_name']
            search_continent = form.cleaned_data['continent_name']
            search_sizeRange = form.cleaned_data['size_class'] # this wil; eventually be a range of values OR a drop-down of size classes (ranges). not sure how this will be affected
            search_waterType = form.cleaned_data['water_type'] # will be drop down of 3 options (river, lake, resevoir)

            # deal with location-based fields - use icontains to allow lower case entry (may not matter if/when we format fields as drop down/etc- still will need it for country)
            if search_country:             
                objects = MaxExtent.objects.filter(Q(geoName__icontains = search_country) | Q(sovereignty__icontains = search_country) | Q(glwdCountry__icontains = search_country) | Q(glwdCountry2__icontains = search_country))
            elif search_region:
                objects = MaxExtent.objects.filter(unRegion__icontains = search_region)
            elif search_subregion:
                objects = MaxExtent.objects.filter(subregion__icontains = search_subregion)
            elif search_continent:
                objects = MaxExtent.objects.filter(continent__icontains = search_continent)
            else: # none of the location-based options were selected
                objects = MaxExtent.objects.all() # get all objects (and filter further below)

            # add other filters #* fix these:
            #if search_sizeRange:
                #objects = objects.filter( # areaMax < range and areaMax > range          
            if search_waterType: # NOTE (add note to form html? how?): This filter will only return objects that are in the GLWD
                objects = objects.filter(typeGlwd__icontains = search_waterType)            
            
            # 2. Now that we have objects, build results for context
            if objects:
                results = [] # list of lists [attribute, result]
                
                count = len(objects) # since objects is already in memory, len() is faster than .count() according to django docs
                min = objects.aggregate(val=Min('areaMax'))['val']
                max = objects.aggregate(val=Max('areaMax'))['val']
                significantObjs = objects.filter(pValue__lt = 0.05)
                nSignificant = '{} ({}%)'.format(len(significantObjs), (len(significantObjs)/count)*100 )
                aveSlope = significantObjs.aggregate(val=Avg('slope'))['val']
                
                results.extend([['Number of water bodies', count], ['Minimum area (all years)', min], \
                 ['Maximum area (all years)', max], ['Number of water bodies with a statistically significant linear trend (p-value < 0.05)', nSignificant],\
                 ['Average rate of change among statistically significant objects', aveSlope]])
                #print results
                context['results'] = results               

            else: # if for example country is provided but there are no objects for it
                error_message = 'No objects exist for these filters'
                context['error_message'] = error_message                 
    else:
        form = AggSearchForm() # blank form
 
    context['form'] = form
    return render(request, 'waterExplorer/searchAggregate.html', context)


# lake name uses the search by name form and redirects to (object) viewer
def getLakeName(request):

    context = {}
    if request.method == 'POST':
#        print request.POST
        
        form = NameForm(request.POST) # make form out of current post data                    
        if form.is_valid():
            search_term = form.cleaned_data['lake_name']

            # do the searching of db based on term to get ID we want
            best_match = MaxExtent.objects.filter(lakeName__icontains=search_term).order_by('-areaMax').first()
 
            # send values to functions.chart_object_area 

            if best_match:
                return redirect('viewer', req_id=best_match.pk)
            else:
                error_message = 'Object with name {} does not exist'.format(search_term)
                context['error_message'] = error_message #* NEED to add this to template if theres error
            
    else:
        form = nameForm() # unbound empty form

#    message = '{}'.format(request.GET['q'])
    context['form'] = form
    return render(request, 'waterExplorer/searchByName.html', context) # handles multiple cases    
#    return HttpResponse(message)


# Home page
# waterExplorer/
def index(request):
    #* need to do view? and template for Home page
    return HttpResponse("Hello, world. Welcome to the Global Water Explorer.")
    
# Object viewer
def viewer(request, req_id):
    waterBody = get_object_or_404(MaxExtent, pk = req_id)

    # Get list of fields for display
    displayFields = [str(f.name) for f in MaxExtent._meta.get_fields()]
    class MaxExtentForm(ModelForm):
        class Meta:
            model = MaxExtent
            fields = displayFields
    fields = MaxExtentForm(instance=waterBody)

    # Send area values and slope to chart function
    #functions.chart_object_area(
    """ this did not work. object doesnt have values_list()
    print waterBody.values_list('area2000', 'area2001', 'area2002', 'area2003', 'area2004', 'area2005',\
          'area2006', 'area2007', 'area2008', 'area2009', 'area2010', 'area2011', 'area2012',\
           'area2013', 'area2014', 'area2015', 'slope')
    """
 
    #* better way to do this?
    areas = [waterBody.area2000, waterBody.area2001, waterBody.area2002, waterBody.area2003, \
             waterBody.area2004, waterBody.area2005, waterBody.area2006, waterBody.area2007, \
             waterBody.area2008, waterBody.area2009, waterBody.area2010, waterBody.area2011, \
             waterBody.area2012, waterBody.area2013, waterBody.area2014, waterBody.area2015]

#    print len(areas)
    years = [y for y in range(2000,2016)]
 #   print len(years)

    # return plot object that can be passed to template
    charted = chart_object_areas([x for x in range(2000,2016)], areas, waterBody.slope, waterBody.intercept)

    context = {'waterBody': waterBody, 'displayFields': fields, 'chart': charted}

    

    return render(request, 'waterExplorer/viewer.html', context)





# Filter views:
# By name --> viewer/id
# By Size --> aggViewer
# By location --> aggViewer

# Query by country
# water/explorer/countryQuery/<CountryName>
def query_by_country(request, country_name):
    from itertools import chain
#    querySet = MaxExtent.objects.filter(geoName = country_name)
    # ** THIS WAY IS NOT THE BEST. Use Q() instead. this way will return duplicates
    qs1 = MaxExtent.objects.filter(geoName__contains = country_name)
    qs2 = MaxExtent.objects.filter(sovereignty__contains = country_name)
    querySet = list(chain(qs1, qs2)) # combine filters with or
    #out = '\n'.join([q.areaMax for q in querySet])
    #return HttpResponse(out)
    #template = loader.get_template('waterExplorer/query_by_country.html')
    context = {'querySet': querySet}
    return render(request, 'waterExplorer/query_by_country.html', context)
     
