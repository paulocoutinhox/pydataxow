import socket

import requests


def open_url(params):
    r = requests.get(url=params["url"])

    return "Status code: {0}".format(
        r.status_code,
    )


def get_network_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(("10.255.255.255", 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = "127.0.0.1"
    finally:
        s.close()
    return IP
