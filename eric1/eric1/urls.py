from django.conf.urls import patterns, include, url
from django.contrib import admin
from main import views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^blog/$', views.blog_overview, name='blog_overview'),
    url(r'^blog/([0-9]+)/$', views.blog_details, name='blog_details'),
    url(r'^admin/', include(admin.site.urls)),
)
