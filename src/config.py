from pathlib import Path

HOME = Path.home()
TODO_DIR = HOME / "todo_cli"
DATA_DIR = TODO_DIR / "data"
NOTES_DIR = TODO_DIR / "notes"

TODO_SAVE = DATA_DIR / "todos.json"

EDITOR_FOR_NOTES = "vim"
