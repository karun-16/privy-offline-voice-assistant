import pystray
from pystray import MenuItem as item
from PIL import Image
import os
import sys


def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


def create_image():
    return Image.open(resource_path("privy.ico"))


def setup_tray(root):

    def show_window(icon, item):
        root.after(0, root.deiconify)
        root.after(0, root.lift)

    def exit_app(icon, item):
        icon.stop()
        root.after(0, root.quit)

    menu = pystray.Menu(
        item("Open Privy", show_window),
        item("Exit", exit_app),
    )

    icon = pystray.Icon(
        "Privy",
        create_image(),
        "Privy Assistant",
        menu
    )

    return icon
