import os

from loguru import logger


class Rclone:
    def move(self, source_path: str, destination_path: str) -> None:
        args = [
            "gclone",
            "move",
            "-P",
            "--no-traverse",
            "--fast-list",
            "--max-backlog=999999",
            "--drive-chunk-size=512M",
            "--transfers=4",
            "--checkers=16",
            "--buffer-size=75M",
            "--exclude",
            "'_UNPACK_**'",
            "--ignore-existing",
            source_path,
            destination_path,
        ]
        logger.debug(f"Move operation: {' '.join(args)}")
        os.system(" ".join(args))

    def move_server_side(self, source_path: str, destination_path: str) -> None:
        args = [
            "gclone",
            "move",
            source_path,
            destination_path,
            "-P",
            "--drive-server-side-across-configs",
            "--no-traverse",
            "--delete-empty-src-dirs",
        ]
        logger.debug(f"Move server side operation: {' '.join(args)}")
        os.system(" ".join(args))
