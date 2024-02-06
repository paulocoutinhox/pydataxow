import os
import sys

# window
is_debug = True if os.environ.get("PYWEBVIEW_DEBUG") == "1" else False

# root path
if getattr(sys, "frozen", False):
    # frozen executable path
    root_dir = os.path.join(sys._MEIPASS)
else:
    # normal path
    root_dir = os.path.abspath(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..")
    )

# gui
gui_panel_dir = os.path.join(root_dir, "gui", "panel")
gui_player_dir = os.path.join(root_dir, "gui", "player")

# url
panel_url = "http://127.0.0.1:5000/panel/index.html"
player_url = "http://127.0.0.1:5000/player/index.html"

if is_debug:
    panel_url = "http://localhost:8080/index.html"
    player_url = "http://localhost:8081/index.html"
