from django import forms
from .models import Info
from django.forms.widgets import Textarea

class InfoForm(forms.ModelForm):
    """ Form for inputing a new event """
    class Meta:
        model = Info
        fields = ['first_name','last_name', 'email', 'short_description','tel']
        photo = forms.ImageField()
        first_name = forms.CharField(
            widget=forms.TextInput(
            attrs={'type':'input', 'id':'first_name'}
            ))
        last_name = forms.CharField(
            widget=forms.TextInput(
            attrs={'type':'input', 'id':'last_name'}
            ))
        email = forms.CharField(
            widget=forms.TextInput(
            attrs={'type':'input', 'id':'email'}
            ))  
        tel = forms.CharField(
            widget=forms.TextInput(
            attrs={'type':'input', 'id':'tel'}
            ))
        short_description = forms.CharField(
            widget=forms.TextInput(
            attrs={'type':'input', 'id':'short_description'}
            ))
       
        