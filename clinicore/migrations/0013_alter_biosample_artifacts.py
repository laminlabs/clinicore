# Generated by Django 5.1.4 on 2025-01-30 12:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("clinicore", "0012_lamindbv1_part6"),
        ("lamindb", "0085_squashed"),
    ]

    operations = [
        migrations.AlterField(
            model_name="biosample",
            name="artifacts",
            field=models.ManyToManyField(
                related_name="clinicore_biosamples",
                through="clinicore.ArtifactBiosample",
                to="lamindb.artifact",
            ),
        ),
    ]
