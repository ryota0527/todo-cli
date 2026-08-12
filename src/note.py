import sys
import json
from config import HOME, TODO_SAVE, NOTES_DIR ,EDITOR_FOR_NOTES
import subprocess


def note(arg):
    with open(TODO_SAVE,"r", encoding="utf-8") as f:
        todos = json.load(f)

    for item in todos:
        if item["name"] == arg:
            break

    else:
        print(f"todo {arg} not found")
        return

    name = arg + ".md"
    path = NOTES_DIR / name
    path.touch(exist_ok=True)

    subprocess.run([EDITOR_FOR_NOTES, str(path)])

