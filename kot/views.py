from django.core.serializers import serialize
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
from django.views import View

from .forms import SignUpForm, VisitPlaceForm, UnvisitPlaceForm
from .models import Place, Tourist, TouristsPlaces


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class MapView(View):
    def get(self, request):
        return render(request, 'map.html')


class ListView(View):
    def get(self, request):
        return render(request, 'list.html')


class PlaceDetailsView(View):
    def get(self, request, place_id):
        place = Place.objects.get(pk=place_id)
        tourist_id = request.user.id

        try:
            visited_place = TouristsPlaces.objects.get(tourist_id=tourist_id,
                                                       place_id=place_id)
        except TouristsPlaces.DoesNotExist:
            visited_place = None

        if visited_place:
            form = UnvisitPlaceForm(
                initial={
                    'tourist_id': tourist_id,
                    'place_id': place_id
                }
            )
            visited = True
        else:
            form = VisitPlaceForm(
                initial={
                    'tourist_id': tourist_id,
                    'place_id': place_id
                }
            )
            visited = False

        ctx = {'place': place,
               'form': form,
               'visited_place': visited_place,
               'visited': visited}

        return render(request, 'place-details.html', ctx)

    def post(self, request, place_id):
        form = VisitPlaceForm(request.POST)
        if form.is_valid():
            tourist_id = form.cleaned_data['tourist_id']
            place_id = form.cleaned_data['place_id']
            visit_date = form.cleaned_data['visit_date']

            TouristsPlaces.objects.create(
                tourist_id=tourist_id,
                place_id=place_id,
                visit_date=visit_date
            )

            return redirect(f'/obiekt/{place_id}')

        form = UnvisitPlaceForm(request.POST)
        if form.is_valid():
            tourist_id = form.cleaned_data['tourist_id']
            place_id = form.cleaned_data['place_id']

            visited_place = TouristsPlaces.objects.get(
                tourist_id = tourist_id,
                place_id = place_id
            )

            visited_place.delete()

            return redirect(f'/obiekt/{place_id}')


class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request, 'sign-up.html', {'form': form})
    
    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            if not User.objects.filter(username=username).exists():
                form.save()
            user = User.objects.get(username=username)
            Tourist.objects.create(user=user)
        else:
            return redirect('zarejestruj')

        return redirect('login')


class SignInView(LoginView):
    template_name = 'sign-in.html'
    next_page = '/'


class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')


class DatasetPlacesView(View):
    def get(self, request):
        places = serialize('geojson', Place.objects.all())
        return HttpResponse(places, content_type='json')
