===========================
How to add custom leagues
===========================

FBrefData has built-in support to scrape data from the top-5 European leagues
and the major international tournaments. The leagues available for each source
can be listed with the :meth:`~fbrefdata.FBref.available_leagues` class method.

.. code:: python

  import fbrefdata as sd
  sd.FBref.available_leagues()
  >>> ['ENG-Premier League', 'ESP-La Liga', 'FRA-Ligue 1', 'GER-Bundesliga', 'ITA-Serie A']

This documentation explains how to add custom leagues.


.. warning::

  Note that you might encounter errors when trying to scrape data for the
  leagues you added yourself. This is because the data provided for these
  leagues might have a different structure. If you encounter such an error,
  please do not open an issue on GitHub, but try to fix it yourself.



Adding a new league
-------------------

Additional leagues can configured in ``FBREFDATA_DIR/config/league_dict.json``.
This file should contain a mapping between a generic name for the league and
the identifier used internally by each data source (see below) that you want
to support. For example, for the Dutch Eredivisie this would be:

.. code-block:: json

  {
    "NED-Eredivisie": {
      "FBref": "Eredivisie",
      "season_start": "Aug",
      "season_end": "May"
    }
  }

The ``season_end`` and ``season_start`` fields are optional. This should be
the month in which the last game and first game of a season are played,
respectively. If they are not provided, June is used as the last month of the
season and July as the first one.

Now, restart your Python session and check whether it is added to available
leagues by running the command below.

.. code:: python

  >>> import fbrefdata as sd
  >>> sd.FBref.available_leagues()
  [..., 'NED-Eredivisie', ...]



Internal identifiers
--------------------

Below are instructions on how to find the internal identifiers for each data
source.

**FBref**
  Go to https://fbref.com/en/comps/ and take the value in the ``Competition
  Name`` column.

Troubleshooting
---------------

If you add a new league and it doesn't show up in the list of available leagues,
there are a few things you can do to debug the problem.

1. Make sure to reload the fbrefdata module after you modify the
   ``league_dict.json`` file. The most straightforward way to do this is to
   restart your notebook or Python interpreter.

2. Check whether your ``league_dict.json`` file is at the correct location. If
   so, you should see this appear in the log messages when importing the
   fbrefdata library.

   .. code:: python

     >>> import fbrefdata as sd
     [11/25/22 11:49:12] INFO     Custom team name replacements loaded from <path>/teamname_replacements.json.                                                                                                _config.py:83
                         INFO     Custom league dict loaded from <path>/league_dict.json.                                                                                                                    _config.py:153


3. Check whether the content of your ``league_dict.json`` file is valid JSON.
   You can check the file's syntax using Python's built-in ``json.tool``
   module.

   .. code:: sh

      $ cat config/league_dict.json | python -m json.tool
      Expecting ',' delimiter: line 1 column 10 (char 9)
