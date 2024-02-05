import os

# window
is_debug = True if os.environ.get("PYWEBVIEW_DEBUG") == "1" else False

# development path
root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

# frozen executable path
if not os.path.exists(root_dir):
    root_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)))

# gui
gui_panel_dir = os.path.join(root_dir, "gui", "panel")
gui_player_dir = os.path.join(root_dir, "gui", "player")

# url
panel_url = os.path.abspath(os.path.join(gui_panel_dir, "index.html"))
player_url = os.path.abspath(os.path.join(gui_player_dir, "index.html"))

if is_debug:
    panel_url = "http://localhost:8080/index.html"
    player_url = "http://localhost:8081/index.html"