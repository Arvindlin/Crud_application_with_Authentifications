from django.db import models


# Create your models here.

class Information(models.Model):
    firstname = models.CharField(max_length=20, default=' ')
    lastname = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.IntegerField()

    def __str__(self):
        return self.firstname
