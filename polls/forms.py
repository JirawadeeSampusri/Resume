from django import forms
from .models import Event, User
from django.forms.widgets import Textarea
from polls.models import User
from django.contrib.auth.forms import UserCreationForm

class InfoForm(forms.ModelForm):
    """ Form for inputing a new event """
    class Meta:
        model = Event
        fields = ['photo','first_name','last_name', 'gender', 'nationality', 'interest', 'email', 'address', 'short_description']
        photo = forms.ImageField()
        first_name = forms.CharField(
            widget=forms.TextInput(
            attrs={'type':'input', 'id':'name-input'}
            ))
        last_name = forms.CharField(
            widget=forms.TextInput(
            attrs={'type':'input', 'id':'name-input'}
            ))
        gender = forms.CharField(
            widget=forms.TextInput(
            attrs={'type':'input', 'id':'gender-input'}
            ))
        nationality = forms.CharField(
            widget=forms.TextInput(
            attrs={'type':'input', 'id':'nationality-input'}
            ))
        interest = forms.CharField(
            widget=forms.TextInput(
            attrs={'type':'input', 'id':'interest-input'}
            ))
        email = forms.CharField(
            widget=forms.TextInput(
            attrs={'type':'input', 'id':'email-input'}
            ))
        address = forms.CharField(
            widget=forms.TextInput(
            attrs={'type':'input', 'id':'address-input'}
            ))
        short_description = forms.CharField(
            widget=forms.TextInput(
            attrs={'type':'input', 'id':'short-description-input'}
            ))
        # arrange_time = forms.DateTimeField(
        #     input_formats=['YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]'],
        #     widget=forms.DateTimeInput(
        #         attrs={'type':'datetime', 'id': 'arrange-time'}
        #     ))

class EducationForm(forms.ModelForm):
    """ Form for inputing a new event """
    class Meta:
        model = Event
        fields = ['university','bachelor','major', 'start_study', 'end_study']
        university = forms.CharField(
            widget=forms.TextInput(
            attrs={'type':'input', 'id':'university-input'}
            ))
        bachelor = forms.CharField(
            widget=forms.TextInput(
            attrs={'type':'input', 'id':'bachelor-input'}
            ))
        major = forms.CharField(
            widget=forms.TextInput(
            attrs={'type':'input', 'id':'major-input'}
            ))
        start_study = forms.DateTimeField(
            input_formats=['YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]'],
            widget=forms.DateTimeInput(
                attrs={'type':'datetime', 'id': 'start_study'}
            ))
        end_study = forms.DateTimeField(
            input_formats=['YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]'],
            widget=forms.DateTimeInput(
                attrs={'type':'datetime', 'id': 'end_study'}
            ))
        