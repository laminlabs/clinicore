"""A clinicorel schema.

Import the package::

   import clinicore

This is the complete API reference:

.. autosummary::
   :toctree: .

   Biosample
   ClinicalTrial
   Medication
   Patient
   Treatment
"""

__version__ = "0.4.0"  # denote a pre-release for 0.1.0 with 0.1rc1

from lamindb_setup import _check_instance_setup


# trigger instance loading if users
# want to access attributes
def __getattr__(name):
    if name not in {"models"}:
        _check_instance_setup(from_lamindb=True)
    return globals()[name]


if _check_instance_setup():
    del __getattr__  # delete so that imports work out
    from .models import (
        Biosample,
        ClinicalTrial,
        Medication,
        Patient,
        Treatment,
    )
