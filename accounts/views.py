# Native libraries
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
# Custom modules
from .models import Profile
from .forms import ProfileForm, ImageForm


# PROFILE #


# Profile Crud - recall
def profile(request, pk):
    '''
Shows any user's profile
no login required
    '''
    user = get_object_or_404(User, username=pk)
    Profile.create_or_recall(user)
    return render(
        request,
        'accounts/profile.html',
        {'profile': user.profile}
    )


# Bio
def bio(request, pk):
    '''
Shows any user's profile
no login required
    '''
    user = get_object_or_404(User, username=pk)
    return render(
        request,
        'accounts/bio.html',
        {'profile': user.profile}
    )

# Profile - create/update
@login_required
def edit_profile(request):
    '''
Edits a user's own profile
login required
    '''
    try:
        profile = Profile.objects.get(account=request.user)
    except (Profile.DoesNotExist, UnboundLocalError):
        profile = None
    if request.method == 'POST':
        form = ProfileForm(
            data=request.POST,
            instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.account = request.user
            profile.save()
            print('Profile Saved')
            messages.success(request, 'profile updated!')
            return HttpResponseRedirect(
                reverse('accounts:profile', kwargs={
                    'pk': request.user.username,
                })
            )
    try:
        data = profile.__dict__
    except AttributeError:
        data = {}
    data['email'] = ''
    form = ProfileForm(instance=profile, data=data)
    return render(
        request,
        'accounts/edit_profile.html',
        {'form': form}
    )


@login_required
def avatar_upload(request):
    '''
Adds the ability to upload and save a user’s avatar image
    '''
    form = ImageForm()
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            profile = Profile.objects.get(pk=request.user)
            profile.avatar = request.FILES['avatar']
            profile.save()
        messages.success(request, 'Avatar Updated')
    return render(request, 'accounts/update_avatar.html', {
        'H1': 'Update Avatar',
        'form': form,
    }
    )


# AUTH ROUTES #


def sign_up(request):
    '''
Creates a new user account, and get sign in to the new account
    '''
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            # TODO: create user profile here, and then save email?
            login(request, user)
            messages.success(
                request,
                "You're now a user! You've been signed in, too."
            )
            messages.success(
                request,
                "Why not get started by editing your profile?"
            )
            return HttpResponseRedirect(reverse('accounts:edit_profile'))
    return render(request, 'accounts/sign_up.html', {'form': form})


def sign_in(request):
    '''
Signs in a user with an authenticated password
    '''
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            if form.user_cache is not None:
                user = form.user_cache
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(
                        reverse(
                            'accounts:profile',
                            kwargs={'pk': user.username}
                        )
                    )
                else:
                    messages.error(
                        request,
                        "That user account has been disabled."
                    )
            else:
                messages.error(
                    request,
                    "Username or password is incorrect."
                )
    return render(request, 'accounts/sign_in.html', {'form': form})


@login_required
def sign_out(request):
    '''
Signs out a user
    '''
    logout(request)
    messages.success(request, "You've been signed out. Come back soon!")
    return HttpResponseRedirect(reverse('home'))


def change_password(request):
    '''
this route allows a user to reset their password
    '''
    form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was updated!')
    return render(request, 'accounts/default_w_form.html', {
        'H1': 'Change Password',
        'form': form})
