# from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from projects.views import ProfileView, ProjectView


router = routers.DefaultRouter()
router.register(r"profiles", ProfileView)
router.register(r"profiles/<int:id>", ProfileView)
router.register(r"projects", ProjectView)
router.register(r"projects/<int:id>", ProjectView)

urlpatterns = [
    path("", include(router.urls)),
    # path("admin/", admin.site.urls),
]
