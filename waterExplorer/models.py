# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from django.db import models
from django.contrib.gis.db import models

# Create your models here.
class testgeo(models.Model):
    gridcode = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    poly = models.MultiPolygonField()


    def __str__(self): # string representation of the model will be it's name
        return self.name

class MaxExtentPlot(models.Model):
    maxExtent = models.ForeignKey("MaxExtent", on_delete=models.CASCADE)
    plot = models.ImageField(upload_to="plots")
    



class MaxExtent(models.Model):
    
    """Need to define choices for: Continent, Region, subregion, maybe typeGLWD and others
    i.e. like so:
    CONTINENT_CHOICES = (
        ('Europe', 'Europe'), # i think??? not positive
        ('Seven Seas (open ocean)', 'Open Ocean'),
        ('North America', 'North Anerica'), ...
        ... etc.
    )
    # and then below in field:
    continent = models.CharField(
        max_length = 10,
        choices=CONTINENT_CHOICES,
        ...and others
    """
    
    # Model fields correspond to subset of fields in MaxExtent_2000to2015.shp: 
    id = models.IntegerField(primary_key=True) # gridcode
    geoName = models.CharField('Geounit name (territories are unique geounits)', max_length=40, null=True, blank=True) # GEOUNIT
    sovereignty = models.CharField('Sovereign country name', max_length=32, null=True, blank=True) # SOVEREIGNT
    abbrName = models.CharField('3-character country abbreviation', max_length=3, null=True, blank=True) # SU_A3
    population = models.IntegerField('Country population', null=True)
    medianGdp = models.IntegerField("Country median GDP", null=True)
    continent = models.CharField('Continent name', max_length=23)
    unRegion = models.CharField('UN region name', max_length=23, blank=True)
    subregion = models.CharField('UN subregion', max_length=25, blank=True)
    lakeName = models.CharField('GLWD Lake name', max_length=50)
    glwdCountry = models.CharField('Country name according to GLWD', max_length = 30, blank=True)
    glwdCountry2 = models.CharField('Other intersecting country names, per GLWD', max_length=50, blank=True)
    areaMax = models.FloatField('Max Extent area (km<sup>2</sup>)')
    area2000 = models.FloatField('2000 area (km<sup>2</sup>)')
    area2001 = models.FloatField('2001 area (km<sup>2</sup>)')
    area2002 = models.FloatField('2002 area (km<sup>2</sup>)')
    area2003 = models.FloatField('2003 area (km<sup>2</sup>)')
    area2004 = models.FloatField('2004 area (km<sup>2</sup>)')
    area2005 = models.FloatField('2005 area (km<sup>2</sup>)')
    area2006 = models.FloatField('2006 area (km<sup>2</sup>)')
    area2007 = models.FloatField('2007 area (km<sup>2</sup>)')
    area2008 = models.FloatField('2008 area (km<sup>2</sup>)')
    area2009 = models.FloatField('2009 area (km<sup>2</sup>)')
    area2010 = models.FloatField('2010 area (km<sup>2</sup>)')
    area2011 = models.FloatField('2011 area (km<sup>2</sup>)')
    area2012 = models.FloatField('2012 area (km<sup>2</sup>)')
    area2013 = models.FloatField('2013 area (km<sup>2</sup>)')
    area2014 = models.FloatField('2014 area (km<sup>2</sup>)')
    area2015 = models.FloatField('2015 area (km<sup>2</sup>)')
    slope = models.FloatField('Rate of change (2000 to 2015; km<sup>2</sup>/year)')
    intercept = models.FloatField()
    rSquared = models.FloatField('R<sup>2</sup> of linear trend')
    pValue = models.FloatField('P-value of linear trend')
    stdErr = models.FloatField('Standard error of linear trend')
    nYears = models.IntegerField('Number of years where water body is identified')
    centerLat = models.FloatField('Latitude of centroid')
    centerLon = models.FloatField('Longitude of centroid')
    nCountry = models.IntegerField('Number of countries intersecting lake')
    nGlwd = models.IntegerField('Number of GLWD bodies intersecting lake')
    typeGlwd = models.CharField('GLWD type', max_length=25)

    poly = models.MultiPolygonField()

    def __str__(self): # default field for string representation
        
        if self.lakeName: 
            return "ID {}: {} ({}, {})".format(self.id, self.lakeName, self.centerLon, self.centerLat)
        else:
            return "ID {}: Not named ({}, {})".format(self.id, self.centerLon, self.centerLat)


#    def get_fields(self):
#        return [(field.name, field.value_to_string(self)) for field in MaxExtent.__meta.fields]
