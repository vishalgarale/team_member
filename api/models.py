from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# We can extent existing user model to consider team member
from django.contrib.auth.models import AbstractUser
#
#
# class User(AbstractUser):
#     phone_number = PhoneNumberField()
#     role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=ROLE_REGULAR)


# Considering team member as separate entity from User model
class TeamMember(models.Model):
    ROLE_ADMIN = 1
    ROLE_REGULAR = 2
    ROLE_CHOICES = [
        (ROLE_ADMIN, 'admin'),
        (ROLE_REGULAR, 'regular')
    ]

    email = models.EmailField(unique=True, null=False, blank=False)
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    phone_number = PhoneNumberField()
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, default=ROLE_REGULAR)
