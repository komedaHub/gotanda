import django_filters
from rest_framework import viewsets, filters

from django.shortcuts import render
from django.http import HttpResponse
from .models import Omikuji, Omikuji_items
from .serializer import OmikujiSerializer,OmikujiItemSerializer
from .forms import SearchForm,OmikujiForm

class OmikujiViewSet(viewsets.ModelViewSet):
    queryset = Omikuji.objects.all()
    serializer_class = OmikujiSerializer
    filter_fields = ('id','name')

class OmikujiItemViewSet(viewsets.ModelViewSet):
    queryset = Omikuji_items.objects.all()
    serializer_class = OmikujiItemSerializer

# Create your views here.
def index(request):
    searchForm = SearchForm(request.GET)
    if searchForm.is_valid():
        keyword = searchForm.cleaned_data['keyword']
        omikuji_list = Omikuji.objects.filter(name__contains=keyword)
    else:
        searchForm = SearchForm()
        omikuji_list = Omikuji.objects.all()

    context = {
        'message': 'Welcome my Omikuji',
        'omikuji_list': omikuji_list,
        'searchForm': searchForm,
    }
    return render(request, 'index.html', context)

def new(request):
    omikujiForm = OmikujiForm()

    context = {
        'message': 'New omikuji',
        'omikujiForm': omikujiForm,
    }
    return render(request, 'new.html', context)

def create(request):
    if request.method == 'POST':
        omikujiForm = OmikujiForm(request.POST)
        if omikujiForm.is_valid():
            omikuji = omikujiForm.save()

    searchForm = SearchForm()
    omikuji_list = Omikuji.objects.all()

    context = {
        'message': 'Welcome my Omikuji',
        'omikuji_list': omikuji_list,
        'searchForm': searchForm,
    }
    return render(request, 'index.html', context)

def edit(request, id):
    omikuji = Omikuji.objects.get(id=id)
    omikujiForm = OmikujiForm(instance=omikuji)

    context = {
        'message': 'Edit omikuji',
        'omikuji': omikuji,
        'omikujiForm': omikujiForm,
    }
    return render(request, 'edit.html', context)

def update(request, id):
    if request.method == 'POST':
        omikuji = Omikuji.objects.get(id=id)
        omikujiForm = OmikujiForm(request.POST, instance=omikuji)
        if omikujiForm.is_valid():
            omikujiForm.save()

    searchForm = SearchForm()
    omikuji_list = Omikuji.objects.all()

    context = {
        'message': 'Welcome my Omikuji',
        'omikuji_list': omikuji_list,
        'searchForm': searchForm,
    }
    return render(request, 'index.html', context)

def delete(request, id):
    omikuji = Omikuji.objects.get(pk=id)
    omikuji.delete()

    omikuji_list = Omikuji.objects.all()
    context = {
        'message': 'Welcome my Omikuji',
        'omikuji_list': omikuji_list,
    }
    return render(request, 'index.html', context)

def detail(request, id):
    omikuji_item_list = Omikuji_items.objects.filter(omikuji_id=id)
    context = {
        'message': 'Welcome my Omikuji',
        'omikuji_item_list': omikuji_item_list,
    }
    return render(request, 'detail.html', context)
