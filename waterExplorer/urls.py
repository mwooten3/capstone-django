from django.conf.urls import url#, patterns, include
#from django.urls import path
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
#    url(r'^$', TemplateView.as_view(template_name="waterExplorer/index.html")),
    url(r'^$', views.index, name='index'),
    #url(r'^countryQuery/(?P<country_name>\w+)/$', views.query_by_country, name='query_by_country'),
    #url(r'^countryQuery/(?P<country_name> \w+)/$', views.query_by_country, name='query_by_country'),
    url(r'^viewID/(?P<req_id>[0-9]+)/$', views.objectViewer, name='objectViewer'),
    #url(r'^searchByName/$', views.getLakeName, name='getLakeName'),
    url(r'^search/$', views.searchDb, name='searchDb'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact')
]

#if settings.DEBUG:
#    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#    urlpatterns += staticfiles_urlpatterns()
#print urlpatterns
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
#urlpatterns += staticfiles_urlpatterns()


#urlpatterns = [
#    path('', views.index, name='index'),
#    path('<str:country>/', views.query_by_country, name='countryQuery'),

#]
