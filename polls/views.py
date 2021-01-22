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
        photo = form.cleaned_data.get('photo') 
        first_name = form.data.get('first_name')
        last_name = form.data.get('last_name')
        gender = form.data.get('gender')
        nationality = form.data.get('nationality')
        interest = form.data.get('interest')
        email = form.data.get('email')
        skill = form.data.get('skill')
        tel = form.data.get('tel')
        gpa = form.data.get('gpa')
        branch = form.data.get('branch')
        address = form.data.get('address')
        short_description = form.data.get('short_description')
        university = form.data.get('university')
        bachelor = form.data.get('bachelor')
        major = form.data.get('major')
        start_study = form.data.get('start_study')
        birth = form.data.get('birth')
        end_study = form.data.get('end_study')
        info = Info(photo=photo,first_name=first_name,last_name=last_name,gender=gender,
                    nationality=nationality,interest=interest,email=email,
                    address=address,short_description=short_description,
                    university=university,bachelor=bachelor,major=major,
                    start_study=start_study,end_study=end_study,
                    birth=birth,tel=tel,gpa=gpa,skill=skill,branch=branch)
        info.save()
        return render(request, 'profile.html', {'info': info})
    return render(request, 'add_profile.html', {'form': form})

def profile(request,info_id):
    info = get_object_or_404(Info, pk=info_id)
    return render(request, 'profile.html', {'info':info})

def index(request):
    all_info = Info.objects.all()
    print(all_info)
    return render(request, 'index.html', {'all_info':all_info})

def main(request):
    return render(request, 'main.html')