# from django.shortcuts import render
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAuthenticated

from projects.models.profile_model import Profile
from projects.models.project_model import Project
from projects.models.certifying_model import CertifyingInstitution
from projects.models.certificate_model import Certificate

from projects.serializers.profile_serializer import ProfileSerializer
from projects.serializers.project_serializer import ProjectSerializer
from projects.serializers.certifying_serializer import (
    CertifyingInstitutionSerializer,
)
from projects.serializers.certificate_serializer import CertificateSerializer


# Create your views here.
class ProfileView(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def retrieve(self, request, *args, **kwargs):
        if request.method == "GET":
            kwargs.get("pk")
            all_profile = self.get_object()

            return render(
                request,
                "profile_detail.html",
                {"profile": all_profile},
            )
        return super().retrieve(request, *args, **kwargs)


class ProjectView(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class CertifyingView(viewsets.ModelViewSet):
    queryset = CertifyingInstitution.objects.all()
    serializer_class = CertifyingInstitutionSerializer


class CertificateView(viewsets.ModelViewSet):
    queryset = Certificate.objects.all()
    serializer_class = CertificateSerializer
