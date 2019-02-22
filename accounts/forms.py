from django import forms
from django.core.exceptions import ValidationError

from . import models


class ImageForm(forms.ModelForm):
    '''This form is for updating a user's avatar'''
    class Meta:
        model = models.Profile
        fields = ['avatar']


class EmailForm(forms.ModelForm):
    '''This form is for adding the email field to the profile separately.'''
    email = forms.EmailField()

    class Meta:
        model = models.Profile
        fields = ['email', ]


class ProfileForm(forms.ModelForm):
    '''This form is the main form for editing a user's profile'''
    bio = forms.CharField(
        min_length=10,
        widget=forms.Textarea(
            attrs={'placeholder': "Tell your story"}))
    dob = forms.DateField(
        widget=forms.TextInput(attrs={
            'class': 'datepicker'
        }))
    email = forms.EmailField(
        error_messages={
            'required': 'Please verify your email to make changes'})
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
        '''This is the method for validating that the user submitted their
        email when editing their profile.
        '''
        email = self.cleaned_data['email']
        if not email.lower() == self.instance.email.lower():
            raise ValidationError("please verify your email address on file")
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
        widgets = {'dob': forms.DateInput(attrs={'class': 'datepicker'}), }
