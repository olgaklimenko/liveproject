from django.conf.urls import patterns, url
from liveupdate.models import Update
from liveupdate.views import ListView 

urlpatterns = patterns('',
    url(r'^$', ListView.as_view()),
)
