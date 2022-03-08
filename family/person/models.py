from django.db import models

# Create your models here.

class Person(models.Model):
    firstName = models.CharField(max_length=255)
    middleName = models.CharField(max_length=255, blank=True)
    lastName = models.CharField(max_length=255)
    gender = models.CharField(max_length=16)

class PersonImage(models.Model):
    image = models.CharField(max_length=999)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)