import json
from config import TODO_SAVE, NOTES_DIR, CLEAN_NUM


def detect_sametodo(args):
    with open(TODO_SAVE,"r", encoding="utf-8") as f:
        todos = json.load(f)

    for item in todos:
        if item["name"] in args:
            raise ValueError(f"The todo '{item["name"]}' already exists.")

    else:
        pass


def make(args):
    detect_sametodo(args)

    with open(TODO_SAVE,"r", encoding="utf-8") as f:
        todo = json.load(f)

    for arg in args:
        t = {
                "name": arg,
                "due": None,
                "tag": None,
                "done": False,
                "delay": False
            }
        todo.append(t)

    with open(TODO_SAVE,"w", encoding="utf-8") as f:
        json.dump(todo, f, ensure_ascii=False, indent=4)


def done(args):
    with open(TODO_SAVE,"r", encoding="utf-8") as f:
        todos = json.load(f)

    for item in todos:
        if item["name"] in args:
            item["done"] = True

    with open(TODO_SAVE,"w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=4)


def undone(args):
    with open(TODO_SAVE,"r", encoding="utf-8") as f:
        todos = json.load(f)

    for item in todos:
        if item["name"] in args:
            item["done"] = False

    with open(TODO_SAVE,"w", encoding="utf-8") as f:
        json.dump(todos, f, ensure_ascii=False, indent=4)


def delete(args):
    new_todos = []

    with open(TODO_SAVE,"r", encoding="utf-8") as f:
        todos = json.load(f)

    for item in todos:
        if item["name"] in args:
            rmpath = NOTES_DIR / item["name"]
            if rmpath.exists():
                rmpath.unlink()
            
        else:
            new_todos.append(item)

    with open(TODO_SAVE,"w", encoding="utf-8") as f:
        json.dump(new_todos, f, ensure_ascii=False, indent=4)


def clean(manual):
    new_todo = []
    n = int(CLEAN_NUM)
    if manual == True:
        n = 0

    with open(TODO_SAVE,"r", encoding="utf-8") as f:
        todos = json.load(f)

    if len(todos) >= n:
        for item in todos:
            if item["done"] == True:
                rmpath = NOTES_DIR / item["name"]
                if rmpath.exists():
                    rmpath.unlink()
            
            elif item["done"] == False:
                new_todo.append(item)

        with open(TODO_SAVE,"w", encoding="utf-8") as f:
            json.dump(new_todo, f, ensure_ascii=False, indent=4)

    else:
        pass
