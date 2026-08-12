import sys
import json
from config import TODO_SAVE, CURRENT_BRANCH
from due import delay
from task import clean


def classify():
    c_todo = []
    f_todo = []

    with open(TODO_SAVE,"r", encoding="utf-8") as f:
        todos = json.load(f)

    for t in todos:
        if t["done"] == False:
            c_todo.append(t)
        
        elif t["done"] == True:
            f_todo.append(t)

    return c_todo, f_todo


def formats(c_todo, f_todo, al):
    print("=================")
    print(f"\033[92mBranch: {CURRENT_BRANCH}\033[0m")
    print("=================")
    print("\033[93mCurrent todos:\033[0m")
    for c in c_todo:
        c_name = c["name"]
        c_tag = ""
        c_due = ""
    
        if c["tag"] != None:
            c_tag = f" [ Tag: {c["tag"]} ]"

        if c["due"] != None:
            c_due = f" [ Due: {c["due"]} ]"

        if c["delay"] == True:
            print(f"- {c_name}\033[31m{c_due}\033[36m{c_tag}\033[0m")
        
        else:
            print(f"- {c_name}\033[33m{c_due}\033[36m{c_tag}\033[0m")

    print()

    if al == True:
        print("=================")
        print("\033[92mFinished:\033[0m")
        for f in f_todo:
            f_name = f["name"]
            f_tag = ""
            f_due = ""
            if f["tag"] != None:
                f_tag = f" [ Tag: {f["tag"]} ]"

            if f["due"] != None:
                f_due = f" [ Due: {f["due"]} ]"

            print(f"- {f_name}\033[32m{f_due}\033[36m{f_tag}\033[0m")

        print()


def show_sort_by_tags(al):
    delay()
    clean(manual=False)

    c_todo, f_todo = classify()

    c_todo.sort(key= lambda x: (x.get("tag") is None, x.get("tag", "")))
    f_todo.sort(key= lambda x: (x.get("tag") is None, x.get("tag", "")))

    formats(c_todo, f_todo, al)


def show_sort_by_due(al):
    delay()
    clean(manual=False)

    c_todo, f_todo = classify()

    c_todo.sort(key= lambda x: (x.get("due") is None, x.get("due", "")))
    f_todo.sort(key= lambda x: (x.get("due") is None, x.get("due", "")))

    formats(c_todo, f_todo, al)


def show_find_tag(al, arg):
    delay()
    clean(manual=False)

    c_todo = []
    f_todo = []

    with open(TODO_SAVE,"r", encoding="utf-8") as f:
        todos = json.load(f)

    for t in todos:
        if t["tag"] == arg and t["done"] == False:
            c_todo.append(t)
        
        elif t["tag"] == arg and t["done"] == True:
            f_todo.append(t)

    c_todo.sort(key= lambda x: (x.get("due") is None, x.get("due", "")))
    f_todo.sort(key= lambda x: (x.get("due") is None, x.get("due", "")))

    print("=================")
    print(f"\033[92mBranch: {CURRENT_BRANCH}\033[0m")
    print("=================")
    print(f"\033[36mTag: {arg}\033[0m\n")
    print("\033[93mCurrent todos:\033[0m")
    for c in c_todo:
        c_name = c["name"]
        c_due = ""
    
        if c["due"] != None:
            c_due = f" [ Due: {c["due"]} ]"

        if c["delay"] == True:
            print(f"- {c_name}\033[31m{c_due}\033[0m")
        
        else:
            print(f"- {c_name}\033[33m{c_due}\033[0m")

    print()

    if al == True:
        print("=================")
        print("\033[92mFinished:\033[0m")
        for f in f_todo:
            f_name = f["name"]
            f_due = ""

            if f["due"] != None:
                f_due = f" [ Due: {f["due"]} ]"

            print(f"- {f_name}\033[32m{f_due}\033[0m")

        print()


