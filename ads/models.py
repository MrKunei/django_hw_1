from django.db import models

class Ad(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    address = models.CharField(max_length=255)
    is_publish = models.BooleanField()



class Category(models.Model):
    name = models.CharField(max_length=255)

