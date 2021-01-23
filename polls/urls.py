from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    path('contactme/',views.add_profile, name='add_profile'),
    path('',views.profile, name='profile'),
]