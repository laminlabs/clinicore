"""Basic clinical entities [`source <https://github.com/laminlabs/clinicore/blob/main/clinicore/models.py>`__].

Install and mount `clinicore` in a new instance:

>>> pip install clinicore
>>> lamin init --storage ./test-clinicore --schema bionty,clinicore

Import the package:

>>> import clinicore as cc

Registries:

.. autosummary::
   :toctree: .

   Biosample
   ClinicalTrial
   Medication
   Patient
   Treatment
"""

__version__ = "0.5.0"  # denote a pre-release for 0.1.0 with 0.1rc1

from lamindb_setup import _check_instance_setup


def __getattr__(name):
    if name != "models":
        _check_instance_setup(from_module="clinicore")
    return globals()[name]


if _check_instance_setup():
    import lamindb

    del __getattr__  # delete so that imports work out
    from .models import (
        Biosample,
        ClinicalTrial,
        Medication,
        Patient,
        Treatment,
    )
