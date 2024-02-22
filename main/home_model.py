# main/home_models.py
from django.db import models
from .models import User

class Home(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    size = models.IntegerField()
    insulation = models.CharField(max_length=50)
    heating_system = models.CharField(max_length=50)
    cooling_system = models.CharField(max_length=50)

    # other fields here