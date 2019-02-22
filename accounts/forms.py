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
        if self.instance.email == "":
            # if the email hasn't been set yet, pass
            print("if the email hasn't been set yet")
        elif not email == self.instance.email:
            raise ValidationError("please verify your email address on file")
        return email

    def __init__(self, *args, **kwargs):
        if self.instance:
            if self.instance.email == "":
                print("No instance e    mail")
                self.email = forms.EmailField(
                    error_messages={
                        'required': (
                            '''Please enter a new email address''')},
                )
            else:
                print("instance email: {}".format(instance.email))
                self.email = forms.EmailField(
                    error_messages={
                        'required': (
                            '''Please verify your email address to make changes''')},
                )
        super().__init__(*args, **kwargs)

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
