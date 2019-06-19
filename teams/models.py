from django.db import models

from accounts.models import Profile


# TODO As a user of the site, I should be able to create a project that I need help on.
class Project(models.Model):
    """
    Model for a User Skill


    rather than extend a user model, this is simply an extended class connected to
    a profile with a foreign key
    """

    creator = models.ForeignKey(Profile, on_delete=models.CASCADE)

    # Title
    title = models.CharField(max_length=60, null=True)
    # Last Name
    description = models.CharField(max_length=256, null=True)


# TODO As a user of the site, I should be able to specify the positions my project needs help in with a name, a description, and related skill.
class Position(models.Model):
    """
    Model for a User Skill


    rather than extend a user model, this is simply an extended class connected to
    a profile with a foreign key
    """

    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="positions"
    )

    # Title
    title = models.CharField(max_length=60, null=True)
    # Last Name
    description = models.CharField(max_length=256, null=True)
    # person in the position
    incumbent = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="role", null=True, default=None
    )
    # TODO As a user of the site, I should be able to see all of the applicants for my project's positions.
    applicants = models.ManyToManyField(Profile, related_name="applicants")
    rejects = models.ManyToManyField(Profile, related_name="rejects")

    def apply_for_position(self, profile):
        self.applicants.add(profile)

    # TODO As a user of the site, I should be able to approve an applicant for a position in my project.
    def approve_for_position(self, profile):
        self.incumbent = profile
        self.applicants.add([profile])
        self.rejects.remove(profile)
        # TODO As a user of the site, I should get a notification if I've been rejected or approved for a position.
        profile.add_notification("You've been approved for a position!")
        self.save()

    # TODO As a user of the site, I should be able to reject an applicant for a position in my project.
    def reject_for_position(self, profile):
        self.applicants.remove(profile)
        self.rejects.add([profile])
        # TODO As a user of the site, I should get a notification if I've been rejected or approved for a position.
        profile.add_notification("You've been rejected for a position!")
        self.save()


# TODO As a user of the site, I should be able to pick my skills for my profile.
class Skill(models.Model):
    """
    Model for a User Skill


    rather than extend a user model, this is simply an extended class connected to
    a profile with a foreign key
    """

    account = models.ManyToManyField(Profile, related_name="skills")
    project = models.ManyToManyField(Position, related_name="desired_skills")

    # Title
    title = models.CharField(max_length=60, null=True)
