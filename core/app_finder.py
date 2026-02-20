import os
from pathlib import Path
from difflib import get_close_matches
import win32com.client


APP_CACHE = {}
APP_ALIASES = {
    "vscode": "visual studio code",
    "vs code": "visual studio code",
    "code": "visual studio code",
    "whatsapp": "whatsapp",
    "spotify": "spotify",
}


# ---------------------------------------------------
# START MENU PATHS
# ---------------------------------------------------
def get_start_menu_paths():
    return [
        r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs",
        str(Path.home() /
            r"AppData\Roaming\Microsoft\Windows\Start Menu\Programs")
    ]


# ---------------------------------------------------
# SCAN START MENU SHORTCUTS
# ---------------------------------------------------
def scan_start_menu():

    shell = win32com.client.Dispatch("WScript.Shell")

    for base_path in get_start_menu_paths():

        if not os.path.exists(base_path):
            continue

        for root, _, files in os.walk(base_path):
            for file in files:

                if not file.lower().endswith(".lnk"):
                    continue

                full_path = os.path.join(root, file)

                try:
                    shortcut = shell.CreateShortCut(full_path)
                    target = shortcut.Targetpath.lower()

                    # ignore browser shortcuts
                    if "chrome.exe" in target or \
                       "msedge.exe" in target:
                        continue

                except:
                    continue

                name = file.replace(".lnk", "").lower()
                APP_CACHE[name] = ("shortcut", full_path)


# ---------------------------------------------------
# SCAN WINDOWS STORE APPS (AppsFolder)
# ---------------------------------------------------
def scan_store_apps():

    shell = win32com.client.Dispatch("Shell.Application")
    apps_folder = shell.NameSpace("shell:AppsFolder")

    for item in apps_folder.Items():

        name = item.Name.lower()
        app_id = item.Path

        APP_CACHE[name] = ("uwp", app_id)


# ---------------------------------------------------
# MAIN SCAN FUNCTION
# ---------------------------------------------------
def scan_apps():
    APP_CACHE.clear()

    scan_start_menu()
    scan_store_apps()

    print(f"Indexed {len(APP_CACHE)} applications.")


# ---------------------------------------------------
# FIND APP
# ---------------------------------------------------
def find_app(app_name):

    app_name = app_name.lower().strip()

    if app_name in APP_ALIASES:
        app_name = APP_ALIASES[app_name]

    # exact
    if app_name in APP_CACHE:
        return APP_CACHE[app_name]

    # partial
    for name in APP_CACHE:
        if app_name in name:
            return APP_CACHE[name]

    # fuzzy
    matches = get_close_matches(
        app_name,
        APP_CACHE.keys(),
        n=1,
        cutoff=0.6
    )

    if matches:
        return APP_CACHE[matches[0]]

    return None
