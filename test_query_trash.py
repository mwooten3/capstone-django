#import sys
#print sys.path

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'capstone.settings')
import django
django.setup()

#print sys.path # to test before and after env setup

from waterExplorer.models import MaxExtent

pnt_wkt = 'POINT(-67.8608 -55.8619)'

# 1. get all objects
#print MaxExtent.objects.all()
##prints query set of all objects
#print len(MaxExtent.objects.all())
## 1977678

# 2. filter objects in db (recieve list)

# print objects that contain pnt_wkt (1)
print MaxExtent.objects.filter(poly__contains=pnt_wkt)
##<QuerySet [<MaxExtent: ID 1977678: Not named (-67.8608, -55.8619)>]>

# options that can be used on query set
print dir(MaxExtent.objects.filter(poly__contains=pnt_wkt))
## ['__and__', '__bool__', '__class__', '__deepcopy__', '__delattr__', '__dict__', 
##'__doc__', '__format__', '__getattribute__', '__getitem__', '__getstate__', '__hash__',
##'__init__', '__iter__', '__len__', '__module__', '__new__', '__nonzero__', '__or__', 
##'__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__',
##'__str__', '__subclasshook__', '__weakref__', '_add_hints', '_batched_insert', '_clone', 
##'_combinator_query', '_create_object_from_params', '_db', '_earliest_or_latest', 
##'_extract_model_params', '_fetch_all', '_fields', '_filter_or_exclude', '_for_write',
##'_has_filters', '_hints', '_insert', '_iterable_class', '_known_related_objects', 
##'_merge_known_related_objects', '_merge_sanity_check', '_next_is_sticky', '_populate_pk_values',
##'_prefetch_done', '_prefetch_related_lookups', '_prefetch_related_objects', '_prepare_as_filter_value', 
##'_raw_delete', '_result_cache', '_sticky_filter', '_update', '_values', 'aggregate', 'all', 'annotate',
##'as_manager', 'bulk_create', 'complex_filter', 'count', 'create', 'dates', 'datetimes', 'db', 'defer', 
##'delete', 'difference', 'distinct', 'earliest', 'exclude', 'exists', 'extra', 'filter', 'first', 'get',\
##'get_or_create', 'in_bulk', 'intersection', 'iterator', 'last', 'latest', 'model', 'none', 'only', 
##'order_by', 'ordered', 'prefetch_related', 'query', 'raw', 'reverse', 'select_for_update', 
##'select_related', 'union', 'update', 'update_or_create', 'using', 'values', 'values_list']

# print first object that contains pnt_wkt
print MaxExtent.objects.filter(poly__contains=pnt_wkt)[0]
##ID 1977678: Not named (-67.8608, -55.8619)

# print options that can be done on first object in query set
print dir(MaxExtent.objects.filter(poly__contains=pnt_wkt)[0])
##['DoesNotExist', 'MultipleObjectsReturned', '__class__', '__delattr__', '__dict__', '__doc__', 
##'__eq__', '__format__', '__getattribute__', '__hash__', '__init__', u'__module__', '__ne__', 
##'__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__setstate__', '__sizeof__', 
##'__str__', '__subclasshook__', '__weakref__', '_check_column_name_clashes', '_check_field_name_clashes', 
##'_check_fields', '_check_id_field', '_check_index_together', '_check_local_fields',
##'_check_long_column_names', '_check_m2m_through_same_relationship', '_check_managers', '_check_model',
##'_check_model_name_db_lookup_clashes', '_check_ordering', '_check_swappable', '_check_unique_together',
##'_do_insert', '_do_update', '_get_FIELD_display', '_get_next_or_previous_by_FIELD', 
##'_get_next_or_previous_in_order', '_get_pk_val', '_get_unique_checks', '_meta', '_perform_date_checks', 
##'_perform_unique_checks', '_save_parents', '_save_table', '_set_pk_val', '_state', 'abbrName', 'area2000', 
##'area2001', 'area2002', 'area2003', 'area2004', 'area2005', 'area2006', 'area2007', 'area2008', 'area2009', 
##'area2010', 'area2011', 'area2012', 'area2013', 'area2014', 'area2015', 'areaMax', 'centerLat', 'centerLon',
##'check', 'clean', 'clean_fields', 'continent', 'date_error_message', 'delete', 'from_db', 'full_clean',
##'geoName', 'get_deferred_fields', 'glwdCountry', 'glwdCountry2', 'id', 'intercept', 'lakeName', 'medianGdp',
##'nCountry', 'nGlwd', 'nYears', 'objects', 'pValue', 'pk', 'poly', 'population', 'prepare_database_save', 
##'rSquared', 'refresh_from_db', 'save', 'save_base', 'serializable_value', 'slope', 'sovereignty', 'stdErr', 
##'subregion', 'typeGlwd', 'unRegion', 'unique_error_message', 'validate_unique']

# print attributes from first result in query filter
print MaxExtent.objects.filter(poly__contains=pnt_wkt)[0].subregion
print MaxExtent.objects.filter(poly__contains=pnt_wkt)[0].areaMax
print MaxExtent.objects.filter(poly__contains=pnt_wkt)[0].geoName

# print objects with id < 12
print MaxExtent.objects.filter(id__lt=12)
## <QuerySet [<MaxExtent: ID 2: Not named (-31.2123, 83.6501)>, <MaxExtent: ID 3: Not named (-33.9099, 83.649)>, <MaxExtent: ID 4: Not named (-34.0536, 83.6419)>, <MaxExtent: ID 5: Not named (-31.2151, 83.6449)>, <MaxExtent: ID 6: Not named (-31.1007, 83.6407)>, <MaxExtent: ID 7: Not named (-31.2671, 83.6284)>, <MaxExtent: ID 8: Not named (-30.985, 83.6324)>, <MaxExtent: ID 9: Not named (-34.1485, 83.6233)>, <MaxExtent: ID 10: Not named (-30.9735, 83.6261)>, <MaxExtent: ID 11: Not named (-33.5948, 83.6199)>]>


# print one exact object from db, where id=12
print MaxExtent.objects.get(id=12)
# prob same as .filter(id=12)[0]
## 

# get average max area for all Portugal water bodies
import numpy as np
areas=[]
for r in MaxExtent.objects.filter(geoName='Portugal'):
    print r
    print r.geoName
    print type(r.areaMax)
    areas.append(float(r.areaMax))

print areas
print np.average(areas)
