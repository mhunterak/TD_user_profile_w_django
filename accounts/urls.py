from django.urls import path
from django.contrib.auth.views import (
    PasswordChangeView,
    PasswordChangeDoneView,
)

from . import views

urlpatterns = [
    path(r'sign_in', views.sign_in, name='sign_in'),
    path(r'sign_up', views.sign_up, name='sign_up'),
    path(r'sign_out', views.sign_out, name='sign_out'),
    path(r'edit', views.edit_profile, name='edit_profile'),
    path(r'user/<str:pk>', views.profile, name='profile'),
    path(r'avatar/upload', views.avatar_upload, name='avatar_upload'),
    # TODO: make a custom version of this
    path(r'change_password', PasswordChangeView.as_view(
        success_url='accounts/change_password/done'),
        name="password_change"),
    path(r'change_password/done', PasswordChangeDoneView.as_view(),
         name="change_password_done"),
]
