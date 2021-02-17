========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |coveralls| |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|

.. |docs| image:: https://readthedocs.org/projects/python-unlzw/badge/?style=flat
    :target: https://readthedocs.org/projects/python-unlzw
    :alt: Documentation Status

.. |travis| image:: https://travis-ci.org/ionelmc/python-unlzw.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/ionelmc/python-unlzw

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/ionelmc/python-unlzw?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/ionelmc/python-unlzw

.. |requires| image:: https://requires.io/github/ionelmc/python-unlzw/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/ionelmc/python-unlzw/requirements/?branch=master

.. |coveralls| image:: https://coveralls.io/repos/ionelmc/python-unlzw/badge.svg?branch=master&service=github
    :alt: Coverage Status
    :target: https://coveralls.io/r/ionelmc/python-unlzw

.. |codecov| image:: https://codecov.io/github/ionelmc/python-unlzw/coverage.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/ionelmc/python-unlzw

.. |version| image:: https://img.shields.io/pypi/v/unlzw.svg
    :alt: PyPI Package latest release
    :target: https://pypi.python.org/pypi/unlzw

.. |commits-since| image:: https://img.shields.io/github/commits-since/ionelmc/python-unlzw/v0.1.2.svg
    :alt: Commits since latest release
    :target: https://github.com/ionelmc/python-unlzw/compare/v0.1.2...master

.. |wheel| image:: https://img.shields.io/pypi/wheel/unlzw.svg
    :alt: PyPI Wheel
    :target: https://pypi.python.org/pypi/unlzw

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/unlzw.svg
    :alt: Supported versions
    :target: https://pypi.python.org/pypi/unlzw

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/unlzw.svg
    :alt: Supported implementations
    :target: https://pypi.python.org/pypi/unlzw


.. end-badges

Bindings for Mark Adler's `unlzw
<https://mathematica.stackexchange.com/questions/60531/how-can-i-read-compressed-z-file-automatically-by-mathematica/60879#60879>`_
library.

* Free software: BSD 3-Clause License

Installation
============

::

    pip install unlzw

Documentation
=============

.. code-block:: python

    from unlzw import unlzw

    assert unlzw(b'\x1f\x9d\x90f\xde\xbc\x11\x13FN\xc0\x81\x05\x0f\x124(p\xa1\xc2\x82') == b'foobarfoobarfoobarfoobarfoobar'
