from django.urls import path

from .views import IndexView, MapView, ListView, PlaceDetailsView, \
    SignUpView, SignInView, LogoutView

from .views import DatasetPlacesView

urlpatterns = [
    path(r'', IndexView.as_view(), name='index'),
    path(r'mapa/', MapView.as_view(), name='map'),
    path(r'lista/', ListView.as_view(), name='list'),
    path(r'obiekt/<int:place_id>', PlaceDetailsView.as_view(), name='place-details'),

    path(r'zarejestruj', SignUpView.as_view(), name='register'),
    path(r'zaloguj', SignInView.as_view(), name='login'),
    path(r'wyloguj', LogoutView.as_view(), name='logout'),

    path(r'dataset-places/', DatasetPlacesView.as_view(), name='dataset-places'),
]
