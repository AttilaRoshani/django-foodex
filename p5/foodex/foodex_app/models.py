from django.db import models
from django.db.models import expressions
from django.utils.regex_helper import Choice


class resturant(models.Model):
    name = models.CharField(max_length=128)
    city_name = models.CharField(max_length=128)
    adress = models.CharField(max_length=128)
    descriptions = models.TextField()
    




    
    
    def __str__(self) -> str:
        return self.name
