import pyarr
from loguru import logger

from cloudsync.config import config


class Sonarr:
    def __init__(self) -> None:
        self.sonarr = pyarr.SonarrAPI(config["sonarr"]["host"], config["sonarr"]["api_key"])

    def connect(self):
        """Return connection to Sonarr API if credentials are valid"""
        try:
            self.sonarr.get_command()
        except pyarr.exceptions.PyarrUnauthorizedError:
            return logger.error("Can't connect to Sonarr, credentials invalid")
        return self.sonarr
