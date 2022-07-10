from flask import Flask, request

from cloudsync import config, qbittorrent, rclone
import cloudsync.sonarr

app = Flask(__name__)


@app.route("/")
def index():
    sonarr = cloudsync.sonarr.Sonarr().connect()
    return "Hello, world!", 200


@app.route("/connect", methods=["POST"])
def connect():
    data = request.json
    return "OK", 200


if __name__ == "__main__":
    app.run()
