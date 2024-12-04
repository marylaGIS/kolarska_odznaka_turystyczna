from django.core.serializers import serialize
from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from django.views import View

from .models import Place


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class MapView(View):
    def get(self, request):
        return render(request, 'map.html')


class DatasetPlacesView(View):
    def get(self, request):
        places = serialize('geojson', Place.objects.all())
        return HttpResponse(places, content_type='json')
