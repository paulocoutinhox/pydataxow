import webview
from modules import config as cfg
from server import Server
from window.wpanel import WPanel
from window.wplayer import WPlayer

if __name__ == "__main__":
    Server.instance().start()

    WPanel.instance()
    WPlayer.instance()

    webview.start(
        debug=cfg.is_debug,
        http_server=True,
    )


# test
# import webview

# window1 = None
# window2 = None

# class Api1:
#     def sayHelloTo(self, name):
#         if window2:
#             window2.evaluate_js(f"document.write('Hello from {name}')")

# class Api2:
#     def sayHelloTo(self, name):
#         if window1:
#             window1.evaluate_js(f"document.write('Hello from {name}')")


# if __name__ == '__main__':
#     window1 = webview.create_window('Window #1', html='<button onclick="pywebview.api.sayHelloTo(\'window1\')">Say hello</button>', js_api=Api1())
#     window2 = webview.create_window('Window #2', html='<button onclick="pywebview.api.sayHelloTo(\'window2\')">Say hello</button>', js_api=Api2())
#     webview.start()
