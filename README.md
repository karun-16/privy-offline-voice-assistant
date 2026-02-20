# 🎙️ Privy — Offline Voice Assistant (V1)

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Status](https://img.shields.io/badge/status-active%20development-green)
![Platform](https://img.shields.io/badge/platform-Windows-lightgrey)


Privy is a fully offline desktop voice assistant built to demonstrate privacy-first AI interaction without relying on cloud services.
It performs speech recognition locally and executes system-level actions while maintaining complete user data privacy.

---

## 🚀 Why Privy?

Most voice assistants depend on internet connectivity and cloud processing.
Privy explores an alternative approach:

* No cloud dependency
* Local speech processing
* Fast response time
* Privacy-first architecture

---

## ✨ Features (V1)

* 🎤 Offline speech recognition using Vosk
* 💻 Windows desktop assistant interface
* ⚡ Quick application launching
* 🧠 Command execution framework
* 🖥️ GUI with listening & response states
* 📦 Windows installer via Inno Setup

---

## 🧠 How Privy Works

1. 🎤 Microphone captures user speech
2. 🔊 Audio processed locally using Vosk speech recognition
3. 🧩 Recognized text mapped to command intents
4. ⚙️ Corresponding action executed on system
5. 💬 Assistant feedback displayed via GUI

This pipeline enables a complete offline interaction loop.

---

## 🧭 Architecture

```
User Speech
    ↓
🎤 Microphone Capture
    ↓
🧠 Vosk Speech Recognition
    ↓
🧩 Command / Intent Mapping
    ↓
⚙️ Action Execution Engine
    ↓
🖥️ GUI Feedback & Status Update
```

This pipeline represents the offline interaction loop powering Privy.

## 🏗️ Project Structure

```
Privy/
 ├── core/        → assistant logic & orchestration
 ├── actions/     → executable commands
 ├── gui/         → desktop interface
 ├── data/        → assistant resources
 ├── main.py      → entry point
```

---
## 🎬 Demo Video

[![Privy V1 Demo](https://img.youtube.com/vi/4h9gGLNob_Y/0.jpg)](https://youtu.be/4h9gGLNob_Y)

*Click the thumbnail above to watch the demo.*


## 📸 Demo

### Idle State

![Idle](screenshots/screenshot1.png)

### Listening State

![Listening](screenshots/screenshot2.png)

### Real Usage Example

![Usage](screenshots/screenshot3.png)

---

## 📦 Installation

### Option 1 — Installer (Recommended)

Download the installer from the **Releases** section and run setup.

### Option 2 — Run from source

```
git clone https://github.com/karun-16/privy-offline-voice-assistant
cd privy-offline-voice-assistant
pip install -r requirements.txt
python main.py
```

---

## 🛠️ Tech Stack

* Python
* Vosk (Offline Speech Recognition)
* Tkinter (GUI)
* Inno Setup (Installer Packaging)

---

## 🗺️ Roadmap

### ✅ V1 — Windows Offline Assistant

* Core assistant engine
* Offline speech pipeline
* Desktop GUI
* Installer packaging

### 🔄 V2 — Android Port

* Core engine adaptation
* Mobile audio pipeline
* Background assistant service

### 🚀 V3 — Optimization & Expansion

* Performance improvements
* Extended command set
* Modular plugin architecture
* Enhanced conversational flow

---

## 🤝 Contribution

This project is currently under active development.
Ideas, feedback, and improvements are welcome.

---

## 📜 License

This project is licensed under the MIT License.

---

⭐ If you find this project interesting, consider starring the repository.
