from window.wplayer import WPlayer
from window.wplayer import WPlayer


def hide():
    WPlayer.instance().destroy()


def show():
    WPlayer.instance().create()
