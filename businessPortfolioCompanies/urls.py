'''
Created on 2013-04-03

@author: Ian
'''
from django.conf.urls import patterns, url

from businessPortfolioCompanies import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='companies-index')
                       )


