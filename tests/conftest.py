"""Pytest fixtures for fbrefdata package."""

import pytest

import fbrefdata as fd
import fbrefdata._common


@pytest.fixture
def fbref_ligue1(mocker):
    """Return a correctly initialized instance of FBref filtered by league: Ligue 1."""
    mock_leagues = {
        "FRA-Ligue 1": {
            "FBref": "Ligue 1",
            "season_start": "Aug",
            "season_end": "May"
        }
    }
    mocker.patch.object(fd._common, "get_all_leagues", return_value=mock_leagues)
    return fd.FBref(leagues="FRA-Ligue 1", seasons=2021)
