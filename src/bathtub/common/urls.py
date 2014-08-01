from django.conf.urls import patterns, include, url

from bathtub.api.viewsets import router

urlpatterns = patterns('bathtub.common.views',
    url(r'^$', 'home', name='bathtub_home'),
)
