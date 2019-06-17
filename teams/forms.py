from django import forms
from django.core.exceptions import ValidationError

from . import models


class SkillForm(forms.ModelForm):
    """This form is for adding the email field to the profile separately."""

    title = forms.TextInput()

    class Meta:
        model = models.Skill
        fields = ["title"]


class ProjectForm(forms.ModelForm):
    """This form is for adding the email field to the profile separately."""

    title = forms.TextInput()
    description = forms.TextInput()

    class Meta:
        model = models.Project
        fields = ["title", "description"]


class PositionForm(forms.ModelForm):
    """"""

    title = forms.TextInput()
    description = forms.TextInput()

    class Meta:
        model = models.Position
        fields = ["title", "description"]


class SearchForm(forms.Form):
    search = forms.CharField(
        label="Search",
        widget=forms.TextInput(attrs={"placeholder": "Search", "style": "width: 80%;"}),
    )

