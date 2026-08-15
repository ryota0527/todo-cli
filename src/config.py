from pathlib import Path


#settings for datasaving
HOME = Path.home()
TODO_DIR = HOME / ".todo_cli"

CURRENT_BRANCH = "main"

DATA_DIR = TODO_DIR / CURRENT_BRANCH / "data"
NOTES_DIR = TODO_DIR / CURRENT_BRANCH / "notes"

TODO_SAVE = DATA_DIR / "todos.json"

#settings for notes
EDITOR_FOR_NOTES = "vim"

#settings for clean command
CLEAN_NUM = 15
