from django.contrib import admin
from projects.models.profile_model import Profile
from projects.models.project_model import Project
from projects.models.certifying_model import CertifyingInstitution
from projects.models.certificate_model import Certificate

# Register your models here.

admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(CertifyingInstitution)
admin.site.register(Certificate)
