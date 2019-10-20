from django.db import models

# Create your models here.
class student(models.Model):
    FirstName=models.CharField(max_length=20,default="")
    LastName=models.CharField(max_length=20,default="")
    Age=models.IntegerField(default=2)
