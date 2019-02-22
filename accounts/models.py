from django.conf import settings
from django.db import models


class Profile(models.Model):
    '''
This is the model for a User's profile

USAGE:

profile = Profile.objects.get(account=user)
{{ profile.bio }}
--or--
# Use the logged in user from the request (like flask's current_user)
request.user.profile

rather than extend a user model, this is simply an extended class connected to
a user with a foreign key
    '''
    account = models.OneToOneField(
        # primary key for this model
        # is a foreign key connected to the default user model
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    # Avatar
    avatar = models.ImageField()
    '''
to recall the image in a template, use:
{{ settings.MEDIA_ROOT }}{{ user.profile.avatar.url }}
    '''
    # First Name
    first_name = models.CharField(max_length=60)
    # Last Name
    last_name = models.CharField(max_length=60)
    # Email
    email = models.CharField(max_length=256)
    # Date of Birth
    dob = models.DateField(null=True)
    # Bio
    bio = models.TextField(default="Enter your Bio here!")

    # Specialty (ex. python, javascript)
    specialty = models.CharField(default="", max_length=32)
    # github id (will be used to automatically generate links)
    github = models.CharField(default="", max_length=39)
    # linkedin id (will be used to automatically generate links)
    # no ' ', '-', or special chars
    linkedin = models.CharField(default="", max_length=100)

    def create_or_recall(user):
        '''
this method returns an existing profile, or creates and returns new profile
        '''
        try:
            profile = Profile.objects.get(account=user)
        except Profile.DoesNotExist:
            profile = Profile(account=user).save()
        return profile

    def __iter__(self):
        '''
This handy function is called when you use:

for key, value in profile:
    print("{}: {},".format(key, value))
        '''
        for i, field_name in enumerate(self._meta.get_fields()):
            if i < 2:
                # skip the account and avatar attributes
                pass
            else:
                value = getattr(self, str(field_name).split('.')[2])
                yield (str(field_name).split('.')[2], value)
