from django.conf.urls import patterns, include, url

from django.contrib import admin


#import templates 
from leavesystem.views import *

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'LeaveSystem.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index),
    url(r'^login/$', login),
    url(r'^logout/$', logout),
    url(r'^leavenList/$', leavenList),
    url(r'^calendar/$', index),
    url(r'^addLeavenForm/$', addLeavenForm),
    url(r'^editLeavenForm/(?P<id>\d+)', editLeavenForm),
    url(r'^delLeavenForm/(?P<id>\d+)', delLeavenForm),
    url(r'^submitLeavenForm/$', submitLeavenForm),
)
