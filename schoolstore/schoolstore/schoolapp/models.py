from django.db import models
from django.urls import reverse
# Create your models here.



class Department(models.Model):
    objects = None
    name=models.CharField(max_length=250)


    def __str__(self):
        return self.name


