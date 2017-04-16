from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView
from wlapi.models import Visit, Hit
from django.http import JsonResponse
from django.views.generic.edit import CreateView

# Create your views here.

class VisitCreate(CreateView):

    model = Visit
    fields = ['reason']

class HitCreate(CreateView):

    model = Hit
    fields = []

class HomeView(TemplateView):

    template_name = 'wlapi/home.html'