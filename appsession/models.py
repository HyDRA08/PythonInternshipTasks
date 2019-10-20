from django.db import models

# Create your models here.
class myformsession(models.Model):
    user1=models.CharField(max_length=20)
    pass1=models.CharField(max_length=20)
