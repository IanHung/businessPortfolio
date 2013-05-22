from django.conf.urls import patterns, include, url
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'fixedPages.views.home', name='home'),
    # url(r'^contact/$', 'fixedPages.views.contact', name='contact'),
    # url(r'^BusinessPortfolio/', include('BusinessPortfolio.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^news/' , include('businessPortfolioNews.urls')),
    url(r'^people/' , include('businessPortfolioPeople.urls')),
    url(r'^companies/', include('businessPortfolioCompanies.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^contact/$', include('contactList.urls')),
)

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))
