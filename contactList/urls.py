'''
Created on 2013-04-09

@author: Ian
'''
from django.conf.urls import patterns, url

from contactList import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='contact')
                       )
