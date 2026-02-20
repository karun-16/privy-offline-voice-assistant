import tkinter as tk


class PrivyGUI:

    def __init__(self, root):
        self.root = root
        self.root.title("Privy Assistant")
        self.root.geometry("400x250")
        self.root.resizable(False, False)

        self.is_listening = False

        # STATUS LABEL
        self.status_label = tk.Label(
            root,
            text="Status: Idle",
            font=("Arial", 12)
        )
        self.status_label.pack(pady=10)

        # LAST COMMAND LABEL
        self.command_label = tk.Label(
            root,
            text="Last Command: None",
            font=("Arial", 10)
        )
        self.command_label.pack(pady=10)

        # START BUTTON
        self.start_button = tk.Button(
            root,
            text="Start Listening",
            width=20
        )
        self.start_button.pack(pady=5)

        # STOP BUTTON
        self.stop_button = tk.Button(
            root,
            text="Stop Listening",
            width=20
        )
        self.stop_button.pack(pady=5)

    def update_status(self, text):
        self.status_label.config(text=f"Status: {text}")

    def update_command(self, text):
        self.command_label.config(text=f"Last Command: {text}")
