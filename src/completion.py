import json
from config import TODO_SAVE


def comp():
    with open(TODO_SAVE,"r", encoding="utf-8") as f:
        todos = json.load(f)

    for item in todos:
        print(f'"{item["name"]}"')
