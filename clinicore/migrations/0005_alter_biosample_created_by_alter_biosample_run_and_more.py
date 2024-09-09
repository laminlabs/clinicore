# Generated by Django 5.2 on 2024-09-09 13:14

import django.db.models.deletion
import lnschema_core.models
import lnschema_core.users
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("bionty", "0039_alter_cellline_source_alter_cellmarker_source_and_more"),
        ("clinicore", "0004_remove_biosample_project_clinicaltrial_and_more"),
        ("lnschema_core", "0066_alter_artifact__feature_values_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="biosample",
            name="created_by",
            field=models.ForeignKey(
                default=lnschema_core.users.current_user_id,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="lnschema_core.user",
            ),
        ),
        migrations.AlterField(
            model_name="biosample",
            name="run",
            field=models.ForeignKey(
                default=lnschema_core.models.current_run,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="lnschema_core.run",
            ),
        ),
        migrations.AlterField(
            model_name="clinicaltrial",
            name="created_by",
            field=models.ForeignKey(
                default=lnschema_core.users.current_user_id,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="lnschema_core.user",
            ),
        ),
        migrations.AlterField(
            model_name="clinicaltrial",
            name="run",
            field=models.ForeignKey(
                default=lnschema_core.models.current_run,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="lnschema_core.run",
            ),
        ),
        migrations.AlterField(
            model_name="medication",
            name="created_by",
            field=models.ForeignKey(
                default=lnschema_core.users.current_user_id,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="lnschema_core.user",
            ),
        ),
        migrations.AlterField(
            model_name="medication",
            name="run",
            field=models.ForeignKey(
                default=lnschema_core.models.current_run,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="lnschema_core.run",
            ),
        ),
        migrations.AlterField(
            model_name="medication",
            name="source",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="bionty.source",
            ),
        ),
        migrations.AlterField(
            model_name="patient",
            name="created_by",
            field=models.ForeignKey(
                default=lnschema_core.users.current_user_id,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="lnschema_core.user",
            ),
        ),
        migrations.AlterField(
            model_name="patient",
            name="run",
            field=models.ForeignKey(
                default=lnschema_core.models.current_run,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="lnschema_core.run",
            ),
        ),
        migrations.AlterField(
            model_name="treatment",
            name="created_by",
            field=models.ForeignKey(
                default=lnschema_core.users.current_user_id,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="lnschema_core.user",
            ),
        ),
        migrations.AlterField(
            model_name="treatment",
            name="run",
            field=models.ForeignKey(
                default=lnschema_core.models.current_run,
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="lnschema_core.run",
            ),
        ),
    ]