from django.urls import include, path
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
    path('main/',views.main, name='main'),
    path('addprofile/',views.add_profile, name='add_profile'),
    path('profile/<int:info_id>/',views.profile, name='profile'),
    path('index/',views.index, name='index')
]