from django.db import models


class Student(models.Model):
    name = models.CharField(max_length=225)
    address = models.CharField(max_length=225)


    def __str__(self):
        return f" {self.name}"

# Create your models here.
