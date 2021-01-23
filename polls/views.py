from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from .models import Info
from .forms import InfoForm


def add_profile(request):
    """ 
    Function for create event with form and only logged in user can create the event 
    and render create event page.
    """
    form = InfoForm(request.POST, request.FILES)
    if form.is_valid():
        first_name = form.data.get('first_name')
        last_name = form.data.get('last_name')
        email = form.data.get('email')
        tel = form.data.get('tel')
        short_description = form.data.get('short_description')
        info = Info(first_name=first_name,last_name=last_name,
                    email=email,short_description=short_description,tel=tel)
        info.save()
        return HttpResponseRedirect(reverse('profile'))
    return render(request, 'add_profile.html', {'form': form})

def profile(request):
    return render(request, 'profile.html')

