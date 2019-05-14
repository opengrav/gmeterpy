# -*- coding: utf-8 -*-
"""Constants for gMeterPy.

"""

from astropy.constants import Constant


omega = Constant(
    abbrev='omega',
    name='Mean angular rotation rate of the Earth',
    value=7292115.0e-11,
    unit='rad / s',
    uncertainty=0.0,
    reference='')

atm_sens = Constant(
    abbrev='atm_sens',
    name='Default sensitivity of changes in gravity '
    'with variations in atmospheric pressure.',
    value=0.3,
    unit='uGal / mbar',
    uncertainty=0.0,
    reference='IAG 1983 Resolution no.9')


# ISO 2533:1975 constants
class ISA1975(Constant):
    default_reference = 'Standard Atmosphere ISO 2533:1975'
    _registry = {}
    _has_incompatible_units = set()


p0 = ISA1975('p0', 'Standard atmospheric pressure at sea level.',
             101325.0, 'Pa', 0.0, system='si')

L = ISA1975('L', 'Temperature lapse rate.',
            0.0065, 'K / m', 0.0, system='si')

Tn = ISA1975('Tn', 'Standard thermodynamic air temperature at sea level.',
             288.15, 'K', 0.0, system='si')

gn = ISA1975('gn', 'Standard acceleration of free-fall.',
             9.80665, 'm / s**2', 0.0, system='si')

M = ISA1975('M', 'Air molar mass at sea level.',
            0.028964420, 'kg / mol', 0.0, system='si')

R = ISA1975('R', 'Universal gas constant.',
            8.31432, 'J / (mol * K)', 0.0, system='si')
