from django.conf.urls import patterns, url
from views import index_list

urlpatterns = patterns('',
    #  url(r'^/photolist/index/$', IndexView.as_view()),
    url(r'^$', index_list, name='index_list')
)
