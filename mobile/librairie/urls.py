from django.conf.urls.defaults import *
from django.views.generic import TemplateView
from mobile.urls import *
from librairie.views import *

urlpatterns = patterns('librairie.views',
    url(r'^$', TemplateView.as_view(template_name="mobile/index.html")),
    url(r'^sujet/$', 'sujet'),
    url(r'^new/$', new, name='new'),
    url(r'^search/$', search, name='search'),
    url(r'^contact/$', 'contact'),
    url(r'^detail/(?P<id>\d+)/$', 'detail'),
    url(r'^resume/(?P<id>\d+)/$', 'resume'),
    url(r'^resume2/(?P<id>\d+)/$', 'resume2'),
)
