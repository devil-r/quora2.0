from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class User_info(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    description = models.CharField(blank = True, max_length=50)
    education = models.CharField(blank = True, max_length=50)
