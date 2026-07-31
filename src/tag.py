import json
from config import TODO_SAVE


def maketag(args):
    with open(TODO_SAVE,"r", encoding="utf-8") as f:
        todos = json.load(f)

    name = args[0]
    for item in todos:
        if item["name"] == name:
            item["tag"] = args[1]
            break

    else:
        print(f"todo {name} not found")
        return

    with open(TODO_SAVE,"w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=4)
