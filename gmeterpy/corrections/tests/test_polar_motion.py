# -*- coding: utf-8 -*-
"""
Test atmospheric pressure correction.

"""
import os
import numpy as np

import pytest
from astropy.time import Time, TimeDelta

import gmeterpy.units as u
import gmeterpy.corrections.polar_motion as pm


@pytest.mark.xfail('TRAVIS' in os.environ and os.environ['TRAVIS'] == 'true',
                   reason='Skipping this test on Travis CI.')
def test_get_polar_motion():
    """Test get_polar_motion function.

    """

    # Bulletin B with status
    time = Time('2013-01-01')
    pm_xy = pm.get_polar_motion(time, return_status=True)
    assert len(pm_xy) == 3
    assert pm_xy[-1][0] == 'IERS_B'
    np.testing.assert_almost_equal(pm_xy[0].value, 0.075311, 6)
    np.testing.assert_almost_equal(pm_xy[1].value, 0.289933, 6)

    # Bulletin B with no status
    pm_xy = pm.get_polar_motion(time, return_status=False)
    assert len(pm_xy) == 2
    np.testing.assert_almost_equal(pm_xy[0].value, 0.075311, 6)
    np.testing.assert_almost_equal(pm_xy[1].value, 0.289933, 6)

    # Bulletin A
    time = Time.now()
    xp, yp, status = pm.get_polar_motion(time, return_status=True)
    assert status[0] == 'IERS_A'

    # Out of range
    delta = TimeDelta(400, format='jd')
    time += delta
    xp, yp, status = pm.get_polar_motion(time, return_status=True)
    assert status[0] == 'OUT_OF_RANGE'


def test_polar_motion_correction():
    """Test polar motion correction.

    """
    xp, yp = 0.1375 * u.arcsec, 0.3944 * u.arcsec
    lat, lon = 55.855 * u.deg, 37.516 * u.deg

    grav_corr = pm.polar_motion_correction(xp, yp, lat, lon)

    assert grav_corr.round(2) == 2.33 * u.uGal
