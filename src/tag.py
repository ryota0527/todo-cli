import json
from config import TODO_SAVE


def maketag(args):
    found = False
    with open(TODO_SAVE,"r", encoding="utf-8") as f:
        todos = json.load(f)

    names = args[:-1]
    for item in todos:
        if item["name"] in names:
            item["tag"] = args[-1]
            found = True

    if not found:
        print(f"todo {', '.join(names)} not found")
        return

    with open(TODO_SAVE,"w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=4)
