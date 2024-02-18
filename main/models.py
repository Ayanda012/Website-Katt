from django.db import models
class SolarTip(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    def _str_(self):
        return self.title
    
class Home(models.Model):
    name = models.CharField(max_length=255)

class EnergyReading(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    kwh = models.DecimalField(max_digits=5, decimal_places=2)

class SolarReading(models.Model):
    home = models.ForeignKey(Home, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    kwh = models.DecimalField(max_digits=5, decimal_places=2)
  
     

# Create your models here.
