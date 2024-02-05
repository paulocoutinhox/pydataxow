import api
import webview
from modules import config as cfg


class WPanel:
    _instance = None
    window: webview.Window = None
    api = api.API()

    def __init__(self):
        self.window = webview.create_window(
            "DataXow",
            url=cfg.panel_url,
            js_api=self.api,
            min_size=(800, 600),
        )

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls()
        return cls._instance
