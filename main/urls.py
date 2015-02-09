from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',

	url(r'^$', 'main.views.form.splash', name='splash'),
    # Examples:
    # url(r'^$', 'main.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
