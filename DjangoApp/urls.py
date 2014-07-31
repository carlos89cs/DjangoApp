from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'DjangoApp.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'Principal.views.index'),
    url(r'^privado/$', 'Principal.views.privado'),
    url(r'^admin/', include(admin.site.urls)),
)
