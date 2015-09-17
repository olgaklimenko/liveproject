from django.shortcuts import render
from django.views import generic
from django.core import serializers
from django.http import HttpResponse
from liveupdate.models import Update

class ListView(generic.ListView):
    model = Update

    def get_queryset(self):
        return Update.objects.all()

def updates_after(request, id):
    response = HttpResponse()
    response['Content-Type'] = "text/javascript"
    response.write(serializers.serialize("json",
        Update.objects.filter(pk__gt=id)))
    return response
