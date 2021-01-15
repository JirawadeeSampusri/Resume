from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Info,Education
from .forms import EducationForm,InfoForm
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import login, authenticate,logout
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
import datetime
import sys

def add_profile(request):
    """ 
    Function for create event with form and only logged in user can create the event 
    and render create event page.
    """
    return render(request, 'polls/add_profile.html')
    # form = EventForm(request.POST, request.FILES)
    # number_people = form.data.get('number_people')
    # arrange_time = form.data.get('arrange_time')
    # if request.method == 'POST':
    #     if form.is_valid():
    #         if int(number_people) >= 10:
    #             try:
    #                 if datetime.datetime.strptime(arrange_time,'%Y-%m-%d %H:%M').date() > timezone.now().date():
    #                     photo = form.cleaned_data.get('photo') 
    #                     event_name = form.data.get('event_name')
    #                     location = form.data.get('location')
    #                     short_description = form.data.get('short_description')
    #                     long_description = form.data.get('long_description')
    #                     event = Event(event_name = event_name, location=location, short_description = short_description, long_description = long_description, arrange_time = arrange_time, number_people = number_people,full=False, photo=photo, user=request.user)
    #                     event.save()
    #                     messages.success(request, f"You've created the {event_name} event!")
    #                     return HttpResponseRedirect(reverse('index'))
    #                 else:
    #                     messages.warning(request, "Arrangement date must be in the future!")
    #             except:
    #                 messages.warning(request, f"You should input the date and time as format!")
    #                 return render(request, 'Kvent/create-event-page.html', {'form': form})
    #         else :
    #             messages.warning(request, "Number of paricipants must more than 10 or equal")
    #     else:
    #         messages.warning(request, f"You should input the date and time as format!")
    # return render(request, 'polss/add_profile.html', {'form': form})

def resume(request):
    """ 
    Function for create event with form and only logged in user can create the event 
    and render create event page.
    """
    return render(request, 'polls/resume.html')