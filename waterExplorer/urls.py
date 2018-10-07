from django.conf.urls import url
#from django.urls import path


from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^countryQuery/(?P<country_name>\w+)/$', views.query_by_country, name='query_by_country'),
    #url(r'^countryQuery/(?P<country_name> \w+)/$', views.query_by_country, name='query_by_country'),
    url(r'^viewer/(?P<req_id>[0-9]+)/$', views.viewer, name='viewer')
]

#urlpatterns = [
#    path('', views.index, name='index'),
#    path('<str:country>/', views.query_by_country, name='countryQuery'),

#]
