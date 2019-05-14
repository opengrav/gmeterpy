# -*- coding: utf-8 -*-
# flake8: noqa
"""Units support for gMeterPy.

The `gMeterPy` is supporting units via `astropy.units` subpackage.
The Gal unit (1 Gal = 1 cm / s**2) is already there.

In addition, the Eotvos unit (1 E = 10**-9 s**-2) for the gravity gradient is
defined.

"""

from astropy.units import *

# define namespace
def_unit(['E', 'Eotvos'], represents=1e-9 * s**-2,
         doc='Eötvös-unit for the gravity gradient.',
         prefixes=True, namespace=globals())
