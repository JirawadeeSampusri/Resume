from django.db import models
from datetime import datetime
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class Info(models.Model):
    """ Model for put the infomation of event to database. """
    photo = models.ImageField(upload_to='upload/', default='https://storage.googleapis.com/kvent_bucket/upload/no_img.png')
    first_name = models.CharField("First Name", max_length=254)
    last_name = models.CharField("Last Name", max_length=254)
    gender =  models.CharField("Gender", max_length=254)
    nationality = models.CharField("Nationality", max_length=254)
    interest = models.TextField('Interest', default="", max_length=100)
    email = models.EmailField("E-mail", max_length=254)
    address = models.CharField("Address", max_length=125)
    short_description = models.TextField('Short Description', default="", max_length=100)

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
    
class Education(models.Model):
    """ Model for put the infomation of event to database. """
    university = models.TextField('University', default="", max_length=80)
    bachelor = models.TextField('Bachelor', default="", max_length=80)
    major = models.TextField('Major', default="", max_length=80)
    start_study = models.DateTimeField('Start Date', default=timezone.now())
    end_study = models.DateTimeField('End Date', default=timezone.now())

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

   