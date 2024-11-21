from __future__ import annotations

from datetime import datetime  # noqa
from typing import overload

from bionty import ids as bionty_ids
from bionty.models import BioRecord, CellType, Disease, Ethnicity, Source, Tissue
from django.db import models
from django.db.models import CASCADE, PROTECT
from lnschema_core import ids
from lnschema_core.fields import (
    BooleanField,
    CharField,
    DateField,
    DateTimeField,
    DurationField,
    FloatField,
    ForeignKey,
    IntegerField,
    TextField,
)
from lnschema_core.models import (
    Artifact,
    CanCurate,
    Collection,
    Feature,
    LinkORM,
    Record,
    TracksRun,
    TracksUpdates,
)


class ClinicalTrial(Record, CanCurate, TracksRun, TracksUpdates):
    """Models a ClinicalTrials.

    Example:
        >>> trail = ClinicalTrial(
        ...     name="NCT00000000",
        ...     description="A clinicorel trial to evaluate the efficacy of drug X in patients with disease Y.",
        ... ).save()
    """

    class Meta(Record.Meta, TracksRun.Meta, TracksUpdates.Meta):
        abstract = False

    id: int = models.AutoField(primary_key=True)
    """Internal id, valid only in one DB instance."""
    uid: str = CharField(unique=True, max_length=8, default=ids.base62_8)
    """Universal id, valid across DB instances."""
    name: str | None = CharField(max_length=255, db_index=True)
    """ClinicalTrials.gov ID, the format is "NCT" followed by an 8-digit number."""
    title: str | None = TextField(null=True)
    """Official title of the clinical trial."""
    objective: str | None = TextField(null=True)
    """Objective of the clinical trial."""
    description: str | None = TextField(null=True)
    """Description of the clinical trial."""
    collections: Collection = models.ManyToManyField(
        Collection, related_name="clinical_trials"
    )
    """Collections linked to the clinical trial."""
    artifacts: Artifact = models.ManyToManyField(
        Artifact, through="ArtifactClinicalTrial", related_name="clinical_trials"
    )
    """Artifacts linked to the clinical trial."""


class ArtifactClinicalTrial(Record, LinkORM, TracksRun):
    id: int = models.BigAutoField(primary_key=True)
    artifact: Artifact = ForeignKey(
        Artifact, CASCADE, related_name="links_clinical_trial"
    )
    clinicaltrial: ClinicalTrial = ForeignKey(
        ClinicalTrial, PROTECT, related_name="links_artifact"
    )
    feature: Feature = ForeignKey(
        Feature,
        PROTECT,
        null=True,
        default=None,
        related_name="links_artifactclinicaltrial",
    )
    label_ref_is_name: bool | None = BooleanField(null=True, default=None)
    feature_ref_is_name: bool | None = BooleanField(null=True, default=None)


class Biosample(Record, CanCurate, TracksRun, TracksUpdates):
    """Models a specimen derived from an patient, such as tissue, blood, or cells.

    Examples:
        >>> biosample = Biosample(
        ...     name="control",
        ...     batch="ctrl_1"
        ... ).save()
    """

    id: int = models.AutoField(primary_key=True)
    """Internal id, valid only in one DB instance."""
    uid: str = CharField(unique=True, max_length=12, default=ids.base62_12)
    """Universal id, valid across DB instances."""
    name: str | None = CharField(db_index=True, null=True)
    """Name of the biosample."""
    batch: str | None = CharField(max_length=60, null=True, db_index=True)
    """Batch label of the biosample."""
    description: str | None = TextField(null=True)
    """Description of the biosample."""
    patient: Patient = ForeignKey(
        "Patient", PROTECT, related_name="biosamples", null=True, default=None
    )
    """Patient linked to the biosample."""
    clinical_trial: ClinicalTrial = ForeignKey(
        ClinicalTrial, PROTECT, related_name="biosamples", null=True, default=None
    )
    """Clinical trial linked to the biosample."""
    tissues: Tissue = models.ManyToManyField(Tissue, related_name="biosamples")
    """Tissues linked to the biosample."""
    cell_types: CellType = models.ManyToManyField(CellType, related_name="biosamples")
    """Cell types linked to the biosample."""
    diseases: Disease = models.ManyToManyField(Disease, related_name="biosamples")
    """Diseases linked to the biosample."""
    medications: Medication = models.ManyToManyField(
        "Medication", related_name="biosamples"
    )
    """Medications linked to the biosample."""
    artifacts: Artifact = models.ManyToManyField(
        Artifact, through="ArtifactBiosample", related_name="biosamples"
    )
    """Artifacts linked to the biosample."""


