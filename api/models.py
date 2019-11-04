from django.db import models

# We can extent existing user model
from django.contrib.auth.models import AbstractUser
#
#
# class User(AbstractUser):
#     location = models.CharField(max_length=30, blank=True)
#     birth_date = models.DateField(null=True, blank=True)


# class TeamMember(models.Model):
#     first_name = models.CharField(max_length=50, blank=False)
