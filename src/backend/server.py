import os
import threading

from flask import Flask, send_from_directory
from modules import config as cfg


class Server:
    _instance = None
    app = Flask(__name__, static_folder=os.path.join(cfg.root_dir, "gui"))
    port = 5000

    def __init__(self):
        pass

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def start(self):
        if self.app:
            threading.Thread(
                target=lambda: self.app.run(
                    port=self.port,
                    debug=False,
                ),
                daemon=True,
            ).start()

    @app.route("/panel/<path:path>")
    def serve_panel(path):
        return send_from_directory(os.path.join(cfg.root_dir, "gui/panel"), path)

    @app.route("/panel/")
    def panel_index():
        return send_from_directory(
            os.path.join(cfg.root_dir, "gui/panel"), "index.html"
        )

    @app.route("/player/<path:path>")
    def serve_player(path):
        return send_from_directory(os.path.join(cfg.root_dir, "gui/player"), path)

    @app.route("/player/")
    def player_index():
        return send_from_directory(
            os.path.join(cfg.root_dir, "gui/player"), "index.html"
        )
