from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Information(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    firstname = models.CharField(max_length=20, default=' ')
    lastname = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.IntegerField()

    def __str__(self):
        return self.firstname
