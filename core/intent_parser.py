def parse_command(text):

    text = text.lower().strip()

    # ---------- OPEN WEBSITE ----------
    # Website rules MUST come before open_app
    # otherwise "open youtube" becomes open_app
    if "youtube" in text:
        return "open_website", "youtube"

    # ---------- OPEN APPLICATION ----------
    if text.startswith("open "):
        value = text.replace("open", "", 1).strip()
        return "open_app", value

    # ---------- OPEN FOLDER ----------
    if "downloads" in text:
        return "open_folder", "downloads"

    # ---------- CREATE NOTE ----------
    if text.startswith("create note"):
        value = text.replace("create note", "", 1).strip()
        return "create_note", value

    # ---------- SEARCH ----------
    if text.startswith("search"):
        value = text.replace("search", "", 1).strip()
        return "search", value

    # ---------- UNKNOWN ----------
    return "unknown", text
