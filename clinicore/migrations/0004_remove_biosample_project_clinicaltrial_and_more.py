# Generated by Django 5.2 on 2024-09-04 15:02

import django.db.models.deletion
import lnschema_core.ids
import lnschema_core.models
import lnschema_core.users
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("clinicore", "0003_alter_project_uid"),
        (
            "lnschema_core",
            "0064_alter_artifact_version_alter_collection_version_and_more",
        ),
    ]

    operations = [
        migrations.RemoveField(
            model_name="biosample",
            name="project",
        ),
        migrations.CreateModel(
            name="ClinicalTrial",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("updated_at", models.DateTimeField(auto_now=True, db_index=True)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "uid",
                    models.CharField(
                        default=lnschema_core.ids.base62_8, max_length=8, unique=True
                    ),
                ),
                ("name", models.CharField(db_index=True, default=None, max_length=255)),
                ("title", models.TextField(default=None, null=True)),
                ("objective", models.TextField(default=None, null=True)),
                ("description", models.TextField(default=None, null=True)),
                (
                    "_previous_runs",
                    models.ManyToManyField(related_name="+", to="lnschema_core.run"),
                ),
                (
                    "artifacts",
                    models.ManyToManyField(
                        related_name="clinical_trials", to="lnschema_core.artifact"
                    ),
                ),
                (
                    "collections",
                    models.ManyToManyField(
                        related_name="clinical_trials", to="lnschema_core.collection"
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        default=lnschema_core.users.current_user_id,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="lnschema_core.user",
                    ),
                ),
                (
                    "run",
                    models.ForeignKey(
                        default=lnschema_core.models.current_run,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        to="lnschema_core.run",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(lnschema_core.models.CanCurate, models.Model),
        ),
        migrations.AddField(
            model_name="biosample",
            name="clinical_trial",
            field=models.ForeignKey(
                default=None,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="biosamples",
                to="clinicore.clinicaltrial",
            ),
        ),
        migrations.DeleteModel(
            name="Project",
        ),
    ]
