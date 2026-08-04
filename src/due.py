import json
from datetime import date, datetime
from config import TODO_SAVE


def dueset(args):
    found = False
    with open(TODO_SAVE,"r", encoding="utf-8") as f:
        todos = json.load(f)

    names = args[:-1]

    try:
        due = datetime.strptime(args[-1], "%Y-%m-%d").date()

    except ValueError:
        print("Due date should be YYYY-MM-DD")
        return

    for item in todos:
        if item["name"] in names:
            item["due"] = str(due)
            found = True

    if not found:
        print(f"todo {', '.join(names)} not found")
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
