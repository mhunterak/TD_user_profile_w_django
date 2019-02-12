from django.conf import settings
from django.db import models


# Create your models here.
class Profile(models.Model):
    account = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    # First Name,
    first_name = models.CharField(
        max_length=60,
    )
    # Last Name,
    last_name = models.CharField(
        max_length=60,
    )
    # Email,
    email = models.CharField(
        max_length=256,
    )   
    # Date of Birth,
    dob = models.DateField()
    # Bio and
    bio = models.TextField()
    # Avatar
    avatar = models.ImageField()

    def __iter__(self):
        for i, field_name in enumerate(self._meta.get_fields()):
            if i == 0:
                pass
            else:
                value = getattr(self, str(field_name).split('.')[2])
                yield (str(field_name).split('.')[2], value)

