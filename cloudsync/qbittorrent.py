import qbittorrentapi
from loguru import logger

from cloudsync.config import config


class qBittorrent:
    def __init__(self) -> None:
        self.qbit = qbittorrentapi.Client(
            host=config["qbittorrent"]["host"],
            username=config["qbittorrent"]["username"],
            password=config["qbittorrent"]["password"],
        )

    def connect(self):
        """Return connection to qBittorrent API if credentials are valid"""
        try:
            self.qbit.auth_login()
        except qbittorrentapi.LoginFailed:
            return logger.error("qBittorrent credentials invalid, exiting")
        return self.qbit
