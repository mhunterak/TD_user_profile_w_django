from django.utils import timezone as tz
from django.conf import settings
from django.db import models


class Profile(models.Model):

    """
    Model for a User Profile


rather than extend a user model, this is simply an extended class connected to
a user with a foreign key
    """

    account = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, primary_key=True
    )
    avatar = models.ImageField()
    # First Name
    first_name = models.CharField(max_length=60, null=True)
    # Last Name
    last_name = models.CharField(max_length=60, null=True)
    # Email
    email = models.CharField(max_length=256)
    # Date of Birth
    dob = models.DateField(null=True)
    # Bio
    bio = models.TextField(null=True)
    # EXTRA CREDIT
    # Specialty (ex. python, javascript)
    specialty = models.CharField(default="", max_length=32, null=True)
    # github id - generates links automatically
    github = models.CharField(default="", max_length=39, null=True)
    # linkedin id - generates links automatically
    linkedin = models.CharField(default="", max_length=100, null=True)

    def add_notification(self, description):
        Notification.objects.create(profile=self, description=description)

    def get_notifications(self):
        return Notification.objects.all().filter(profile=self)

    def __iter__(self):
        """
This handy function returns the instance attributes when called as an iterator
ie:

for key, value in profile:
    print("{}: {},".format(key, value))
        """
        for i, field_name in enumerate(self._meta.get_fields()):
            if i < 2:
                # skip the account and avatar attributes
                pass
            else:
                value = getattr(self, str(field_name).split(".")[2])
                yield (str(field_name).split(".")[2], value)


class Notification(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    description = models.CharField(max_length=256)
    timestamp = models.DateTimeField(default=tz.now)
