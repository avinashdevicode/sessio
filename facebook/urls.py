from django.conf.urls import patterns, include, url
from products import urls as URL
from django.conf import settings
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
                       url(r'', include('social_auth.urls')),
                       #url(r'^login/', 'facebook.views.viewLogin'),
                       url(r'^home/', 'facebook.views.viewHome'),
                       url(r'logout/', 'facebook.views.viewLogout'),
                       url(r'^log/in/', 'facebook.views.viewLogin'),
                       url(r'^product/',include(URL)),
    # Examples:
    # url(r'^$', 'facebook.views.home', name='home'),
    # url(r'^facebook/', include('facebook.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
if settings.DEBUG:
    urlpatterns += patterns('django.views.static',
                            (r'^media/(?P<path>.*)',
                             'serve',
                             {'document_root':settings.MEDIA_ROOT}),)
