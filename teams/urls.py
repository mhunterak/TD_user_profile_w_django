from django.urls import path

from . import views


urlpatterns = [
    path(r"add_skill", views.add_skill, name="add_skill"),
    path(r"add_project", views.add_project, name="add_project"),
    path(r"project/<int:pk>", views.project, name="project"),
    path(r"project/<int:pk>/add_position", views.add_position, name="add_position"),
    path(r"project/<int:pk>/view_position", views.view_position, name="view_position"),
    path(
        r"project/<int:pk>/approve/<int:applicant_pk>",
        views.approve_for_position,
        name="approve_for_position",
    ),
    path(
        r"project/<int:pk>/reject/<int:applicant_pk>",
        views.reject_for_position,
        name="reject_for_position",
    ),
    path(r"my_projects", views.my_projects, name="my_projects"),
    path(
        r"project/<int:pk>/apply", views.apply_for_position, name="apply_for_position"
    ),
    path(r"project/<int:pk>/applications", views.applications, name="applications"),
    path(
        r"project/<int:pk>/add_skill_position",
        views.add_skill_position,
        name="add_skill_position",
    ),
    path(r"project/position_search", views.position_search, name="position_search"),
    path(r"project/project_search", views.project_search, name="project_search"),
]
