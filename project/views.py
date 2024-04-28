from django.shortcuts import render
from django.views.generic import ListView   # help to read data base
from django.views.generic import TemplateView

class Pricing(TemplateView):
    template_name = "pricing.html"

class Home(TemplateView):
    template_name = 'home.html'