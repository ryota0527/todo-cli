from config import TODO_SAVE, DATA_DIR, NOTES_DIR
import json


def init():
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    NOTES_DIR.mkdir(parents=True, exist_ok=True)

    if not TODO_SAVE.exists():
        with open(TODO_SAVE, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4)
