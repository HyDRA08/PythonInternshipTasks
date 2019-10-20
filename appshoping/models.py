from django.db import models

# Create your models here.
class shoping(models.Model):
    catid=models.CharField(max_length=20)
    catname=models.CharField(max_length=20)
    catparentid=models.CharField(max_length=10)
    def __str__(self):
        return self.catname
    class Meta:
        verbose_name_plural="Shoping"