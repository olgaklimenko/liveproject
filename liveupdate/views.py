from django.shortcuts import render
from django.views import generic
from liveupdate.models import Update

class ListView(generic.ListView):
    model = Update

    def get_queryset(self):
        return Update.objects.all()
