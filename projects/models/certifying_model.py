from django.db import models
from django.core.validators import MaxLengthValidator


class CertifyingInstitution(models.Model):
    name = models.CharField(
        max_length=100,
        null=False,
        blank=False,
        validators=[MaxLengthValidator(limit_value=500)],
    )
    url = models.URLField(
        null=False,
        blank=False,
        validators=[MaxLengthValidator(limit_value=500)],
    )

    def __str__(self) -> str:
        return self.name
