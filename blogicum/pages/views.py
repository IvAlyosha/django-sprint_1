from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def about(request):   
     
    template = 'about.html'
    return render(request, template) 

def rules(request): 

    template = 'rules.html'
    return render(request, template) 

# Create your views here.
