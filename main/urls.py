from django.conf.urls import patterns, include, url
from django.contrib import admin
from main.models import Campaign

urlpatterns = patterns('',
	url(r'^blue_man', 'main.views.views.blue_man', name='blue_man'),
	url(r'^dont_care', 'main.views.views.dont_care', name='dont_care'),
	url(r'^mouse', 'main.views.views.mouse', name='mouse'),
	url(r'^friend', 'main.views.views.friend', name='friend'),
	url(r'^old_school', 'main.views.views.old_school', name='old_school'),
	url(r'^closure', 'main.views.views.closure', name='closure'),
	url(r'^$', 'main.views.views.splash', name='splash'),
    url(r'^about', 'main.views.views.about', name='about'),
    url(r'^campaigns', 'main.views.views.campaigns', name='campaigns'),
    url(r'^admin/', include(admin.site.urls))
)