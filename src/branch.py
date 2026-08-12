from config import TODO_DIR, CURRENT_BRANCH
import json
from pathlib import Path
import shutil


HOME = Path.home()
config_path = HOME / "todo_cli" / "src" / "config.py"
branch_list = TODO_DIR / "branches.json"


def show_br():
    if branch_list.exists():
        with open(branch_list, "r", encoding="utf-8") as f:
            branches = json.load(f)

        print()
        for br in branches:
            if br == CURRENT_BRANCH:
                print(f"\033[92m{br} <- Current branch\033[0m")

            else:
                print(br)

        print()


def switch(br_name):
    if branch_list.exists():
        with open(branch_list, "r", encoding="utf-8") as f:
            branches = json.load(f)

        if str(br_name) in branches:
            pass
        
        else:
            raise ValueError(f'Branch "{br_name}" does not exist.')
    
    else:
        return

    with open(config_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    for i, line in enumerate(lines):
        if line.startswith("CURRENT_BRANCH"):
            lines[i] = f'CURRENT_BRANCH = "{br_name}"\n'

    with open(config_path, "w", encoding="utf-8") as f:
        f.writelines(lines)

    print(f'Switched to branch "{br_name}".')


def rm_branch(br_name):
    if str(br_name) == CURRENT_BRANCH:
        raise ValueError("Cannot remove the current branch.")

    if not branch_list.exists():
        return

    with open(branch_list, "r", encoding="utf-8") as f:
        branches = json.load(f)
     
    if br_name not in branches:
        raise ValueError(f'Branch "{br_name}" does not exist.')

    branches.remove(br_name)

    with open(branch_list, "w", encoding="utf-8") as f:
        json.dump(branches, f, ensure_ascii=False, indent=4)

    target = TODO_DIR / str(br_name)
    
    if target.exists():
        shutil.rmtree(target)

