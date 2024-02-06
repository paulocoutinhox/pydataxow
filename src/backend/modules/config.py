import os
import sys

# window
is_debug = True if os.environ.get("PYWEBVIEW_DEBUG") == "1" else False

# root path
if getattr(sys, "frozen", False) and hasattr(sys, "_MEIPASS"):
    # frozen executable path
    root_dir = os.path.join(sys._MEIPASS)
else:
    # normal path
    root_dir = os.path.abspath(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..")
    )

# server
server_host = "0.0.0.0"
server_port = 5151

# gui
gui_panel_dir = os.path.join(root_dir, "gui", "panel")
gui_player_dir = os.path.join(root_dir, "gui", "player")
gui_rcontrol_dir = os.path.join(root_dir, "gui", "rcontrol")

# url
panel_url = f"http://127.0.0.1:{server_port}/panel"
player_url = f"http://127.0.0.1:{server_port}/player"
rcontrol_url = f"http://[ip]:{server_port}/rcontrol?api_url=http://[ip]:{server_port}"

if is_debug:
    panel_url = "http://localhost:8080"
    player_url = "http://localhost:8081"
    rcontrol_url = f"http://[ip]:8082?api_url=http://[ip]:{server_port}"
