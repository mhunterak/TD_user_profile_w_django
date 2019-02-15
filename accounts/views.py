from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render


from .models import Profile
from .forms import ProfileForm

# PROFILE
@login_required
def profile(request, pk):
    user = User.objects.get(username=pk)
    profile = Profile.objects.get(account=user)
    return render(
        request,
        'accounts/profile.html',
        {
            'user': user,
            'profile': profile,
        }
    )

@login_required
def edit_profile(request):
    try:
        profile = Profile.objects.get(account=request.user)
        print('Profile recieved')
        messages.add_message(request, 5, 'Profile recieved')
    except Profile.DoesNotExist:
        profile = Profile(account=request.user)
        print('Profile created')
        messages.add_message(request, 5, 'Profile created')

    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(data=request.POST)
        if form.is_valid():
            profile = form.save(
                commit=False
            )
            profile.account = request.user
            profile.save()
            print('profile updated!')
            for field, val in profile:
                print("{} : {}".format(
                    field, val
                    )
                )
                return HttpResponseRedirect(
                    reverse('accounts:profile', kwargs={
                        'pk': request.user.username,
                        }
                    )
                )
    return render(
        request, 
        'accounts/edit_profile.html',
        {
            'form': form,
            'profile': profile,
            'fields': profile._meta.get_fields(),
        }
    )


# AUTH ROUTES
def sign_in(request):
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
                            'accounts:profile', kwargs={'pk': user.username}
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


def sign_up(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )
            login(request, user)
            messages.success(
                request,
                "You're now a user! You've been signed in, too."
            )
            return HttpResponseRedirect(reverse('home'))  # TODO: go to profile
    return render(request, 'accounts/sign_up.html', {'form': form})


@login_required
def sign_out(request):
    logout(request)
    messages.success(request, "You've been signed out. Come back soon!")
    return HttpResponseRedirect(reverse('home'))

@login_required
def avatar_upload(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            profile = Profile.objects.get(pk=request.user)
            profile.avatar = form.cleaned_data['image']
            profile.save()
            return HttpResponseRedirect(
                        reverse(
                            'accounts:profile', kwargs={'pk': user.username}
                        )
            )
