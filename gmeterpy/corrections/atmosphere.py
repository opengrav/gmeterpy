# -*- coding: utf-8 -*-
"""Atmospheric pressure correction.

This module contains the atmospheric correction to the gravity observations.

"""

import gmeterpy.units as u
import gmeterpy.constants as c


@u.quantity_input
def normal_pressure(height: u.m) -> u.Pa:
    r"""Normal atmospheric pressure.

    Parameters
    ----------
    height : ~astropy.units.Quantity
        Height above sea level.

    Returns
    -------
    pn : ~astropy.units.Quantity
        Normal pressure.

    Notes
    -----
    The normal pressure is referred to the DIN5450 (ISO 2533:1975)
    Standard Atmosphere [1]_:

    .. math::

       p_n = 101325 \left(1 -
       0.0065 \dfrac{H}{288.15}\right)^{5.2559}\quad [\textrm{Pa}]

    where :math:`H` -- physical height of the station in metres.

    Reference
    ---------
    .. [1] International Organization for Standardization
       1975 Standard Atmosphere ISO 2533 1975

    """
    # pn = 101325 * (1 - 0.0065 * height / 288.15) ** 5.2559
    pn = c.p0 * (1 - c.L * height / c.Tn)**(c.gn * c.M / c.R / c.L).round(4)

    return pn


@u.quantity_input
def atmospheric_pressure_correction(height: u.m, pressure: u.Pa,
                                    barometric_factor:
                                    u.uGal / u.mbar = c.atm_sens) -> u.uGal:
    r"""Atmospheric pressure correction.

    Parameters
    ----------
    height : ~astropy.units.Quantity
        Height above sea level.
    pressure : ~astropy.units.Quantity
        Observed atmospheric pressure.
    barometric_factor : ~astropy.units.Quantity
        Barometric factor.
        Default is 0.3 uGal / mBar as recommended by IAG.

    Returns
    -------
    delta_g_atm : ~astropy.units.Quantity
        Atmospheric pressure correction.

    Notes
    -----
    The lumped effects of direct gravitation of air mass changes and indirect
    effect via deformation of the solid earth have been determined
    empirically from air pressure variations. It is recommended to
    reduce these effects through (IAG 1983 resolution no. 9)

    .. math::

       \Delta g = 0.30\times 10^{-10} (p_a - p_n)\quad [\textrm{ms}^{-2}]

    where :math:`p_a` -- actual observed air pressure,
    :math:`p_n` -- normal pressure calculated by
    `gmeterpy.corrections.atmosphere.normal_pressure` function,
    0.3 uGal / mBar -- default barometric factor.

    The actual value of :math:`p_n` needs to be documented.

    """
    delta_p = pressure - normal_pressure(height)
    delta_g_atm = barometric_factor * delta_p
    return delta_g_atm
