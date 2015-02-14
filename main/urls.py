from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	url(r'^index', 'main.views.form.index', name='index'),
	url(r'^$', 'main.views.form.splash', name='splash'),
    url(r'^about', 'main.views.form.about', name='about'),
    url(r'^campaign1', 'main.views.form.campaign1', name='campaign1'),
    url(r'^campaign2', 'main.views.form.campaign2', name='campaign2'),
    url(r'^campaign3', 'main.views.form.campaign3', name='campaign3'),
    url(r'^admin/', include(admin.site.urls))
)