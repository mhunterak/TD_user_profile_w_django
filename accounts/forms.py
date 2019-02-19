from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from . import models


class ImageForm(forms.ModelForm):
    '''This form is for updating a user's avatar'''
    class Meta:
        model = models.Profile
        fields = ['avatar']


class ProfileForm(forms.ModelForm):
    '''This form is the main form for editing a user's profile'''
    bio = forms.CharField(
        min_length=10,
        widget=forms.Textarea(
            attrs={'placeholder': "Tell your story"}))
    dob = forms.DateField(
        widget=forms.DateInput(
            attrs={
                'placeholder': "use format MM/DD/YYYY",
            }
        )
    )
    email = forms.EmailField(
        validators=[],
        error_messages={
            'required': (
                'Please verify your email address to make changes')},
    )
    specialty = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': "What's your weapon of choice?"}))
    github = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': "Just user your @username"}))
    linkedin = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': "Enter linkedin.com/in/[THIS_PART]"}))

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email == self.instance.email:
            raise ValidationError("please verify your email address")
        return email

    class Meta:
        model = models.Profile
        fields = [
            'email',
            'first_name',
            'last_name',
            'dob',
            'specialty',
            'github',
            'linkedin',
            'bio',
        ]
