from django.db import models
from django.contrib.auth.models import User


class Subscriber (models.Model):
    email = models.EmailField(unique=True)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.email

class Style (models.Model):
    name = models.CharField(max_length=150)
    def __str__(self):
        return self.name

class Inscription (models.Model):
    name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    birth_date = models.DateField()
    sexe = models.CharField(max_length=1)
    town_residence = models.CharField(max_length=150)
    number = models.PositiveIntegerField()
    style  = models.ForeignKey(Style, on_delete=models.CASCADE, related_name='styles')
