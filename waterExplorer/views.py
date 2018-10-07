# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import get_object_or_404, render

from django.http import HttpResponse
from django.template import loader

from django.forms import ModelForm

from .models import MaxExtent


# Create your views here.

# Home page
# waterExplorer/
def index(request):
    return HttpResponse("Hello, world. Welcome to the Global Water Explorer.")

# Object viewer
def viewer(request, req_id):
    waterBody = get_object_or_404(MaxExtent, pk = req_id)

    displayFields = [str(f.name) for f in MaxExtent._meta.get_fields()]
    class MaxExtentForm(ModelForm):
        class Meta:
            model = MaxExtent
            fields = displayFields
    form = MaxExtentForm(instance=waterBody)

    context = {'waterBody': waterBody, 'displayFields': form}

    

    return render(request, 'waterExplorer/viewer.html', context)

# Query by country
# water/explorer/countryQuery/<CountryName>
def query_by_country(request, country_name):
    from itertools import chain
#    querySet = MaxExtent.objects.filter(geoName = country_name)
    qs1 = MaxExtent.objects.filter(geoName__contains = country_name)
    qs2 = MaxExtent.objects.filter(sovereignty__contains = country_name)
    querySet = list(chain(qs1, qs2))
    #out = '\n'.join([q.areaMax for q in querySet])
    #return HttpResponse(out)
    #template = loader.get_template('waterExplorer/query_by_country.html')
    context = {'querySet': querySet}
    return render(request, 'waterExplorer/query_by_country.html', context)
     
