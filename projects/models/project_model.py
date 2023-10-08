from django.db import models
from projects.models.profile_model import Profile
from django.core.validators import MaxLengthValidator


class Project(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(
        null=False,
        blank=False,
        validators=[MaxLengthValidator(limit_value=500)],
    )
    github_url = models.URLField(null=False, blank=False)
    keyword = models.CharField(max_length=50, null=False, blank=False)
    key_skill = models.CharField(max_length=50, null=False, blank=False)
    profile = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name='projects'
    )
