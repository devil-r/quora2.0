from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Account(models.Model):
    GENDER = (
        ('M', "Male"),
        ('F', "Female"),
    )

    @staticmethod
    def to_gender(key):
        for item in Profile.GENDER:
            if item[0] == key:
                return item[1]
        return "None"

    user = models.OneToOneField(User, on_delete=models.CASCADE)    
    username = models.CharField(blank=False, max_length=50)
    gender = models.CharField(blank=True, max_length=1, choices=GENDER)
    address = models.CharField(blank=True, max_length=50)
