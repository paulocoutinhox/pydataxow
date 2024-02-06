import os
import threading

from api import API
from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
from modules import config as cfg


class Server:
    _instance = None
    app = Flask(__name__, static_folder=os.path.join(cfg.root_dir, "gui"))

    def __init__(self):
        CORS(self.app)

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def start(self):
        if self.app:
            threading.Thread(
                target=lambda: self.app.run(
                    host=cfg.server_host,
                    port=cfg.server_port,
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

    @app.route("/rcontrol/<path:path>")
    def serve_rcontrolr(path):
        return send_from_directory(os.path.join(cfg.root_dir, "gui/rcontrol"), path)

    @app.route("/rcontrol/")
    def rcontrol_index():
        return send_from_directory(
            os.path.join(cfg.root_dir, "gui/rcontrol"), "index.html"
        )

    @app.route("/module/call", methods=["POST"])
    def module_call_api():
        data = request.get_json(silent=True)

        if type(data) is dict:
            func = data.get("func")
            params = data.get("params") if "params" in data else None

            if func:
                result = API().call(func, params)

                return jsonify({"result": result})
            else:
                return jsonify({"error": "Function name not provided in JSON data."})
        else:
            return jsonify({"error": "Invalid data."})
