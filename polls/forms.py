from django import forms
from .models import Info, Education
from django.forms.widgets import Textarea

class InfoForm(forms.ModelForm):
    """ Form for inputing a new event """
    class Meta:
        model = Info
        fields = ['photo','first_name','last_name', 'gender', 'nationality', 'interest', 'email', 'address', 'short_description']
        photo = forms.ImageField()
        first_name = forms.CharField(
            widget=forms.TextInput(
            attrs={'type':'input', 'id':'first_name'}
            ))
        last_name = forms.CharField(
            widget=forms.TextInput(
            attrs={'type':'input', 'id':'last_name'}
            ))
        gender = forms.CharField(
            widget=forms.TextInput(
            attrs={'type':'input', 'id':'gender'}
            ))
        nationality = forms.CharField(
            widget=forms.TextInput(
            attrs={'type':'input', 'id':'nationality'}
            ))
        interest = forms.CharField(
            widget=forms.TextInput(
            attrs={'type':'input', 'id':'interest'}
            ))
        email = forms.CharField(
            widget=forms.TextInput(
            attrs={'type':'input', 'id':'email'}
            ))
        address = forms.CharField(
            widget=forms.TextInput(
            attrs={'type':'input', 'id':'address'}
            ))
        short_description = forms.CharField(
            widget=forms.TextInput(
            attrs={'type':'input', 'id':'short_description'}
            ))
        # arrange_time = forms.DateTimeField(
        #     input_formats=['YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]'],
        #     widget=forms.DateTimeInput(
        #         attrs={'type':'datetime', 'id': 'arrange-time'}
        #     ))

class EducationForm(forms.ModelForm):
    """ Form for inputing a new event """
    class Meta:
        model = Education
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
        