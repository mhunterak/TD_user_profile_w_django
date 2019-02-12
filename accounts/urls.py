from django.urls import path

from . import views

urlpatterns = [
    path(r'sign_in/', views.sign_in, name='sign_in'),
    path(r'sign_up/', views.sign_up, name='sign_up'),
    path(r'sign_out/', views.sign_out, name='sign_out'),
    path(r'edit_profile/', views.edit_profile, name='edit_profile'),
    path(r'profile/<str:pk>/', views.profile, name='profile'),
]

