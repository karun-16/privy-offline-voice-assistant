from core.intent_parser import parse_command
from actions.system_actions import execute


# ---------- CLEAN TEXT ----------
def clean_text(text):

    text = text.lower().strip()

    # remove filler phrases
    fillers = [
        "please",
        "can you",
        "could you",
        "for me",
        "i think",
        "hey",
        "privy",
    ]

    for f in fillers:
        text = text.replace(f, "")

    # remove multiple spaces
    text = " ".join(text.split())

    # remove repeated words (open open spotify → open spotify)
    words = text.split()
    cleaned = []

    for w in words:
        if not cleaned or cleaned[-1] != w:
            cleaned.append(w)

    text = " ".join(cleaned)

    return text.strip()


# ---------- PROCESS COMMAND ----------
def process_command(text):

    cleaned_text = clean_text(text)

    print("Cleaned:", cleaned_text)

    intent, value = parse_command(cleaned_text)

    print("Intent:", intent, "| Value:", value)

    execute(intent, value)
