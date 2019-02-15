from django import forms

from . import models


class ProfileForm(forms.ModelForm):
    bio = forms.CharField(
        min_length=10,
        widget=forms.Textarea
    )
    email = forms.EmailField()

    class Meta:
        model = models.Profile
        fields = [
            'first_name',
            'last_name',
            'email',
            'dob',
            'bio',
        ]
