# from django.shortcuts import render

# Create your views here.
from django.template import loader
from django.http import HttpResponse
def home(request):
    "Home page /"
    template = loader.get_template('home.html')
    return HttpResponse(template.render())
