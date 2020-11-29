from django.db import models

# Create your models here.
class student(models.Model):
    idnum = models.CharField(max_length=13)
    name = models.CharField(max_length=25)
    branch = models.CharField(max_length=5)
    gender = models.CharField(max_length=6)
    dob = models.DateField()
    age = models.IntegerField()