class ArtifactBiosample(Record, LinkORM, TracksRun):
    id: int = models.BigAutoField(primary_key=True)
    artifact: Artifact = ForeignKey(Artifact, CASCADE, related_name="links_biosample")
    biosample: Biosample = ForeignKey(Biosample, PROTECT, related_name="links_artifact")
    feature: Feature = ForeignKey(
        Feature,
        PROTECT,
        null=True,
        default=None,
        related_name="links_artifactbiosample",
    )
    label_ref_is_name: bool | None = BooleanField(null=True, default=None)
    feature_ref_is_name: bool | None = BooleanField(null=True, default=None)


class Patient(Record, CanCurate, TracksRun, TracksUpdates):
    """Models a patient in a clinical study.

    Examples:
        >>> patient = Patient(
        ...     uid="internal_patient_id_5446"
        ...     name="Patient 5446",
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

    id: int = models.AutoField(primary_key=True)
    """Internal id, valid only in one DB instance."""
    uid: str = CharField(unique=True, max_length=12, default=ids.base62_12)
    """Universal id, valid across DB instances. Use this field to model internal patient IDs."""
    name: str | None = CharField(db_index=True)
    """Name of the patient."""
    age: int | None = IntegerField(null=True, default=None, db_index=True)
    """Age of the patient."""
    gender: str | None = CharField(
        max_length=10, choices=GENDER_CHOICES, null=True, db_index=True
    )
    """Gender of the patient."""
    ethnicity: Ethnicity = ForeignKey(Ethnicity, PROTECT, null=True, default=None)
    """Ethnicity of the patient."""
    birth_date: datetime | None = DateField(db_index=True, null=True, default=None)
    """Birth date of the patient."""
    deceased: bool | None = BooleanField(db_index=True, null=True, default=None)
    """Whether the patient is deceased."""
    deceased_date: datetime | None = DateField(db_index=True, null=True, default=None)
    """Date of death of the patient."""
    artifacts: Artifact = models.ManyToManyField(
        Artifact, through="ArtifactPatient", related_name="patients"
    )
    """Artifacts linked to the patient."""


class ArtifactPatient(Record, LinkORM, TracksRun):
    id: int = models.BigAutoField(primary_key=True)
    artifact: Artifact = ForeignKey(Artifact, CASCADE, related_name="links_patient")
    patient: Patient = ForeignKey(Patient, PROTECT, related_name="links_artifact")
    feature: Feature = ForeignKey(
        Feature,
        PROTECT,
        null=True,
        default=None,
        related_name="links_artifactpatient",
    )
    label_ref_is_name: bool | None = BooleanField(null=True, default=None)
    feature_ref_is_name: bool | None = BooleanField(null=True, default=None)


class Medication(BioRecord, TracksRun, TracksUpdates):
    """Models a medication."""

    class Meta(BioRecord.Meta, TracksRun.Meta, TracksUpdates.Meta):
        abstract = False
        unique_together = (("name", "ontology_id"),)

    _name_field: str = "name"
    _ontology_id_field: str = "ontology_id"

    id: int = models.AutoField(primary_key=True)
    """Internal id, valid only in one DB instance."""
    uid: str = CharField(unique=True, max_length=8, default=bionty_ids.ontology)
    """A universal id (hash of selected field)."""
    name: str = CharField(max_length=256, db_index=True)
    """Name of the medication."""
    ontology_id: str | None = CharField(max_length=32, db_index=True, null=True)
    """Ontology ID of the medication."""
    chembl_id: str | None = CharField(max_length=32, db_index=True, null=True)
    """ChEMBL ID of the medication."""
    abbr: str | None = CharField(max_length=32, db_index=True, unique=True, null=True)
    """A unique abbreviation of medication."""
    synonyms: str | None = TextField(null=True)
    """Bar-separated (|) synonyms that correspond to this medication."""
    description: str | None = TextField(null=True)
    """Description of the medication."""
    parents: Medication = models.ManyToManyField(
        "self", symmetrical=False, related_name="children"
    )
    """Parent medication records."""
    artifacts: Artifact = models.ManyToManyField(
        Artifact, through="ArtifactMedication", related_name="medications"
    )
    """Artifacts linked to the medication."""

    @overload
    def __init__(
        self,
        name: str,
        ontology_id: str | None,
        abbr: str | None,
        synonyms: str | None,
        description: str | None,
        parents: list[Medication],
        source: Source | None,
    ): ...

    @overload
    def __init__(
        self,
        *db_args,
    ): ...

    def __init__(
        self,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)


class ArtifactMedication(Record, LinkORM, TracksRun):
    id: int = models.BigAutoField(primary_key=True)
    artifact: Artifact = ForeignKey(Artifact, CASCADE, related_name="links_medication")
    medication: Medication = ForeignKey(
        Medication, PROTECT, related_name="links_artifact"
    )
    feature: Feature = ForeignKey(
        Feature,
        PROTECT,
        null=True,
        default=None,
        related_name="links_artifactmedication",
    )
    label_ref_is_name: bool | None = BooleanField(null=True, default=None)
    feature_ref_is_name: bool | None = BooleanField(null=True, default=None)


class Treatment(Record, CanCurate, TracksRun, TracksUpdates):
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

    id: int = models.AutoField(primary_key=True)
    """Internal id, valid only in one DB instance."""
    uid: str = CharField(unique=True, max_length=12, default=ids.base62_12)
    """Universal id, valid across DB instances."""
    name: str | None = CharField(db_index=True)
    """Name of the treatment."""
    status: str | None = CharField(max_length=16, choices=STATUS_CHOICES, null=True)
    """Status of the treatment."""
    medication: Medication | None = ForeignKey(
        Medication, PROTECT, null=True, default=None
    )
    """Medications linked to the treatment."""
    dosage: float | None = FloatField(null=True, default=None)
    """Dosage of the treatment."""
    dosage_unit: str | None = CharField(max_length=32, null=True)
    """Unit of the dosage."""
    administered_datetime: datetime | None = DateTimeField(null=True, default=None)
    """Date and time the treatment was administered."""
    duration: DurationField = DurationField(null=True, default=None)
    """Duration of the treatment."""
    route: str | None = CharField(max_length=32, null=True)
    """Route of administration of the treatment."""
    site: str | None = CharField(max_length=32, null=True)
    """Body site of administration of the treatment."""
    artifacts: Artifact = models.ManyToManyField(
        Artifact, through="ArtifactTreatment", related_name="treatments"
    )
    """Artifacts linked to the treatment."""


class ArtifactTreatment(Record, LinkORM, TracksRun):
    id: int = models.BigAutoField(primary_key=True)
    artifact: Artifact = ForeignKey(Artifact, CASCADE, related_name="links_treatment")
    treatment: Treatment = ForeignKey(Treatment, PROTECT, related_name="links_artifact")
    feature: Feature = ForeignKey(
        Feature,
        PROTECT,
        null=True,
        default=None,
        related_name="links_artifacttreatment",
    )
    label_ref_is_name: bool | None = BooleanField(null=True, default=None)
    feature_ref_is_name: bool | None = BooleanField(null=True, default=None)
