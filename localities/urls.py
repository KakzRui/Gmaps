from django.conf.urls import *

urlpatterns = patterns('localities.views',
    url(r'^$', 'index', name='localities-index'),
    url(r'^save$', 'save', name='localities-save'),
)