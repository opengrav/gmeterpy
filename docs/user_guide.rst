User guide
==========

Units (`gmeterpy.units`)
------------------------

The unit aware calculations is one of the main goals of the `gMeterPy`. 
We are using `astropy.units` sub-package for this. To use units you need 
to import `gmeterpy.units` module:

>>> import gmeterpy.units as u

And now you can work with gravity acceleration SI units:

>>> gravity = 9.8 * u.m / u.s**2
>>> gravity
<Quantity 9.8 m / s2>

and convert them to more convinient CGS units:

>>> gravity.to(u.Gal)
<Quantity 980. Gal>

and even use prefixes (u -- micro):

>>> gravity.to(u.uGal)
<Quantity 9.8e+08 uGal>

In addition to Astropy built-in units we introduce Eotvos unit for
the gravity gradient:

>>> gradient = 0.3086 * u.mGal / u.m
>>> gradient.to(u.E)
<Quantity 3086. E>


Constants (`gmeterpy.constants`)
--------------------------------

The `gMeterPy` uses `astropy.constants` sub-package for handling constants.
We expand it for some frequently used constants in gravimetry.

+------------+-------+------------------------------------------------+
| Constant   |  Description                                           |
+============+========================================================+
| `omega`    | Mean angular rotation rate of the Earth                |
+------------+-------+------------------------------------------------+
| `atm_sens` | Default gravity/pressure sensitivity (0.3 uGal / mbar) |
+------------+-------+------------------------------------------------+

International Standard Atmosphere
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The Standard Atmosphere (ISO 2533:1975) is used to calculate 
the normal pressure in the atmospheric pressure correction.

+----------+-------+----------------------------------------------+
| Constant |  Description                                         |
+==========+======================================================+
|   `p0`   | Standard atmospheric pressure at sea level           |
+----------+-------+----------------------------------------------+
|   `L`    | Temperature lapse rate                               |
+----------+-------+----------------------------------------------+
|   `Tn`   | Standard thermodynamic air temperature at sea level  |
+----------+-------+----------------------------------------------+
|   `gn`   | Standard acceleration of free-fall                   |
+----------+-------+----------------------------------------------+
|   `M`    | Air molar mass at sea level                          |
+----------+-------+----------------------------------------------+
|   `R`    |  Universal gas constant                              |
+----------+-------+----------------------------------------------+
