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


# from flask import Flask, send_from_directory
# import threading
# import webview
# import os
# from modules import config as cfg

# app = Flask(__name__)

# def serve_static(directory):
#     directory_path = os.path.join(cfg.root_dir, f'gui/{directory}')

#     # Função para servir arquivos dentro do diretório
#     def dynamic_serve_file(file_path):
#         return send_from_directory(directory_path, file_path)

#     # Função para servir o index.html por padrão
#     def dynamic_serve_index():
#         return send_from_directory(directory_path, 'index.html')

#     # Atribuição de nomes únicos para as funções de visualização
#     dynamic_serve_file.__name__ = f'serve_file_{directory}'
#     dynamic_serve_index.__name__ = f'serve_index_{directory}'

#     # Criação de rotas dinamicamente
#     app.add_url_rule(f'/{directory}/<path:file_path>', view_func=dynamic_serve_file)
#     app.add_url_rule(f'/{directory}/', view_func=dynamic_serve_index)

# def start_flask():
#     app.run(port=5000, debug=True)

# if __name__ == '__main__':
#     # Configuração das rotas estáticas
#     serve_static('panel')
#     serve_static('player')

#     # Iniciar Flask em um thread secundário
#     flask_thread = threading.Thread(target=start_flask, daemon=True)
#     flask_thread.start()

#     # Configuração e inicialização das janelas do pywebview no thread principal
#     url_panel = "http://localhost:5000/panel/"
#     url_player = "http://localhost:5000/player/"
#     window1 = webview.create_window('Window #1', url_panel)
#     window2 = webview.create_window('Window #2', url_player)
#     webview.start(debug=False)
