# Generated by Django 4.2.3 on 2023-10-07 18:13

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0003_certifyinginstitution_certificate"),
    ]

    operations = [
        migrations.DeleteModel(
            name="Certificate",
        ),
        migrations.DeleteModel(
            name="CertifyingInstitution",
        ),
    ]
