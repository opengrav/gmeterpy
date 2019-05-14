# -*- coding: utf-8 -*-
"""Polar motion correction.

This module contains the polar motion correction to the gravity observations.

"""

import warnings
import numpy as np
from astropy.utils import iers

import gmeterpy.units as u
from gmeterpy.constants import omega


iers.conf.auto_max_age = 10
iers.conf.auto_download = True
IERS_A_URL = 'ftp://ftp.iers.org/products/eop/rapid/standard/finals2000A.all'
iers.conf.iers_auto_url = IERS_A_URL
iers.conf.remote_timeout = 60

STATUS = {iers.FROM_IERS_B: 'IERS_B',
          iers.FROM_IERS_A: 'IERS_A',
          iers.FROM_IERS_A_PREDICTION: 'IERS_A',
          iers.TIME_BEFORE_IERS_RANGE: 'OUT_OF_RANGE',
          iers.TIME_BEYOND_IERS_RANGE: 'OUT_OF_RANGE'}


NOT_FROM_IERS_B = """\
Some pole coordinates are not from IERS Bulletin B and are not final.
They will change in the future. This may affect precision depending on the time
elapsed since the latest release of the IERS Bulletin B.

Please check your dates, update IERS tables or redo calculations
when the Bulletin B will be released on your dates.
"""


def get_polar_motion(time, return_status=False):
    """Interpolate polar motions from the IERS for the given time.

    This function will automatically download IERS data and interpolate
    pole coordinates for the given time.

    Parameters
    ----------
    time : float, array, or `astropy.time.Time` object
        Julian Date or `astropy.time.Time` object.
    return_status : bool
        Whether to return status values.

    Returns
    -------
    xp, yp : ~astropy.units.Quantity
        Polar motion coordinates, in arcsec.
    status : str or list
        Status values (if `return_status`=`True`):

        * 'IERS_B' pole coordinates are from IERS Bulletin B (final).
        * 'IERS_A' pole coordinates are from IERS Bulletin A (preliminary).
        * 'OUT_OF_RANGE' given `time` is out of IERS data range.

    """

    xp, yp, status = iers.IERS_Auto.open().pm_xy(time, return_status=True)

    if np.any(status != iers.FROM_IERS_B):
        wmsg = NOT_FROM_IERS_B
        warnings.warn(wmsg)

    if return_status:
        status_new = [STATUS.get(e, e) for e in status.ravel()]
        return xp, yp, status_new
    else:
        return xp, yp


@u.quantity_input(xp=u.rad, yp=u.rad, lat=u.deg, lon=u.deg, radius=u.m)
def polar_motion_correction(xp, yp, lat, lon, radius=6378136 * u.m, delta=1.164):
    r"""Polar motion correction.

    Parameters
    ----------
    xp : ~astropy.units.Quantity
        x coordinate of the terrestrial pole.
    yp : ~astropy.units.Quantity
        y coordinate of the terrestrial pole.
    lat : ~astropy.units.Quantity
        Geocentric latitude of the observation point referred to IERS pole.
    lon : ~astropy.units.Quantity
        Geocentric longitude of the observation point referred to IERS pole.
    radius : ~astropy.units.Quantity, optional
        Geocentric radius. Default value is `r = a = 6378136` m.
    delta : float, optional
        Gravimetric amplitude factor, default is 1.164.

    Returns
    -------
    delta_g_polar : ~astropy.units.Quantity
        Polar motion correction.

    Notes
    -----
    Variations in the geocentric position of the Earth's rotation axis
    (polar motion) cause deformation within the Earth due to centrifugal forces.
    The actual position of the rotational axis is referenced to the IERS pole
    and described by the pole coordinates. The gravity correction (pole tide)
    is expressed by, e.g. Wahr (1985) [1]_:

    .. math::

       \Delta g = -\delta\omega^2\times r \times 2 \times
       \sin\phi\cos\phi\left(x_p\cos\lambda - y_p\sin\lambda\right)\quad
       [\textrm{ms}^{-2}]

    where :math:`x_p,y_p` -- pole coordinates,
    :math:`\omega` -- mean angular velocity,
    :math:`r = a = 6 378 136` [m] -- equatirial radius of the Earth,
    :math:`\phi,\lambda` -- geocentric coordinates of the station,
    :math:`\delta = 1.164` -- is the amplitude factor for
    the elastic response of the Earth.

    Reference
    ---------
    .. [1] Wahr, J. M. ( 1985), Deformation induced by polar motion,
       J. Geophys. Res., 90( B11), 9363– 9368, doi:10.1029/JB090iB11p09363

    """

    delta_lat = xp * np.cos(lon) - yp * np.sin(lon)
    delta_g_polar = -delta * omega**2 * radius * np.sin(2 * lat) * delta_lat

    return delta_g_polar.to(u.uGal, equivalencies=u.dimensionless_angles())
