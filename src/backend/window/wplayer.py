import json

import webview
from modules import config as cfg


class WPlayer:
    _instance = None
    window: webview.Window = None

    def __init__(self):
        pass

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance

    def create(self):
        if self.window is None:
            self.window = webview.create_window(
                "Player",
                url=cfg.player_url,
                hidden=True,
                frameless=True,
            )

            self.window.events.closed += self.on_closed

        self.window.show()

    def destroy(self):
        if self.window:
            self.window.destroy()

        self.window = None

    def on_closed(self):
        self.window = None

    def update_data(self, params):
        if self.window:
            params_json = json.dumps(json.dumps(params))
            js_code = f"updateData(JSON.parse({params_json}));"

            self.window.evaluate_js(js_code)
