import json


def comp():
    with open(TODO_SAVE,"r", encoding="utf-8") as f:
        todos = json.load(f)

    for item in todos:
        print(item["name"])
