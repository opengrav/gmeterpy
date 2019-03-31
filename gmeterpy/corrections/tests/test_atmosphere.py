"""
Test atmospheric pressure correction.

"""

import os
import numpy as np

from gmeterpy.corrections.atmosphere import normal_pressure
from gmeterpy.corrections.atmosphere import atmospheric_pressure_correction

# load test data
path = os.path.dirname(os.path.abspath(__file__))
fname = os.path.join(path, 'data/atmospheric_pressure_correction.txt')
height, t_pressure, t_atm_corr = np.loadtxt(fname, usecols=(0, 1, 2), unpack=True,
                                            dtype=np.float32)


def test_normal_pressure():
    """Test normal pressure calculation.

    """
    pressure = normal_pressure(height)

    np.testing.assert_array_almost_equal(pressure, t_pressure, decimal=1)


def test_atmospheric_pressure_corrections():
    """Test atmospheric pressure correction.

    """
    # "measured" pressure, in Pa
    measured_pressure = 99536

    atm_corr = atmospheric_pressure_correction(height, measured_pressure)

    np.testing.assert_array_almost_equal(atm_corr * 1e8, t_atm_corr, decimal=1)
