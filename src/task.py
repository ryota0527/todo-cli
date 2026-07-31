import json
import sys
from config import TODO_SAVE


def make():
    with open(TODO_SAVE,"r", encoding="utf-8") as f:
        todo = json.load(f)

    for arg in sys.argv:
        t = {
                "name": arg,
                "due": None,
                "tag": None,
                "note": None,
                "done": False
            }
        todo.append(t)

    with open(TODO_SAVE,"w", encoding="utf-8") as f:
        json.dump(todo, f, ensure_ascii=False, indent=4)


def done():
    with open(TODO_SAVE,"r", encoding="utf-8") as f:
        todos = json.load(f)

    for arg in sys.argv:
        for item in todos:
            if item["name"] == arg:
                item["done"] = True
                break

        else:
            print(f"todo {arg} not found")


    with open(TODO_SAVE,"w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=4)


def delete():
    new_todos = []

    with open(TODO_SAVE,"r", encoding="utf-8") as f:
        todos = json.load(f)

    for arg in sys.argv:
        for item in todos:
            if item["name"] == arg:
                continue
            
            else:
                new_todos.append(item)

    with open(TODO_SAVE,"w", encoding="utf-8") as f:
        json.dump(new_todos, f, ensure_ascii=False, indent=4)


def clean():
    with open(TODO_SAVE,"r", encoding="utf-8") as f:
        todos = json.load(f)

    if len(todos) == 100:
        t = [item for item in todos if not item["done"]]

        with open(TODO_SAVE,"w", encoding="utf-8") as f:
            json.dump(t, f, ensure_ascii=False, indent=4)

    else:
        pass 

    print("Finished tasks deleted")

