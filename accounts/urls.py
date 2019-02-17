from django.urls import path

from . import views


urlpatterns = [
    path(r'sign_in', views.sign_in, name='sign_in'),
    path(r'sign_up', views.sign_up, name='sign_up'),
    path(r'sign_out', views.sign_out, name='sign_out'),
    path(r'edit', views.edit_profile, name='edit_profile'),
    path(r'user/<str:pk>', views.profile, name='profile'),
    path(r'bio/<str:pk>', views.bio, name='bio'),
    path(r'avatar/upload', views.avatar_upload, name='avatar_upload'),
    path(r'change_password', views.change_password, name='change_password')
]
