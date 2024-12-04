from rest_framework_gis.serializers import GeoFeatureModelListSerializer

from .models import Place


class PlaceSerializer(GeoFeatureModelListSerializer):
    class Meta:
        model = Place
        geo_field = 'geom'
        fields = ('name',)
