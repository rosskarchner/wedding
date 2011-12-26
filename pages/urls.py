from django.conf.urls.defaults import patterns, include, url
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('pages.views',
    
    
    url(r'^logout$', 'logout', name='logout'),
    url(r'^login$', 'login', name='login'),
    url(r'^$', 'getpage', name='front'),
    url(r'^songs/$', 'songs', name='songs'),
    url(r'^(?P<name>\w+).html$', 'getpage',name='getpage'),
)
