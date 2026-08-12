from config import TODO_DIR
import json


def init(br_name):
    data_dir = TODO_DIR / br_name / "data"
    notes_dir = TODO_DIR / br_name / "notes"
    todo_save = data_dir / "todos.json"
    branch_save = TODO_DIR / "branches.json"

    data_dir.mkdir(parents=True, exist_ok=True)
    notes_dir.mkdir(parents=True, exist_ok=True)

    if not todo_save.exists():
        with open(todo_save, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4)
    
    if branch_save.exists():
        with open(branch_save, "r", encoding="utf-8") as f:
            branches = json.load(f)

    else:
        branches = []

    branches.append(br_name)

    with open(branch_save, "w", encoding="utf-8") as f:
        json.dump(branches, f, ensure_ascii=False, indent=4)

