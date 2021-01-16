from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from .models import Info,Education
from .forms import EducationForm,InfoForm


def add_profile(request):
    """ 
    Function for create event with form and only logged in user can create the event 
    and render create event page.
    """
    form = InfoForm(request.POST, request.FILES)
    if request.method == "POST" and form.is_valid():
        photo = form.cleaned_data.get('photo') 
        first_name = form.data.get('first_name')
        last_name = form.data.get('last_name')
        gender = form.data.get('gender')
        nationality = form.data.get('nationality')
        interest = form.data.get('interest')
        email = form.data.get('email')
        address = form.data.get('address')
        short_description = form.data.get('short_description')
        info = Info(photo=photo,first_name=first_name,last_name=last_name,gender=gender,
                    nationality=nationality,interest=interest,email=email,
                    address=address,short_description=short_description)
        info.save()
    return render(request, 'add_profile.html', {'form': form})
  
# def resume(request):
#     """ 
#     Function for create event with form and only logged in user can create the event 
#     and render create event page.
#     """
#     return render(request, 'polls/resume.html')