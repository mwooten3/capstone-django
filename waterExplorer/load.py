import os
from django.contrib.gis.utils import LayerMapping
from .models import MaxExtent

waterExplorer_mapping = {

    # model field (key): shp field (value)
    'id': 'gridcode',
    'geoName': 'GEOUNIT',
    'sovereignty': 'SOVEREIGNT',
    'abbrName': 'SU_A3',
    'population': 'POP_EST',
    'medianGdp': 'GDP_MD_EST',
    'continent': 'CONTINENT',
    'unRegion': 'REGION_UN',
    'subregion': 'SUBREGION',
    'lakeName': 'LAKE_NAME',
    'glwdCountry': 'COUNTRY',
    'glwdCountry2': 'SEC_CNTRY',
    'areaMax': 'area_max',
    'area2000': 'area_2000',
    'area2001': 'area_2001',
    'area2002': 'area_2002',
    'area2003': 'area_2003',
    'area2004': 'area_2004',
    'area2005': 'area_2005',
    'area2006': 'area_2006',
    'area2007': 'area_2007',
    'area2008': 'area_2008', 
    'area2009': 'area_2009',
    'area2010': 'area_2010',
    'area2011': 'area_2011',
    'area2012': 'area_2012',
    'area2013': 'area_2013',
    'area2014': 'area_2014',
    'area2015': 'area_2015',
    'slope': 'slope',
    'intercept': 'intercept',
    'rSquared': 'r_squared',
    'pValue': 'p_value',
    'stdErr': 'std_err',
    'nYears': 'n_years',
    'centerLat': 'centr_lat',
    'centerLon': 'centr_lon',
    'nCountry': 'n_country',
    'nGlwd': 'n_glwd',
    'typeGlwd': 'glwd_type',

    'poly': 'MULTIPOLYGON',
}


maxExtent_shp = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'MaxExtent_2000to2015.shp'),
)
 
#= '/att/gpfsfs/briskfs01/ppl/mwooten3/capstone/capstone-django/waterExplorer/data/MaxExtent_2000to2015.shp'

def run(verbose=True):
    lm = LayerMapping(MaxExtent, maxExtent_shp, waterExplorer_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
