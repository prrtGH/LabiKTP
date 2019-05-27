from django.conf.urls import patterns, include, url
from articles.views import create_post
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'articles.views.archive', name='archive'),
    url(r'^article/(?P<article_id>\d+)$','articles.views.get_article',name='get_article'),
    url(r'^article/new/$', 'articles.views.create_post', name='create_post'),
    url(r'^reg/$', 'articles.views.reg', name='reg'),
    url(r'^auth/$', 'articles.views.aut', name='aut'),
    # url(r'^blog/', include('blog.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

