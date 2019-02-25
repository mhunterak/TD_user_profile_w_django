'''
ACCOUNT VIEWS

views for auth routes, and updating account profiles
'''
# Native libraries
import os
# 3rd party imports
from django.contrib import messages
from django.contrib.auth import (
    authenticate, login, logout, update_session_auth_hash)
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import (
    AuthenticationForm, UserCreationForm, PasswordChangeForm)
from django.contrib.auth.models import User
from django.urls import reverse

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from PIL import Image
# Custom modules
from .models import Profile
from .forms import ProfileForm, ImageForm, EmailForm


def user_has_email(request):
    '''This function looks to see if a user has submitted their email yet'''
    try:
        # if they have a profile, but their email is None or blank
        if (
                request.user.profile.email is None) or (
                request.user.profile.email == ''):
            messages.error(
                request,
                "Before we get do that, we need your email:")
            return False
    # if the user doesn't have a profile yet
    except User.profile.RelatedObjectDoesNotExist:
        messages.error(
            request,
            "To get started, we need your email:")
        return False
    return True

# PROFILE #


# Profile Crud - recall
@login_required
def profile(request, pk):
    '''Shows any user's profile'''
    if not user_has_email(request):
        # if a user hasn't sent in their email yet, they can't see profiles
        return HttpResponseRedirect(reverse('accounts:provide_email'))
    # a profile is recalled by the connected user's username
    user = get_object_or_404(User, username=pk)
    return render(
        request,
        'accounts/profile.html',
        {'profile': user.profile}
    )


@login_required
def bio(request, pk):
    '''Shows any user's profile'''
    if not user_has_email(request):
        # if a user hasn't sent in their email yet, they can't see profiles
        return HttpResponseRedirect(reverse('accounts:provide_email'))
    user = get_object_or_404(User, username=pk)
    return render(
        request,
        'accounts/bio.html',
        {'profile': user.profile}
    )

# Profile - add your email first
@login_required
def provide_email(request):
    '''After registering, a user must first provide their email.'''
    form = EmailForm()
    if request.method == 'POST':
        form = EmailForm(
            data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.account = request.user
            profile.save()
            print('Profile Saved')
            messages.success(request, 'profile updated!')
            return HttpResponseRedirect(
                reverse('accounts:edit_profile'))
    return render(
        request,
        'accounts/default_w_form.html',
        {'form': form}
    )


# Profile - create/update
@login_required
def edit_profile(request):
    '''Edits a user's own profile'''
    if not user_has_email(request):
        return HttpResponseRedirect(reverse('accounts:provide_email'))
    profile = request.user.profile
    if request.method == 'POST':
        form = ProfileForm(instance=profile, data=request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.account = request.user
            profile.save()
            print('Profile Saved')
            messages.success(request, 'profile updated!')
            return HttpResponseRedirect(
                reverse(
                    'accounts:profile',
                    kwargs={
                        'pk': request.user.username, }))
    form = ProfileForm(instance=profile)
    return render(
        request,
        'accounts/edit_profile.html',
        {'form': form}
    )


# AVATAR


@login_required
def avatar_upload(request):
    '''Adds the ability to upload and save a user’s avatar image'''
    if not user_has_email(request):
        return HttpResponseRedirect(reverse('accounts:provide_email'))
    form = ImageForm()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            profile = Profile.objects.get(pk=request.user)
            profile.avatar = request.FILES['avatar']
            profile.save()
            messages.success(request, 'Avatar Uploaded')
            return HttpResponseRedirect(reverse('accounts:avatar_upload'))
    return render(request, 'accounts/update_avatar.html', {
        'H1': 'Update Avatar',
        'form': form, })


@login_required
def avatar_manipulate(request, pk):
    '''This function handles all image manipulation with PIL'''

    if pk not in ['left', 'right', 'vert', 'horz']:
        # these are acceptable parameters, anything else gets rejected.
        raise ValueError("I'm afraid I can't let you do that, Dave.")
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # get the file path for the current user's profile
    filepath = BASE_DIR + request.user.profile.avatar.url
    # open the image in PIL
    image = Image.open(filepath)
    # perform the image manipulation
    if pk == "left":
        image = image.rotate(90, expand=True)
    if pk == "right":
        image = image.rotate(270, expand=True)
    if pk == "vert":
        image = image.transpose(Image.FLIP_TOP_BOTTOM)
    if pk == "horz":
        image = image.transpose(Image.FLIP_LEFT_RIGHT)
    # save the image back to the same filepath
    image.save(filepath)
    image.close()
    return HttpResponseRedirect(reverse('accounts:avatar_upload'))


"""
@login_required
def avatar_crop(request):
    '''This function handles adding in a crop feature for the avatar'''
    return render(request, 'accounts/crop_avatar.html')
"""


# AUTH ROUTES #


def sign_up(request):
    '''Creates a new user account, and sign in to the new account'''
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            # user =
            form.save()
            # the user account (not the profile) has been created
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'])
            login(request, user)
            messages.success(
                request,
                "You're now a user! You've been signed in, too.")
            messages.success(
                request,
                "Why not get started by providing your email?")
            # redirect to the email page. This could also be a modal?
            return HttpResponseRedirect(reverse('accounts:provide_email'))
    return render(request, 'accounts/sign_up.html', {'form': form})


def sign_in(request):
    '''Signs in a user with an authenticated password'''
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            if form.user_cache is not None:
                user = form.user_cache
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(
                        reverse('accounts:profile',
                                kwargs={'pk': user.username}))
                else:
                    messages.error(
                        request,
                        "That user account has been disabled.")
            else:
                messages.error(
                    request,
                    "Username or password is incorrect.")
    return render(request, 'accounts/sign_in.html', {'form': form})


@login_required
def sign_out(request):
    '''Signs out a user'''
    logout(request)
    messages.success(request, "You've been signed out. Come back soon!")
    return HttpResponseRedirect(reverse('home'))


def change_password(request):
    '''This route allows a user to reset their password'''
    form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        # if the user provided the corrent current password
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was updated!')
    return render(request, 'accounts/default_w_form.html', {
        'H1': 'Change Password',
        'form': form})
