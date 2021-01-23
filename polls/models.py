from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class Info(models.Model):
    """ Model for put the infomation of event to database. """
    first_name = models.CharField("First Name", default="",max_length=254)
    last_name = models.CharField("Last Name", default="",max_length=254)
    email = models.EmailField("E-mail", default="",max_length=254)
    tel = models.CharField("Tel", default="",max_length=254)
    short_description = models.TextField('Short Description', default="", max_length=300)

    def get_tel(self):
        return self.get_tel
    
    def get_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_email(self):
        return self.email

    def get_short_description(self):
        return self.short_description
    
  
   