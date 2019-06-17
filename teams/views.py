from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse


from .models import Profile, Skill, Project, Position
from .forms import SkillForm, ProjectForm, PositionForm, SearchForm


# skill Crud - create
@login_required
def add_skill(request):
    """adds a skill to user's profile"""
    # a profile is recalled by the connected user's username
    form = SkillForm()
    if request.method == "POST":
        form = SkillForm(data=request.POST)
        if form.is_valid():
            skill = form.save()
            skill.account.set([request.user.profile])
            print("skill {} saved".format(skill.title))
            messages.success(request, "skill added to your Profile!")
            return HttpResponseRedirect(
                reverse("accounts:profile", kwargs={"pk": request.user.username})
            )
    return render(request, "default_w_form.html", {"form": form})


# skill Crud - create desired skill for project position
@login_required
def add_skill_position(request, pk):
    """adds a skill to a project position"""
    # a profile is recalled by the connected user's username
    form = SkillForm()
    if request.method == "POST":
        form = SkillForm(data=request.POST)
        if form.is_valid():
            position = Position.objects.get(pk=pk)
            skill = form.save()
            skill.project.set([position])
            print("skill {} saved".format(skill.title))
            messages.success(request, "skill saved!")
            return HttpResponseRedirect(
                reverse("teams:project", kwargs={"pk": position.project.id})
            )
    messages.success(request, "add a new skill to your project!")
    return render(request, "default_w_form.html", {"form": form})


# skills are shown on a users profile


@login_required
def add_project(request):
    """adds a skill to user's profile"""
    # a profile is recalled by the connected user's username
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(data=request.POST)
        if form.is_valid():
            project = form.save(commit=False)
            project.creator = request.user.profile
            project.save()
            print("project {} saved".format(project.title))
            messages.success(request, "project saved!")
            return HttpResponseRedirect(
                reverse("accounts:profile", kwargs={"pk": request.user.username})
            )
    return render(request, "default_w_form.html", {"form": form})


@login_required
def project(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, "project.html", {"project": project})


@login_required
def add_position(request, pk):
    """adds a position to a project"""
    # a profile is recalled by the connected user's username
    form = PositionForm()
    if request.method == "POST":
        form = PositionForm(data=request.POST)
        if form.is_valid():
            position = form.save(commit=False)
            position.project = Project.objects.get(pk=pk)
            position.incumbent = None
            position.save()
            print("position {} saved".format(position.title))
            messages.success(request, "position saved!")
            return HttpResponseRedirect(reverse("teams:project", kwargs={"pk": pk}))
    return render(
        request, "default_w_form.html", {"H1": "Add a newPosition", "form": form}
    )


@login_required
def view_position(request, pk):
    position = Position.objects.get(pk=pk)
    return render(request, "position.html", {"position": position})


@login_required
def apply_for_position(request, pk):
    position = Position.objects.get(pk=pk)
    position.apply_for_position(request.user.profile)
    messages.success(request, "You've applied, good luck!")
    return HttpResponseRedirect(
        reverse("teams:project", kwargs={"pk": position.project.id})
    )


@login_required
def approve_for_position(request, pk, applicant_pk):
    position = Position.objects.get(pk=pk)
    applicant = Profile.objects.get(pk=applicant_pk)
    position.approve_for_position(applicant)
    messages.success(request, "You've approved an applicant!")
    return HttpResponseRedirect(
        reverse("teams:project", kwargs={"pk": position.project.id})
    )


@login_required
def reject_for_position(request, pk, applicant_pk):
    position = Position.objects.get(pk=pk)
    applicant = Profile.objects.get(pk=applicant_pk)
    position.reject_for_position(applicant)
    messages.success(request, "You've rejected an applicant!")
    return HttpResponseRedirect(
        reverse("teams:applications", kwargs={"pk": position.project.id})
    )


@login_required
def my_projects(request):
    projects = Project.objects.all().filter(creator=request.user.profile)
    return render(request, "projects.html", {"H1": "My Projects", "projects": projects})


@login_required
def applications(request, pk):
    project = Project.objects.get(pk=pk)
    return render(request, "applications.html", {"project": project})


@login_required
def project_search(request):
    form = SearchForm()
    if request.method == "POST":
        form = SearchForm(request.POST)
        projects = Project.objects.all().filter(
            title__icontains=form.data['search']
        )
        return render(request, "search.html", {'form': form, "projects": projects, 'query': form.data['search'],})
    return render(request, "search.html", {'form': form})


@login_required
def position_search(request):
    form = SearchForm()
    if request.method == "POST":
        form = SearchForm(request.POST)
        positions = Position.objects.all().filter(
            title__icontains=form.data['search']
        )
        return render(request, "search.html", {'form': form, "positions": positions, 'query': form.data['search'],})
    return render(request, "search.html", {'form': form})
