.. image:: https://raw.githubusercontent.com/lorenzodb1/fbrefdata/master/docs/_static/logo2.png
   :align: center
   :alt: fbrefdata
   :width: 600px

.. badges-begin

|Downloads| |PyPI| |Python Version| |License| |Read the Docs| |Tests| |Codecov| |pre-commit| |Black|

.. |Downloads| image:: https://static.pepy.tech/badge/soccerdata/month
   :target: https://pepy.tech/project/soccerdata
   :alt: Downloads Per Month
.. |PyPI| image:: https://img.shields.io/pypi/v/soccerdata.svg
   :target: https://pypi.org/project/soccerdata/
   :alt: PyPI
.. |Python Version| image:: https://img.shields.io/pypi/pyversions/fbrefdata
   :target: https://pypi.org/project/fbrefdata
   :alt: Python Version
.. |License| image:: https://img.shields.io/pypi/l/fbrefdata.svg
   :target: https://opensource.org/licenses/Apache-2.0
   :alt: License
.. |Read the Docs| image:: https://img.shields.io/readthedocs/fbrefdata/latest.svg?label=Read%20the%20Docs
   :target: https://fbrefdata.readthedocs.io/
   :alt: Read the documentation at https://fbrefdata.readthedocs.io/
.. |Tests| image:: https://github.com/lorenzodb1/fbrefdata/workflows/CI/badge.svg
   :target: https://github.com/lorenzodb1/fbrefdata/actions?workflow=CI
   :alt: Tests
.. |Codecov| image:: https://codecov.io/gh/lorenzodb1/fbrefdata/branch/master/graph/badge.svg
   :target: https://app.codecov.io/gh/lorenzodb1/fbrefdata
   :alt: Codecov
.. |pre-commit| image:: https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white
   :target: https://github.com/pre-commit/pre-commit
   :alt: pre-commit
.. |Black| image:: https://img.shields.io/badge/code%20style-black-000000.svg
   :target: https://github.com/psf/black
   :alt: Black

.. badges-end

SoccerData is a collection of scrapers to gather soccer data from popular
websites, including `Club Elo`_, `ESPN`_, `FBref`_, `FiveThirtyEight`_,
`Football-Data.co.uk`_, `FotMob`_, `SoFIFA`_, `Understat`_ and `WhoScored`_.
You get Pandas DataFrames with sensible, matching column names and identifiers
across datasets. Data is downloaded when needed and cached locally.

.. code:: python

   import fbrefdata as fd

   # Create a scraper class instance for the 2018/19 Premier League
   five38 = sd.FiveThirtyEight('ENG-Premier League', '1819')

   # Fetch data
   games = five38.read_games()
   forecasts = five38.read_forecasts()
   clinches = five38.read_clinches()

To learn how to install, configure and use SoccerData, see the
`Quickstart guide <https://soccerdata.readthedocs.io/en/latest/intro.html>`__. For documentation on each of the
supported data sources, see the `example notebooks <https://soccerdata.readthedocs.io/en/latest/datasources/>`__
and `API reference <https://soccerdata.readthedocs.io/en/latest/reference/>`__.

.. _FBref: https://www.fbref.com/en/
.. _FiveThirtyEight: https://fivethirtyeight.com/soccer-predictions/
.. _Football-Data.co.uk: https://www.football-data.co.uk/
.. _FotMob: https://fotmob.com/
.. _SoFIFA: https://sofifa.com/
.. _Understat: https://understat.com/
.. _WhoScored: https://www.whoscored.com/

**Usage Notice:** Please use this web scraping tool responsibly and in compliance with the terms of service of the
websites you intend to scrape. The software is provided as-is, without any warranty or guarantees of any kind. The
developers disclaim any responsibility for misuse, legal consequences, or damages resulting from its use. It is
your responsibility to use the software in accordance with the laws and regulations of your jurisdiction.

**Contribution and Issues:** As soccerdata relies on web scraping, any changes to the
scraped websites will break the package. Hence, do not expect that all code
will work all the time. If you spot any bugs, then please `fork it and start
a pull request <https://github.com/lorenzodb1/fbrefdata/blob/master/CONTRIBUTING.rst>`__.
