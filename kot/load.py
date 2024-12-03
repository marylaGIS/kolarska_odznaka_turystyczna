from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import Place

# Auto-generated `LayerMapping` dictionary for Place model
place_mapping = {
    'voivodeship': 'voivodeship',
    'localization': 'localization',
    'name': 'name',
    'link1': 'link1',
    'link2': 'link2',
    'geom': 'POINT',
}

places_geojson = Path(__file__).resolve().parent / "static" / "data" / "places.geojson"

def run(verbose=True):
    lm = LayerMapping(Place, places_geojson, place_mapping, transform=False)
    lm.save(strict=True, verbose=verbose)
