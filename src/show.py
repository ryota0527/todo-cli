import sys
import json
from config import TODO_SAVE
from due import delay
from task import clean


def show(al):
    delay()
    clean()

    c_todo = []
    f_todo = []

    with open(TODO_SAVE,"r", encoding="utf-8") as f:
        todos = json.load(f)

    for t in todos:
        if t["done"] == False:
            c_todo.append(t)
        
        elif t["done"] == True:
            f_todo.append(t)

    print("=================")
    print("\033[33mCurrent todos:\033[0m")
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
    
    print("\n")

    if al == True:
        print("=================")
        print("\033[32mFinished:\033[0m")
        for f in f_todo:
            f_name = f["name"]
            f_tag = ""
            f_due = ""
            if f["tag"] != None:
                f_tag = f" [ Tag: {f["tag"]} ]"

            elif f["due"] != None:
                f_due = f" [ Due: {f["due"]} ]"

            print(f"- {f_name}\033[32m{f_due}\033[36m{f_tag}\033[0m")

        print("\n")


def show_sort_by_tags():
    print("coming soon")


def show_sort_by_due():
    print("coming soon")
