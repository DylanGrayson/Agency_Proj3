from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	#url(r'^index', 'main.views.form.index', name='index'),
	url(r'^$', 'main.views.views.splash', name='splash'),
    url(r'^about', 'main.views.views.about', name='about'),
    url(r'^campaigns', 'main.views.views.campaigns', name='campaigns'),
    url(r'^admin/', include(admin.site.urls))
)