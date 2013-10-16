from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'display.views.home', name='home'),
    # url(r'^display/', include('display.foo.urls')),
    url(r'^hello/','mainmodule.views.main_view'),

    url(r'^$','mainmodule.views.main_view'),
    url(r'^login$','mainmodule.views.login_view'),
    url(r'^jlogin$','mainmodule.views.jlogin'),
    url(r'^logout$','mainmodule.views.logout_view'),
    url(r'^jlogout$','mainmodule.views.jlogout'),
    
    url(r'^accounts/login/$','mainmodule.views.login_view'),

    url(r'^interface$','searchmodule.views.interface_view'),
    url(r'^jinterface$','searchmodule.views.jinterface'),
    url(r'^typehead$','searchmodule.views.typehead'),
    url(r'^jgetquery$','searchmodule.views.jgetquery'),
    url(r'^item(\d+)$','searchmodule.views.item'),
    
    
    #url(r'^image$','searchmodule.views.image'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
from django.conf.urls.static import  static,settings
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
