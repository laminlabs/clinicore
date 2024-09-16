# ruff: noqa
# Generated by Django 5.2 on 2024-09-16 19:26

import django.db.models.deletion
import lnschema_core.models
import lnschema_core.users
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("clinicore", "0005_alter_biosample_created_by_alter_biosample_run_and_more"),
        ("lnschema_core", "0066_alter_artifact__feature_values_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="ArtifactBiosample",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("label_ref_is_name", models.BooleanField(default=None, null=True)),
                ("feature_ref_is_name", models.BooleanField(default=None, null=True)),
                (
                    "artifact",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="links_biosample",
                        to="lnschema_core.artifact",
                    ),
                ),
                (
                    "biosample",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="links_artifact",
                        to="clinicore.biosample",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        default=lnschema_core.users.current_user_id,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="lnschema_core.user",
                    ),
                ),
                (
                    "feature",
                    models.ForeignKey(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="links_artifactbiosample",
                        to="lnschema_core.feature",
                    ),
                ),
                (
                    "run",
                    models.ForeignKey(
                        default=lnschema_core.models.current_run,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="lnschema_core.run",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(lnschema_core.models.LinkORM, models.Model),
        ),
        migrations.CreateModel(
            name="ArtifactClinicalTrial",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("label_ref_is_name", models.BooleanField(default=None, null=True)),
                ("feature_ref_is_name", models.BooleanField(default=None, null=True)),
                (
                    "artifact",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="links_clinical_trial",
                        to="lnschema_core.artifact",
                    ),
                ),
                (
                    "clinicaltrial",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="links_artifact",
                        to="clinicore.clinicaltrial",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        default=lnschema_core.users.current_user_id,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="lnschema_core.user",
                    ),
                ),
                (
                    "feature",
                    models.ForeignKey(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="links_artifactclinicaltrial",
                        to="lnschema_core.feature",
                    ),
                ),
                (
                    "run",
                    models.ForeignKey(
                        default=lnschema_core.models.current_run,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="lnschema_core.run",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(lnschema_core.models.LinkORM, models.Model),
        ),
        migrations.CreateModel(
            name="ArtifactMedication",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("label_ref_is_name", models.BooleanField(default=None, null=True)),
                ("feature_ref_is_name", models.BooleanField(default=None, null=True)),
                (
                    "artifact",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="links_medication",
                        to="lnschema_core.artifact",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        default=lnschema_core.users.current_user_id,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="lnschema_core.user",
                    ),
                ),
                (
                    "feature",
                    models.ForeignKey(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="links_artifactmedication",
                        to="lnschema_core.feature",
                    ),
                ),
                (
                    "medication",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="links_artifact",
                        to="clinicore.medication",
                    ),
                ),
                (
                    "run",
                    models.ForeignKey(
                        default=lnschema_core.models.current_run,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="lnschema_core.run",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(lnschema_core.models.LinkORM, models.Model),
        ),
        migrations.CreateModel(
            name="ArtifactPatient",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("label_ref_is_name", models.BooleanField(default=None, null=True)),
                ("feature_ref_is_name", models.BooleanField(default=None, null=True)),
                (
                    "artifact",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="links_patient",
                        to="lnschema_core.artifact",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        default=lnschema_core.users.current_user_id,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="lnschema_core.user",
                    ),
                ),
                (
                    "feature",
                    models.ForeignKey(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="links_artifactpatient",
                        to="lnschema_core.feature",
                    ),
                ),
                (
                    "patient",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="links_artifact",
                        to="clinicore.patient",
                    ),
                ),
                (
                    "run",
                    models.ForeignKey(
                        default=lnschema_core.models.current_run,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="lnschema_core.run",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(lnschema_core.models.LinkORM, models.Model),
        ),
        migrations.CreateModel(
            name="ArtifactTreatment",
            fields=[
                ("created_at", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("id", models.BigAutoField(primary_key=True, serialize=False)),
                ("label_ref_is_name", models.BooleanField(default=None, null=True)),
                ("feature_ref_is_name", models.BooleanField(default=None, null=True)),
                (
                    "artifact",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="links_treatment",
                        to="lnschema_core.artifact",
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        default=lnschema_core.users.current_user_id,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="lnschema_core.user",
                    ),
                ),
                (
                    "feature",
                    models.ForeignKey(
                        default=None,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="links_artifacttreatment",
                        to="lnschema_core.feature",
                    ),
                ),
                (
                    "run",
                    models.ForeignKey(
                        default=lnschema_core.models.current_run,
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="+",
                        to="lnschema_core.run",
                    ),
                ),
                (
                    "treatment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="links_artifact",
                        to="clinicore.treatment",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
            bases=(lnschema_core.models.LinkORM, models.Model),
        ),
        migrations.RunSQL(
            f"""
            INSERT INTO clinicore_artifactbiosample (artifact_id, biosample_id, feature_id, created_by_id, created_at)
            SELECT artifact_id, biosample_id, NULL, {1}, CURRENT_TIMESTAMP
            FROM clinicore_biosample_artifacts;
            """
        ),
        migrations.RunSQL(
            f"""
            INSERT INTO clinicore_artifactclinicaltrial (artifact_id, clinicaltrial_id, feature_id, created_by_id, created_at)
            SELECT artifact_id, clinicaltrial_id, NULL, {1}, CURRENT_TIMESTAMP
            FROM clinicore_clinicaltrial_artifacts;
            """
        ),
        migrations.RunSQL(
            f"""
            INSERT INTO clinicore_artifactmedication (artifact_id, medication_id, feature_id, created_by_id, created_at)
            SELECT artifact_id, medication_id, NULL, {1}, CURRENT_TIMESTAMP
            FROM clinicore_medication_artifacts;
            """
        ),
        migrations.RunSQL(
            f"""
            INSERT INTO clinicore_artifactpatient(artifact_id, patient_id, feature_id, created_by_id, created_at)
            SELECT artifact_id, patient_id, NULL, {1}, CURRENT_TIMESTAMP
            FROM clinicore_patient_artifacts;
            """
        ),
        migrations.RunSQL(
            f"""
            INSERT INTO clinicore_artifacttreatment(artifact_id, treatment_id, feature_id, created_by_id, created_at)
            SELECT artifact_id, treatment_id, NULL, {1}, CURRENT_TIMESTAMP
            FROM clinicore_treatment_artifacts;
            """
        ),
        migrations.RemoveField(
            model_name="biosample",
            name="artifacts",
        ),
        migrations.AddField(
            model_name="biosample",
            name="artifacts",
            field=models.ManyToManyField(
                related_name="biosamples",
                through="clinicore.ArtifactBiosample",
                to="lnschema_core.artifact",
            ),
        ),
        migrations.RemoveField(
            model_name="clinicaltrial",
            name="artifacts",
        ),
        migrations.AddField(
            model_name="clinicaltrial",
            name="artifacts",
            field=models.ManyToManyField(
                related_name="clinical_trials",
                through="clinicore.ArtifactClinicalTrial",
                to="lnschema_core.artifact",
            ),
        ),
        migrations.RemoveField(
            model_name="medication",
            name="artifacts",
        ),
        migrations.AddField(
            model_name="medication",
            name="artifacts",
            field=models.ManyToManyField(
                related_name="medications",
                through="clinicore.ArtifactMedication",
                to="lnschema_core.artifact",
            ),
        ),
        migrations.RemoveField(
            model_name="patient",
            name="artifacts",
        ),
        migrations.AddField(
            model_name="patient",
            name="artifacts",
            field=models.ManyToManyField(
                related_name="patients",
                through="clinicore.ArtifactPatient",
                to="lnschema_core.artifact",
            ),
        ),
        migrations.RemoveField(
            model_name="treatment",
            name="artifacts",
        ),
        migrations.AddField(
            model_name="treatment",
            name="artifacts",
            field=models.ManyToManyField(
                related_name="treatments",
                through="clinicore.ArtifactTreatment",
                to="lnschema_core.artifact",
            ),
        ),
    ]