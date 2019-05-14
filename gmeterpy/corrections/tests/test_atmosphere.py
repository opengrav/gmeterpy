"""
Test atmospheric pressure correction.

"""

import os
import numpy as np

import gmeterpy.units as u

from gmeterpy.corrections.atmosphere import normal_pressure
from gmeterpy.corrections.atmosphere import atmospheric_pressure_correction

# load test data
path = os.path.dirname(os.path.abspath(__file__))
fname = os.path.join(path, 'data/atmospheric_pressure_correction.txt')
height, t_pressure, t_atm_corr = np.loadtxt(fname, usecols=(0, 1, 2), unpack=True,
                                            dtype=np.float32)

height *= u.m
t_pressure *= u.Pa
t_atm_corr *= u.uGal


def test_normal_pressure():
    """Test normal pressure calculation.

    """
    pressure = normal_pressure(height)

    assert isinstance(pressure, u.Quantity)

    np.testing.assert_array_almost_equal(pressure.value,
                                         t_pressure.value, decimal=1)

    # Numerical formula from IAGBN
    t_pn_num = 101325 * (1 - 0.0065 * height.value / 288.15) ** 5.2559

    np.testing.assert_array_almost_equal(pressure.value,
                                         t_pn_num, decimal=1)


def test_atmospheric_pressure_corrections():
    """Test atmospheric pressure correction.

    """
    # "measured" pressure, in Pa
    measured_pressure = 99536 * u.Pa

    atm_corr = atmospheric_pressure_correction(height, measured_pressure)

    assert isinstance(atm_corr, u.Quantity)

    np.testing.assert_array_almost_equal(atm_corr.value,
                                         t_atm_corr.value, decimal=1)
