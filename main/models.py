from django.db import models
from django import forms
from django.contrib.auth.models import User

class SolarTip(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def _str_(self):
        return self.title


from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    

    

     
  
     

# Create your models here.
