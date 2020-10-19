from django.shortcuts import render
from .models import Brand, Item
from django.http import HttpResponse, Http404
from django.template import loader

# Create your views here.

def index(request):
    allBrands = Brand.objects.all()
    template = loader.get_template('itemTemplate/index.html')
    context = {'allBrands': allBrands}
    return HttpResponse(template.render(context, request))

def brands(request):
    allBrands = Brand.objects.all()
    template = loader.get_template('itemTemplate/index.html')
    context = {'allBrands': allBrands}
    return HttpResponse(template.render(context, request))

# IMPLEMENT WITH POSTGRESQL SEARCH ENGINE

def search(request):
    search_term = ''
    search_result = []
    if 'search' in request.GET:
        search_term = request.GET
        search_result = Brand.objects.all().filter()

