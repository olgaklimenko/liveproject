from django.conf.urls import patterns, url
from liveupdate.models import Update
from liveupdate import views

urlpatterns = patterns('',
    url(r'^$', views.ListView.as_view()),
    url(r'^updates-after/(?P<id>\d+)/$', views.updates_after),
)
