'''
Created on Mar 11, 2014

@author: avinash
'''
from django.conf.urls import patterns, include, url
import products


urlpatterns = patterns('',
                       url(r'^create/', 'products.views.viewCreate'),
                       url(r'update/(?P<pk>\d+)', 'products.views.viewUpdate', name = 'viewUpdate'),
                       url(r'delete/(?P<pk>\d+)', 'products.views.viewDelete', name = 'viewUpdate'),    
)