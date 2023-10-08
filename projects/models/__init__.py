from django.db import models  # noqa F401

try:
    from projects.models.profile_model import Profile  # noqa F401
    from projects.models.project_model import Project  # noqa F401
except ModuleNotFoundError:
    pass
