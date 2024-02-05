import webview


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

    def create(cls):
        if WPlayer.window is None:
            WPlayer.window = webview.create_window(
                "Player",
                html="<button onclick=\"pywebview.api.sayHelloTo('window2')\">Say hello</button>",
                hidden=True,
                frameless=True,
            )

            WPlayer.window.events.closed += cls.on_closed

        WPlayer.window.show()

    def destroy(cls):
        if WPlayer.window:
            WPlayer.window.destroy()

        WPlayer.window = None

    def on_closed(cls):
        WPlayer.window = None
