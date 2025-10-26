from django.db import models

class PersonalInfo(models.Model):
    fullname = models.CharField(max_length=225)
    age = models.CharField(max_length=3)

# Create your models here.
