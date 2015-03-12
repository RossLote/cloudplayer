from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView
from . import views

urlpatterns = patterns('cloudplayer.views',
    # Examples:
    # url(r'^$', 'cloudplayer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', TemplateView.as_view(template_name='cloudplayer/index.html'), name='index'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^m/', include('music.urls', namespace='music')),
    url(r'^api/', include('music.api_urls', namespace='api')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
