'''
Created on 2013-04-09

@author: Ian
'''
from django.contrib import admin
from contactList.models import Location, Email

admin.site.register(Email)
admin.site.register(Location)