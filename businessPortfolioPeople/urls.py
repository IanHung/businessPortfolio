'''
Created on 2013-04-03

@author: Ian
'''
from django.conf.urls import patterns, url

from businessPortfolioPeople import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='people-index')
                       )
