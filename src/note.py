import sys
import json
from config import HOME, TODO_SAVE
import subprocess


def note(arg):
    with open(TODO_SAVE,"r", encoding="utf-8") as f:
        todos = json.load(f)

    name = arg
    for item in todos:
        if item["name"] == name:
            break

    else:
        print(f"todo {name} not found")
        return

    path = f"{HOME}/todo_cli/notes/{name}"
    subprocess.run(["vim", str(path)])
