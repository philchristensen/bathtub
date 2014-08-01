from django.conf.urls.defaults import patterns, include, url

from bathtub.api.viewsets import router

urlpatterns = patterns('bathtub.scripts.views',
    url(r'^', include(router.urls)),
    url(r'^auth/$', include('rest_framework.urls', namespace='rest_framework'))
)
