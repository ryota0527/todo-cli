from pathlib import Path
from init import init


def link():
    config_path = Path.home() / "todo_cli" / "src" / "config.py"
    linkdir = Path(input("Enter the path to the directory where todos are saved:"))
    if linkdir.exists():
        lines = config_path.read_text(encoding="utf-8").splitlines()

        for i, line in enumerate(lines):
            if line.startswith("TODO_SAVE ="):
                old_todosave = lines[i].split("=", 1)[1].strip()
                lines[i] = f'TODO_SAVE = Path(r"{linkdir}") / "todo_cli"'

        linkdir.write_text("\n".join(lines) + "\n", encoding="utf-8")

    else:
        raise ValueError("Directory not found.")

    init()

    if old_todosave.exists():
        

