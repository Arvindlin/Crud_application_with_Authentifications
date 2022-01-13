from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

# def validate_phone(value):
#     if r'^\d{9,15}$' in value:
#         return value
#     else:
#         raise ValidationError("Phone numbers must be valid")


class Information(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=True)
    firstname = models.CharField(max_length=20, default=' ')
    lastname = models.CharField(max_length=20)
    email = models.EmailField()
    age = models.IntegerField()
    # phone_number = models.CharField(validators = [RegexValidator(regex=r'^\d{9,15}$')],max_length = 10)



    def __str__(self):
        return self.firstname


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
