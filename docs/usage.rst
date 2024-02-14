.. _quickstart:

Usage
=====

This tutorial will walk you through installing, configuring, and using
fbrefdata.


Installation
------------

fbrefdata can be easily installed via `pip <https://pip.readthedocs.org/>`__:

.. code:: bash

  python3 -m pip install fbrefdata


Global configuration
---------------------

Several settings that can be configured globally using the following environment variables:

``FBREFDATA_DIR``
    The directory where the downloaded data is cached and where logs are
    stored. By default, all data is stored to ``~/fbrefdata`` on Linux / Mac
    OS and ``C:\Users\yourusername\fbrefdata`` on Windows.
``FBREFDATA_NOCACHE``
    If set to "true", no cached data is returned. Note that no-cache does not
    mean "don't cache". All downloaded data is still cached and overwrites
    existing caches. If the sense of "don't cache" that you want is actually
    "don't store", then ``fbrefdata_NOSTORE`` is the option to use. By default,
    data is retrieved from the cache.
``FBREFDATA_NOSTORE``
    If set to "true", no data is stored. By default, data is cached.
``FBREFDATA_LOGLEVEL``
    The level of logging to use. By default, this is set to "INFO".

Example:

.. code-block:: bash

  # bash
  export FBREFDATA_DIR = "~/fbrefdata"
  export FBREFDATA_NOCACHE = "False"
  export FBREFDATA_NOSTORE = "False"
  export FBREFDATA_LOGLEVEL = "INFO"

Scraping data
-------------

Each of the supported data sources has its corresponding class for fetching
data with a uniform API. For example, the :class:`~fbrefdata.FBref` class is
used to fetch data from `fbref.com <https://www.fbref.com/>`__.

.. code:: python

   import fbrefdata as sd

   # Create scraper class instance
   fbref = sd.FBref()

This will create a ``fbrefdata/FBref/`` folder in your home directory  in
which all scraped data will be cached and where logs will be saved. If you
prefer to store the data in a different folder or disable caching, you can
configure this using environment variables (see above) or by setting the
``data_dir``, ``no_cache`` and ``no_store`` parameters which are supported by
each scraper class.

.. code:: python

   # Create scraper class instance with custom caching behavior
   fbref = sd.FBref(data_dir="/tmp", no_cache=True, no_store=True)

Once you have a scraper class instance, you can use it to fetch data. See the
:ref:`API reference <api>` for the full list of options available for each scraper. For
example, to fetch aggregated shooting stats for all teams:

.. code:: python

   # Create dataframes
   season_stats = fbref.read_team_season_stats(stat_type='shooting')


The data is always returned as a convenient Pandas DataFrame.

.. csv-table::
   :file: output.csv
   :header-rows: 1

Not all data sources provide data for all leagues. The leagues available for
each source can be listed with the :meth:`~fbrefdata.FBref.available_leagues`
class method.

.. code:: python

   sd.FBref.available_leagues()
   >>> ['ENG-Premier League', 'ESP-La Liga', 'FRA-Ligue 1', 'GER-Bundesliga', 'ITA-Serie A', ...]


By default, the data for all available leagues and 10 most recent seasons will
be downloaded. In most cases, you would want to limit the data to a specific
league and / or seasons. This can be done by passing a list of leagues and
seasons to the constructor of the scraper class. For example:

.. code:: python

   # Create scraper class instance filtering on specific leagues and seasons
   fbref = sd.FBref(leagues=['ENG-Premier League'], seasons=['1718', '1819'])


See the examples and :ref:`API reference <api>` for detailed instructions for
each of the available data sources.

Adding additional leagues
-------------------------

The top-5 European leagues are fully supported. If you want to add more
leagues, you can configure these in ``fbrefdata_DIR/config/league_dict.json``.
This file should contain a mapping between a generic name for the league and
the identifier used internally by each data source that you want to support.
For example, for the Dutch Eredivisie this would be:

.. code-block:: json

  {
    "NED-Eredivisie": {
      "FBref": "Dutch Eredivisie"
    }
  }

The ``season_end`` and ``season_start`` fields are optional. This should be the
month in which the last game and first game of a season are played,
respectively. If they are not provided, June is used as the last month of the
season and July as the first one.

Note that the provided scrapers might give some errors for the leagues you add
yourself. This is because the same data is not always available for all seasons.


Uniform team names
------------------

Each data source uses a different set of team names, which makes it difficult
to combine data from multiple sources. To mitigate this, fbrefdata allows
translating the team names to uniform names. This is done by providing
a ``fbrefdata_DIR/config/team_dict.json`` file. This file should contain a
mapping between a generic name for each team and the team name used by each
data source that you want to support. The example below will map "Tottenham
Hotspur", "Tottenham Hotspur FC" and "Spurs" to "Tottenham" in all scraped
data.

.. code-block:: json

  {
    "Tottenham": ["Tottenham Hotspur", "Tottenham Hotspur FC", "Spurs"],
  }

Next steps
----------
Look at you! You’re now basically an expert at fbrefdata! ✨

From this point you can:

- Look at the example notebooks for each :ref:`Data source <datasources>`.
- Take a deep dive into the :ref:`API <api>`.
- Give us feedback or contribute, see :ref:`Contributing <contributing>`.

Have fun! 🎉
