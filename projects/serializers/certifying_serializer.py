from rest_framework import serializers

from projects.models.certifying_model import CertifyingInstitution
from projects.models.certificate_model import Certificate
from .certificate_serializer import CertificateSerializer


class NestedCertificatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Certificate
        fields = ["id", "name", "timestamp"]


class CertifyingInstitutionSerializer(serializers.ModelSerializer):
    certificates = NestedCertificatesSerializer(many=True)

    class Meta:
        model = CertifyingInstitution
        fields = ["id", "name", "url", "certificates"]

    def create(self, validated_data):
        certificates_data = validated_data.pop("certificates")
        new_certifying_institution = CertifyingInstitution.objects.create(
            **validated_data
        )
        new_certificate = {}
        for certificate in certificates_data:
            new_certificate = {
                "name": certificate["name"],
                "certifying_institution": new_certifying_institution,
                "profiles": [],
            }
            CertificateSerializer().create(new_certificate)
        return new_certifying_institution
