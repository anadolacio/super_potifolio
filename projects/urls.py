# from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from projects.views import (
    ProfileView,
    ProjectView,
    CertifyingView,
    CertificateView,
)


router = routers.DefaultRouter()
router.register(r"profiles", ProfileView)
router.register(r"profiles/<int:id>", ProfileView)
router.register(r"projects", ProjectView)
router.register(r"projects/<int:id>", ProjectView)
router.register(r"certificates", CertificateView)
router.register(r"certificates/<int:id>", CertificateView)
router.register(r"certifying-institutions", CertifyingView)
router.register(r"certifying-institutions/<int:id>", CertifyingView)

urlpatterns = [
    path("", include(router.urls)),
    # path("admin/", admin.site.urls),
]
