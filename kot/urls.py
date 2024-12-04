from django.urls import path

from .views import IndexView, MapView

from .views import DatasetPlacesView

urlpatterns = [
    path(r'', IndexView.as_view(), name='index'),
    path(r'mapa/', MapView.as_view(), name='map'),

    path(r'dataset-places/', DatasetPlacesView.as_view(), name='dataset-places'),
]
