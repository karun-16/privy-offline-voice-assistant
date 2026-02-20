import sys
import os
import threading
import tkinter as tk
import keyboard
import time
import ctypes

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import queue
import sounddevice as sd
import json
from vosk import Model, KaldiRecognizer

from gui.app_window import PrivyGUI
from gui.tray_icon import setup_tray
from core.command_processor import process_command
from core.app_finder import scan_apps


# -------- SINGLE INSTANCE LOCK --------
mutex = ctypes.windll.kernel32.CreateMutexW(
    None, False, "PrivyAssistantMutex_v1"
)

if ctypes.windll.kernel32.GetLastError() == 183:
    sys.exit(0)


# ---------------- QUEUES ----------------
audio_queue = queue.Queue()
command_queue = queue.Queue()


# ---------------- RESOURCE PATH ----------------
def resource_path(relative_path):
    if hasattr(sys, "_MEIPASS"):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


# ---------------- MODEL ----------------
model_path = resource_path("models/vosk-model-en-in-0.5")
model = Model(model_path)
recognizer = KaldiRecognizer(model, 16000)


# -------- SCAN INSTALLED APPS --------
scan_apps()


# ---------------- MICROPHONE CALLBACK ----------------
def callback(indata, frames, time_info, status):
    if status:
        print("Mic status:", status)
    audio_queue.put(bytes(indata))


# ---------------- COMMAND WORKER ----------------
def command_worker():
    while True:
        text = command_queue.get()
        process_command(text)
        command_queue.task_done()


threading.Thread(target=command_worker, daemon=True).start()


# ---------------- LISTENING FUNCTION ----------------
def start_listening(gui):

    if gui.is_listening:
        return

    gui.is_listening = True
    gui.update_status("Listening")

    LISTEN_TIMEOUT = 4
    start_time = time.time()

    with sd.RawInputStream(
            samplerate=16000,
            blocksize=8000,
            dtype='int16',
            channels=1,
            callback=callback):

        time.sleep(0.3)

        while gui.is_listening:

            if time.time() - start_time > LISTEN_TIMEOUT:
                break

            try:
                data = audio_queue.get(timeout=0.1)
            except queue.Empty:
                continue

            if recognizer.AcceptWaveform(data):
                result = json.loads(recognizer.Result())
                text = result.get("text", "")

                if text:
                    gui.update_command(text)
                    command_queue.put(text)
                    break

    gui.is_listening = False
    gui.update_status("Idle")


# ---------------- STOP LISTENING ----------------
def stop_listening():
    gui.is_listening = False
    gui.update_status("Idle")


# ---------------- BUTTON HANDLER ----------------
def start_button_clicked():
    threading.Thread(
        target=start_listening,
        args=(gui,),
        daemon=True
    ).start()


def hotkey_start():
    start_button_clicked()


# ---------------- GUI START ----------------
root = tk.Tk()
gui = PrivyGUI(root)

root.iconbitmap(resource_path("privy.ico"))
root.withdraw()

gui.start_button.config(command=start_button_clicked)
gui.stop_button.config(command=stop_listening)

keyboard.add_hotkey("ctrl+space", hotkey_start)


def minimize_to_tray():
    root.withdraw()


root.protocol("WM_DELETE_WINDOW", minimize_to_tray)


tray_icon = setup_tray(root)


def run_tray():
    tray_icon.run()


threading.Thread(target=run_tray, daemon=True).start()

root.mainloop()
