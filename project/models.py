from django.db import models

# Create your models here.

class person(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)
    age = models.IntegerField()
    contact = models.IntegerField()
    blood = models.CharField(max_length=5)
