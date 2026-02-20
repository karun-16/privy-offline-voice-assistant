import os
import webbrowser
from pathlib import Path
import pyttsx3
from core.app_finder import find_app


# ==================================================
# SAFE WINDOWS ALIASES
# ==================================================
SAFE_WINDOWS_ALIASES = {
    "spotify",
    "code",
    "vscode",
    "notepad",
    "calc",
    "calculator",
    "powershell",
    "cmd",
}


# ==================================================
# TEXT TO SPEECH ENGINE
# ==================================================
engine = pyttsx3.init()

voices = engine.getProperty("voices")
engine.setProperty("voice", voices[0].id)
engine.setProperty("rate", 170)


def speak(text):
    engine.stop()
    engine.say(text)
    engine.runAndWait()


# ==================================================
# RESPONSES
# ==================================================
RESPONSES = {
    "open_app": "Opening",
    "open_website": "Opening",
    "open_folder": "Opening",
    "create_note": "Saved",
    "search": "Searching",
    "unknown": "Sorry",
}


# ==================================================
# EXECUTE ACTION
# ==================================================
def execute(intent, value):

    try:

        # ==================================================
        # OPEN APPLICATION
        # ==================================================
        if intent == "open_app":

            value = value.lower().strip()

            # ---------- HARDCODED APPS ----------
            if value == "chrome":
                speak(RESPONSES["open_app"])
                os.startfile(
                    r"C:\Program Files\Google\Chrome\Application\chrome.exe"
                )
                return

            elif value in ["calculator", "calc"]:
                speak(RESPONSES["open_app"])
                os.system("start calc")
                return

            elif value == "notepad":
                speak(RESPONSES["open_app"])
                os.system("start notepad")
                return

            elif value == "settings":
                speak(RESPONSES["open_app"])
                os.system("start ms-settings:")
                return

            elif value == "camera":
                speak(RESPONSES["open_app"])
                os.system("start microsoft.windows.camera:")
                return


            # ---------- APP FINDER (NEW STRUCTURE) ----------
            app_info = find_app(value)

            if app_info:

                app_type, app_target = app_info

                speak(RESPONSES["open_app"])

                # Start Menu shortcut
                if app_type == "shortcut":
                    print(f"Opening {value} via shortcut")
                    os.startfile(app_target)
                    return

                # Microsoft Store / UWP app
                elif app_type == "uwp":
                    print(f"Opening {value} via AppsFolder")
                    os.system(
                        f'explorer shell:AppsFolder\\{app_target}'
                    )
                    return


            # ---------- SAFE WINDOWS ALIAS ----------
            if value in SAFE_WINDOWS_ALIASES:
                speak(RESPONSES["open_app"])
                os.system(f'start "" "{value}"')
                return


            # ---------- SPECIAL FALLBACK ----------
            if value == "whatsapp":
                speak("Opening WhatsApp Web")
                webbrowser.open("https://web.whatsapp.com")
                return


            # ---------- FAIL ----------
            speak("Application not found")
            return


        # ==================================================
        # OPEN WEBSITE
        # ==================================================
        elif intent == "open_website":

            if value == "youtube":
                speak(RESPONSES["open_website"])
                webbrowser.open("https://www.youtube.com")
            else:
                speak(RESPONSES["unknown"])


        # ==================================================
        # OPEN FOLDER
        # ==================================================
        elif intent == "open_folder":

            if value == "downloads":
                speak(RESPONSES["open_folder"])
                downloads = str(Path.home() / "Downloads")
                os.startfile(downloads)
            else:
                speak(RESPONSES["unknown"])


        # ==================================================
        # CREATE NOTE
        # ==================================================
        elif intent == "create_note":

            if value:
                with open("data/notes.txt", "a", encoding="utf-8") as f:
                    f.write(value + "\n")

                speak(RESPONSES["create_note"])
            else:
                speak(RESPONSES["unknown"])


        # ==================================================
        # SEARCH INTERNET
        # ==================================================
        elif intent == "search":

            if value:
                speak(RESPONSES["search"])
                webbrowser.open(
                    f"https://www.google.com/search?q={value}"
                )
            else:
                speak(RESPONSES["unknown"])


        # ==================================================
        # UNKNOWN
        # ==================================================
        else:
            speak(RESPONSES["unknown"])

    except Exception as e:
        print("Error executing command:", e)
        speak("Error")
