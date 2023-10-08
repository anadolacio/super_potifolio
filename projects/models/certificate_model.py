from django.db import models
# from projects.models.profile_model import Profile
from projects.models.certifying_model import CertifyingInstitution


class Certificate(models.Model):
    name = models.CharField(max_length=100)
    certifying_institution = models.ForeignKey(
        CertifyingInstitution,
        on_delete=models.CASCADE,
        related_name="certificates",
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    profiles = models.ManyToManyField("Profile", related_name="certificates")

    def __str__(self):
        return self.name
