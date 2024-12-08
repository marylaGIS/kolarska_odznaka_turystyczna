from datetime import date

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields


class VisitPlaceForm(forms.Form):
    tourist_id = forms.IntegerField(widget=forms.HiddenInput)
    place_id = forms.IntegerField(widget=forms.HiddenInput)
    visit_date = forms.DateField(widget=forms.SelectDateWidget(),
                                 initial=date.today(),
                                 label='Data zwiedzenia')


class UnvisitPlaceForm(forms.Form):
    tourist_id = forms.IntegerField(widget=forms.HiddenInput)
    place_id = forms.IntegerField(widget=forms.HiddenInput)
