from django.core.serializers import serialize
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.shortcuts import redirect, render, HttpResponse
from django.views import View

from .forms import SignUpForm
from .models import Place, Tourist


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

        ctx = {'place': place}

        return render(request, 'place-details.html', ctx)


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
