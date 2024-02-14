"""Configurations."""

import json
import logging.config
import os
import sys
from pathlib import Path

from rich.logging import RichHandler

# Configuration
NOCACHE = os.environ.get("FBREFDATA_NOCACHE", 'False').lower() in ('true', '1', 't')
NOSTORE = os.environ.get("FBREFDATA_NOSTORE", 'False').lower() in ('true', '1', 't')
LOGLEVEL = os.environ.get('FBREFDATA_LOGLEVEL', 'INFO').upper()

# Directories
BASE_DIR = Path(os.environ.get("FBREFDATA_DIR", Path.home() / "fbrefdata"))
LOGS_DIR = Path(BASE_DIR, "logs")
DATA_DIR = Path(BASE_DIR, "data")
CONFIG_DIR = Path(BASE_DIR, "config")

# Create dirs
LOGS_DIR.mkdir(parents=True, exist_ok=True)
DATA_DIR.mkdir(parents=True, exist_ok=True)
CONFIG_DIR.mkdir(parents=True, exist_ok=True)

# Logger
logging_config = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "minimal": {"format": "%(message)s"},
        "detailed": {
            "format": "%(levelname)s %(asctime)s [%(filename)s:%(funcName)s:%(lineno)d]\n%(message)s\n"  # noqa: E501
        },
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "stream": sys.stdout,
            "formatter": "minimal",
            "level": logging.DEBUG,
        },
        "info": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": Path(LOGS_DIR, "info.log"),
            "maxBytes": 10485760,  # 1 MB
            "backupCount": 10,
            "formatter": "detailed",
            "level": logging.INFO,
        },
        "error": {
            "class": "logging.handlers.RotatingFileHandler",
            "filename": Path(LOGS_DIR, "error.log"),
            "maxBytes": 10485760,  # 1 MB
            "backupCount": 10,
            "formatter": "detailed",
            "level": logging.ERROR,
        },
    },
    "loggers": {
        "root": {
            "handlers": ["console", "info", "error"],
            "level": LOGLEVEL,
            "propagate": True,
        },
    },
}
logging.config.dictConfig(logging_config)
logger = logging.getLogger("root")
logger.handlers[0] = RichHandler(markup=True)


def get_team_replacements() -> dict:
    teamname_replacements = {}
    _f_custom_teamnname_replacements = CONFIG_DIR / "teamname_replacements.json"
    if _f_custom_teamnname_replacements.is_file():
        with open(_f_custom_teamnname_replacements, encoding='utf8') as json_file:
            for team, to_replace_list in json.load(json_file).items():
                for to_replace in to_replace_list:
                    teamname_replacements[to_replace] = team
        logger.info("Custom team name replacements loaded from %s.", _f_custom_teamnname_replacements)
        return teamname_replacements
    else:
        logger.info(
            "No custom team name replacements found. You can configure these in %s.",
            _f_custom_teamnname_replacements,
        )
        return {}


def get_all_leagues() -> dict:
    _f_custom_league_dict = CONFIG_DIR / "league_dict.json"
    if _f_custom_league_dict.is_file():
        with open(_f_custom_league_dict, encoding='utf8') as json_file:
            logger.info("Custom league dict loaded from %s.", _f_custom_league_dict)
            return json.load(json_file)
    logger.info(
        "No custom league dict found. You need to select leagues in %s.",
        _f_custom_league_dict,
    )
    return {}
