from django.db import models

# Create your models here.
class contactform(models.Model):
    name=models.CharField(max_length=20)
    phone=models.CharField(max_length=15)
    address=models.CharField(max_length=255)