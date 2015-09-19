from django.shortcuts import render, redirect
from django.views import generic
from django.core import serializers
from django.http import HttpResponse
from liveupdate.models import Update
from datetime import datetime
from django.core.urlresolvers import reverse

class ListView(generic.ListView):
    model = Update

    def get_queryset(self):
        return Update.objects.all()

def add_update(request):
    if request.method == 'POST':
        u = Update()
        u.timestamp = datetime.now(),
        u.text = request.POST['updateText']
        u.save() 
        return redirect('update_list')

def updates_after(request, id):
    response = HttpResponse()
    response['Content-Type'] = "text/javascript"
    response.write(serializers.serialize("json",
        Update.objects.filter(pk__gt=id)))
    return response


    
