import webview
from modules import config as cfg
from modules import net


def get_settings():
    network_address = net.get_network_ip()

    data = {
        "network": {
            "address": net.get_network_ip(),
            "rcontrol_url": cfg.rcontrol_url.replace("[ip]", network_address),
        }
    }

    return data


def select_folder():
    dirs = webview.windows[0].create_file_dialog(webview.FOLDER_DIALOG)

    if dirs and len(dirs) > 0:
        directory = dirs[0]

        if isinstance(directory, bytes):
            directory = directory.decode("utf-8")

        response = "Selected: {0}".format(directory)
    else:
        response = "Canceled"

    return response


def toggle_fullscreen():
    webview.windows[0].toggle_fullscreen()
    return "OK"
