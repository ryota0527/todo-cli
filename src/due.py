import json
from datetime import date, datetime
from config import TODO_SAVE


def dueset(args):
    with open(TODO_SAVE,"r", encoding="utf-8") as f:
        todos = json.load(f)

    name = args[0]

    try:
        due = datetime.strptime(args[1], "%Y-%m-%d").date()

    except ValueError:
        print("Due date should be YYYY-MM-DD")
        return

    for item in todos:
        if item["name"] == name:
            item["due"] = str(due)
            break

    else:
        print(f"todo {name} not found")
        return

    with open(TODO_SAVE,"w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=4)


def delay():
    with open(TODO_SAVE,"r", encoding="utf-8") as f:
        todos = json.load(f)

    today = date.today()

    for item in todos:
        if item["due"] != None:
            due = datetime.strptime(item["due"], "%Y-%m-%d").date()
            if due < today :
                item["delay"] = True

    with open(TODO_SAVE,"w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=4)
