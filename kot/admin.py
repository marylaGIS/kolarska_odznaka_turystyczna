from django.contrib import admin
from leaflet.admin import LeafletGeoAdmin

from .models import Place, Tourist


class PlaceAdmin(LeafletGeoAdmin):
    list_display = ['id', 'voivodeship', 'localization',
                    'name', 'geom', 'link1', 'link2']
    

class TouristAdmin(LeafletGeoAdmin):
    list_display = ['home', 'geom', 'public', 'user']


admin.site.register(Place, PlaceAdmin)
admin.site.register(Tourist, TouristAdmin)
