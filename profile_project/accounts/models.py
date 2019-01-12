from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.


# INPROG: Create a Django model for the user profile.
class Account(AbstractUser):
    '''
Account is the main class for this project, and stores user information to be
displayed on their profile page. Does not handle authentication directly.
    '''
    # First Name, Last Name, Email, Password, is_active are inherited from
    # the Django User class
    # Date of Birth
    dob = models.DateField()
    # Bio
    '''The bio validation should check that the bio is 10 characters or longer
    and properly escapes HTML formatting.'''
    bio = models.TextField(
        max_length=16384,
    )
    # Avatar
    avatar = models.ImageField()
