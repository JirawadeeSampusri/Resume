from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class Info(models.Model):
    """ Model for put the infomation of event to database. """
    photo = models.ImageField(upload_to='upload/', default=None)
    first_name = models.CharField("First Name", default="",max_length=254)
    last_name = models.CharField("Last Name", default="",max_length=254)
    gender =  models.CharField("Gender", default="",max_length=254)
    nationality = models.CharField("Nationality", default="",max_length=254)
    interest = models.TextField('Short Description', default="", max_length=300)
    email = models.EmailField("E-mail", default="",max_length=254)
    address = models.CharField("Address", default="",max_length=500)
    short_description = models.TextField('Short Description', default="", max_length=300)
    university = models.CharField('University', default="", max_length=80)
    bachelor = models.CharField('Bachelor', default="", max_length=80)
    major = models.CharField('Major', default="", max_length=80)
    start_study = models.DateTimeField('Start Date', default="YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]")
    end_study = models.DateTimeField('End Date', default="YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]")

    def get_photo(self):
        return self.photo

    def get_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_email(self):
        return self.email

    def get_nationality(self):
        return self.nationality

    def get_gender(self):
        return self.gender

    def get_address(self):
        return self.address
    
    def get_short_description(self):
        return self.short_description
    
    def get_interest(self):
        return self.interest
    
    def get_university(self):
        return self.university

    def get_bachelor(self):
        return self.bachelor
    
    def get_major(self):
        return self.major
    
    def get_start_study(self):
        return self.start_study
    
    def get_end_study(self):
        return self.end_study

   