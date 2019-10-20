from django.db import models

# Create your models here.
citynames=(
    ('delhi','Delhi'),
    ('damascus','Damascus'),
    ('istambul','Istambul'),
    ('newyork','NewYork'),
    ('london','London'),
    ('berlin','Berlin'),
)
class myform(models.Model):
    name=models.CharField(max_length=20)
    phone=models.CharField(max_length=15)
    address=models.CharField(max_length=255)
    gender=models.CharField(max_length=10)
    city=models.CharField(choices=citynames,max_length=10)
    email=models.CharField(max_length=20)
    image=models.FileField(upload_to='images/')