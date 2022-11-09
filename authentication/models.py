from unicodedata import name
from django.db import models

# Create your models here.

class Movies(models.Model):
    name = models.CharField(max_length = 50)
    img = models.ImageField(upload_to = 'images')
    des = models.TextField()
    price = models.IntegerField()

    def __str__(self) :
        return self.name 
