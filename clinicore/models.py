from bionty import ids as bionty_ids
from bionty.models import BioRecord, CellType, Disease, Ethnicity, Tissue
from django.db import models
from django.db.models import PROTECT
from lnschema_core import ids
from lnschema_core.models import (
    Artifact,
    CanValidate,
    Collection,
    Record,
    TracksRun,
    TracksUpdates,
)


class Project(Record, CanValidate, TracksRun, TracksUpdates):
    """Models a clinicorel project of :class:`clinicore.Project`.

    Example:
        >>> project = Project(
        ...     name="Clinical trial of drug X in patients with disease Y",
        ...     description="A clinicorel trial to evaluate the efficacy of drug X in patients with disease Y.",
        ... ).save()
    """

    class Meta(Record.Meta, TracksRun.Meta, TracksUpdates.Meta):
        abstract = False

    id = models.AutoField(primary_key=True)
    """Internal id, valid only in one DB instance."""
    uid = models.CharField(unique=True, max_length=8, default=ids.base62_8)
    """Universal id, valid across DB instances."""
    name = models.CharField(max_length=255, default=None, db_index=True)
    """Name of the project."""
    description = models.TextField(null=True, default=None)
    """Description of the project."""
    artifacts = models.ManyToManyField(Artifact, related_name="projects")
    """Artifacts linked to the project."""
    collections = models.ManyToManyField(Collection, related_name="projects")
    """Collections linked to the project."""


class Biosample(Record, CanValidate, TracksRun, TracksUpdates):
    """Models a specimen derived from an patient, such as tissue, blood, or cells.

    Examples:
        >>> biosample = Biosample(
        ...     name="control",
        ...     batch="ctrl_1"
        ... ).save()
    """

    id = models.AutoField(primary_key=True)
    """Internal id, valid only in one DB instance."""
    uid = models.CharField(unique=True, max_length=12, default=ids.base62_12)
    """Universal id, valid across DB instances."""
    name = models.CharField(max_length=255, default=None, db_index=True, null=True)
    """Name of the biosample."""
    batch = models.CharField(max_length=60, default=None, null=True, db_index=True)
    """Batch label of the biosample."""
    description = models.TextField(null=True, default=None)
    """Description of the biosample."""
    tissues = models.ManyToManyField(Tissue, related_name="biosamples")
    """Tissues linked to the biosample."""
    cell_types = models.ManyToManyField(CellType, related_name="biosamples")
    """Cell types linked to the biosample."""
    diseases = models.ManyToManyField(Disease, related_name="biosamples")
    """Diseases linked to the biosample."""
    artifacts = models.ManyToManyField(Artifact, related_name="biosamples")
    """Artifacts linked to the biosample."""


class Patient(Record, CanValidate, TracksRun, TracksUpdates):
    """Models a patient in a clinicorel study.

    Examples:
        >>> patient = Patient(
        ...     name="Patient 1",
        ...     age=45,
        ...     gender="female"
        ... ).save()
    """

    GENDER_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
        ("unknown", "Unknown"),
    ]

    id = models.AutoField(primary_key=True)
    """Internal id, valid only in one DB instance."""
    uid = models.CharField(unique=True, max_length=12, default=ids.base62_12)
    """Universal id, valid across DB instances."""
    name = models.CharField(max_length=255, default=None, db_index=True)
    """Name of the patient."""
    age = models.IntegerField(null=True, default=None, db_index=True)
    """Age of the patient."""
    gender = models.CharField(
        max_length=10, choices=GENDER_CHOICES, null=True, default=None, db_index=True
    )
    """Gender of the patient."""
    ethnicity = models.ForeignKey(Ethnicity, PROTECT, null=True, default=None)
    """Ethnicity of the patient."""
    birth_date = models.DateField(db_index=True, null=True, default=None)
    """Birth date of the patient."""
    deceased = models.BooleanField(db_index=True, null=True, default=None)
    """Whether the patient is deceased."""
    deceased_date = models.DateField(db_index=True, null=True, default=None)
    """Date of death of the patient."""


class Medication(BioRecord):
    """Models a medication."""

    id = models.AutoField(primary_key=True)
    """Internal id, valid only in one DB instance."""
    uid = models.CharField(unique=True, max_length=12, default=bionty_ids.ontology)
    """Universal id, valid across DB instances."""
    ontology_id = models.CharField(
        max_length=32, db_index=True, null=True, default=None
    )
    """Ontology id of the medication."""
    name = models.CharField(max_length=255, db_index=True, null=True, default=None)
    """Name of the medication."""


class Treatment(Record, CanValidate, TracksRun, TracksUpdates):
    """Models compound treatments such as drugs.

    Examples:
        >>> aspirin_treatment = compound_treatment = Treatment(
        ...    name="Aspirin 325 MG Enteric Coated Tablet",
        ... ).save()
    """

    STATUS_CHOICES = [
        ("in-progress", "In Progress"),
        ("completed", "Completed"),
        ("entered-in-error", "Entered in Error"),
        ("stopped", "Stopped"),
        ("on-hold", "On Hold"),
        ("unknown", "Unknown"),
        ("not-done", "Not Done"),
    ]

    id = models.AutoField(primary_key=True)
    """Internal id, valid only in one DB instance."""
    uid = models.CharField(unique=True, max_length=12, default=ids.base62_12)
    """Universal id, valid across DB instances."""
    name = models.CharField(max_length=255, default=None, db_index=True)
    """Name of the treatment."""
    status = models.CharField(
        max_length=16, choices=STATUS_CHOICES, null=True, default=None
    )
    """Status of the treatment."""
    medication = models.ForeignKey(Medication, PROTECT, null=True, default=None)
    """Medications linked to the treatment."""
    dosage = models.FloatField(null=True, default=None)
    """Dosage of the treatment."""
    dosage_unit = models.CharField(max_length=32, null=True, default=None)
    """Unit of the dosage."""
    administered_datetime = models.DateTimeField(null=True, default=None)
    """Date and time the treatment was administered."""
    duration = models.DurationField(null=True, default=None)
    """Duration of the treatment."""
    route = models.CharField(max_length=32, null=True, default=None)
    """Route of administration of the treatment."""
    site = models.CharField(max_length=32, null=True, default=None)
    """Body site of administration of the treatment."""
    artifacts = models.ManyToManyField(Artifact, related_name="treatments")
    """Artifacts linked to the treatment."""