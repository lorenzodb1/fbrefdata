=============================
Welcome to FBrefData's docs!
=============================

Release v\ |release|. (``pip install fbrefdata``)


.. image:: https://pepy.tech/badge/fbrefdata/month
    :target: https://pepy.tech/project/fbrefdata
    :alt: SoccerData Downloads Per Month Badge

.. image:: https://img.shields.io/pypi/l/fbrefdata.svg
    :target: https://pypi.org/project/fbrefdata/
    :alt: License Badge

.. image:: https://img.shields.io/pypi/pyversions/fbrefdata.svg
    :target: https://pypi.org/project/fbrefdata/
    :alt: Python Version Support Badge


**FBrefData** is a collection of scrapers to gather soccer data from `FBref`_.

.. code:: python

   import fbrefdata as sd

   # Create a scraper class instance for the 2018/19 Premier League
   fbref = sd.FBref('ENG-Premier League', '1819')

   # Fetch data
   schedule = fbref.read_schedule()
-------------------

**Main features**

- Access current and historical soccer fixtures, forecasts, detailed match
  stats, event stream data and more.
- Data is only downloaded when needed and cached locally to speed up your
  analyis scripts.

Do you like it? :doc:`Let's dive in! <intro>`

.. toctree::
   :hidden:
   :maxdepth: 1

   intro
   datasources/index
   howto/index
   examples/index
   reference/index
   faq
   contributing
   License <license>
   Changelog <https://github.com/lorenzodb1/fbrefdata/releases>

.. _FBref: https://www.fbref.com/en/
