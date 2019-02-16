from django.conf import settings
from django.db import models


# Create your models here.
class Profile(models.Model):
    account = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        primary_key=True,
    )
    # Avatar
    avatar = models.ImageField()

    # First Name,
    first_name = models.CharField(max_length=60)
    # Last Name,
    last_name = models.CharField(max_length=60)
    # Email,
    email = models.CharField(max_length=256)
    # Date of Birth,
    dob = models.DateField()
    # Bio and
    bio = models.TextField()

    def create_or_recall(request):
        try:
            profile = Profile.objects.get(account=request.user)
        except Profile.DoesNotExist:
            profile = Profile(account=request.user)
        return profile

    def __iter__(self):
        for i, field_name in enumerate(self._meta.get_fields()):
            if i < 2:
                # skip the account and avatar attributes
                pass
            else:
                value = getattr(self, str(field_name).split('.')[2])
                yield (str(field_name).split('.')[2], value)
