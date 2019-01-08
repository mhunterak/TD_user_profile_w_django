from django.db import models

# Create your models here.


# INPROG: Create a Django model for the user profile.
class Account(models.Model):
    '''
Account is the main class for this project, and stores user information to be
displayed on their profile page. Does not handle authentication directly.
    '''
    # First Name
    firstname = models.CharField(
        max_length=64,
    )
    # Last Name
    lastname = models.CharField(
        max_length=64,
    )
    # Email - also the primary key
    email = models.EmailField(
        unique=True,
    )
    # way to disable bad actors
    is_active = models.BooleanField(default=True)
    # Password
    password = models.CharField(
        max_length=256,
    )
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
