from django import forms

from . import models


class AccountForm(forms.ModelForm):
    class Meta:
        model = models.Account
        fields = [
            'first_name',
            'last_name',
            'email',
            'password',
            'dob',
            'bio',
            'avatar',
        ]
