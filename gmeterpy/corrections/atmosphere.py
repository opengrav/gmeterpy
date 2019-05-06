# -*- coding: utf-8 -*-
"""Atmospheric pressure correction.

This module contains the atmospheric correction to the gravity observations.
"""


def normal_pressure(height):
    r"""Normal atmospheric pressure, in Pa.

    Parameters
    ----------
    height : float or array_like
        Height above sea level, in metres.

    Returns
    -------
    float or array_like: Normal pressure, in Pa.

    Notes
    -----
    The normal pressure is referred to the DIN5450 (ISO 2533:1975)
    Standard Atmosphere [1]_:

    .. math::

       p_n = 1.01325\times 10^5 \left(1 -
       0.0065 \dfrac{H}{288.15}\right)^{5.2559}\quad [\textrm{Pa}]

    where :math:`H` -- physical height of the station in metres.

    Reference
    ---------
    .. [1] International Organization for Standardization
       1975 Standard Atmosphere ISO 2533 1975

    """

    p_n = 101325 * (1 - 0.0065 * height / 288.15) ** 5.2559

    return p_n


def atmospheric_pressure_correction(height, pressure, barometric_factor=0.30):
    r"""Atmospheric pressure correction, in m/s**2.

    Parameters
    ----------
    height : float or array_like
        Height above sea level, in metres.
    pressure : float or array_like
        Observed atmospheric pressure, in Pa.
    barometric_factor : float
        Barometric factor, in 1e-10 m/s**2 / Pa.
        Default is 0.30e-10 m/s**2 / Pa (or 0.3 muGal / mBar)
        as recommended by IAG.

    Returns
    -------
    float or array_like:  Atmospheric pressure correction, in m/s**2.

    Notes
    -----
    The lumped effects of direct gravitation of air mass changes and indirect
    effect via deformation of the solid earth have been determined
    empirically from air pressure variations. It is recommended to
    reduce these effects through (IAG 1983 resolution no. 9)

    .. math::

       \delta g = 0.30\times 10^{-10} (p_a - p_n)\quad [\textrm{ms}^{-2}]

    where :math:`p_a` -- actual observed air pressure,
    :math:`p_n` -- normal pressure calculated by
    :meth:`~gmeterpy.corrections.atmosphere.normal_pressure` function,
    0.30 -- default barometric factor.

    """

    p_n = normal_pressure(height)
    return barometric_factor * 1e-10 * (pressure - p_n)
