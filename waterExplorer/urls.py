from django.conf.urls import url#, patterns, include
#from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    #url(r'^countryQuery/(?P<country_name>\w+)/$', views.query_by_country, name='query_by_country'),
    #url(r'^countryQuery/(?P<country_name> \w+)/$', views.query_by_country, name='query_by_country'),
    url(r'^viewID/(?P<req_id>[0-9]+)/$', views.objectViewer, name='objectViewer'),
    #url(r'^searchByName/$', views.getLakeName, name='getLakeName'),
    url(r'^search/$', views.searchDb, name='searchDb')
]

#urlpatterns = [
#    path('', views.index, name='index'),
#    path('<str:country>/', views.query_by_country, name='countryQuery'),

#]
