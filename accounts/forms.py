from django import forms

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
    email = forms.EmailField()
    specialty = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': "What's your weapon of choice?"}))
    github = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': "Just user your @username"}))
    linkedin = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder': "Enter linkedin.com/in/[THIS_PART]"}))

    class Meta:
        model = models.Profile
        fields = [
            'first_name',
            'last_name',
            'email',
            'dob',
            'specialty',
            'github',
            'linkedin',
            'bio',
        ]
