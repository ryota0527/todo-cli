import sys
import json
from config import TODO_SAVE


def show(al):
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
        print("\033[33mCurrent todos:\033[0m\n")
        for c in c_todo:
            c_name = c["name"]
            c_tag = ""
            c_due = ""
            if c["tag"] != None:
                c_tag = "  Tag: " + c["tag"]

            elif c["due"] != None:
                c_due = "  Due: " + c["due"]

            print(f"- {c_name}{c_tag}{c_due}")

        if al == True:
            print("=================")
            print("\033[32mFinished:\033[0m\n")
            for f in f_todo:
                f_name = f["name"]
                f_tag = ""
                f_due = ""
                if f["tag"] != None:
                    f_tag = "  Tag: " + f["tag"]

                elif f["due"] != None:
                    f_due = "  Due: " + f["due"]

                print(f"- {f_name}{f_tag}{f_due}")


def show_sort_by_tags():
    print("coming soon")


def show_sort_by_due():
    print("coming soon")
