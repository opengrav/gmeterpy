.. _install:

Installing
==========

Installing from PyPI
--------------------

``gMeterPy`` can be installed via ``pip`` from PyPI:

.. code:: bash

    pip install gmeterpy

However, this is not the best option, given that the package is under
active development.

Installing the latest development version
-----------------------------------------

To install ``gMeterPy`` from GitHub simply use ``pip`` as usual: 

.. code:: bash

    pip install https://github.com/opengrav/gmeterpy/archive/master.zip

Or clone the git repository locally and run ``pip``:

.. code:: bash

    git clone https://github.com/opengrav/gmeterpy.git
    cd gmeterpy
    pip install .

Dependencies
------------

The ``gMeterPy`` depends on several open source projects:

* `NumPy <http://www.numpy.org/>`__
* `SciPy <https://docs.scipy.org/doc/scipy/reference/>`__
* `pandas <http://pandas.pydata.org/>`__
* `Matplotlib <https://matplotlib.org/>`__
* `Astropy <https://astropy.org/>`__
