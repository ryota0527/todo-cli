from config import TODO_DIR, CURRENT_BRANCH
import json


branch_list = TODO_DIR / "branches.json"


def show_br():
    if branch_save.exists():
        with open(branch_save, "r", encoding="utf-8") as f:
            branches = json.load(f)

        print()
        for br in branches:
            if br == CURRENT_BRANCH:
                print(f"\033[92m{br} <- Current branch\033[0m")

            else:
                print(br)

        print()


def switch(br_name):
    if branch_save.exists():
        with open(branch_save, "r", encoding="utf-8") as f:
            branches = json.load(f)

        if str(br_name) in branches:
            pass
        
        else:
            raise ValueError(f'Branch "{br_name}" does not exist.')
    
    else:
        return

    with open("config.py", "r", encoding="utf-8") as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if line.startswith("CURRENT_BRANCH"):
            lines[i] = f'CURRENT_BRANCH = "{br_name}"\n'

    with open("config.py", "w", encoding="utf-8") as f:
        f.writelines(lines)

    print(f'Switched to branch "{br_name}".')
