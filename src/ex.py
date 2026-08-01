import sys
from pathlib import Path
import json
from config import HOME, TODO_SAVE, DATA_DIR, NOTES_DIR
from task import make, done, delete, clean
from tag import maketag
from note import note
from show import show, show_sort_by_tags, show_sort_by_due
from due import dueset
from completion import comp


def main():
    if len(sys.argv) > 1:
        command = sys.argv[1]

        if command == "init":
            DATA_DIR.mkdir(parents=True, exist_ok=True)
            NOTES_DIR.mkdir(parents=True, exist_ok=True)

            if not TODO_SAVE.exists():
                with open(TODO_SAVE, "w", encoding="utf-8") as f:
                    json.dump([], f, indent=4)

        elif command == "view":
            if len(sys.argv) > 2 and sys.argv[2] == "-a":
                show(al=True)

            else:
                show(al=False)

        elif command == "make":
            make(sys.argv[2:])

        elif command == "del":
            delete(sys.argv[2:])

        elif command == "done":
            done(sys.argv[2:])

        elif command == "tag":
            maketag(sys.argv[2:])

        elif command == "note":
            note(sys.argv[2])

        elif command == "due":
            dueset(sys.argv[2:])

        elif command == "comp":
            comp()

    else:
        print("Usage:")
        print("  todo init")
        print("  todo make <name1>, <name2>, ...")
        print("  todo del <name1>, <name2>, ...")
        print("  todo note <name>")
        print("  todo view [-a]")
        print("  todo tag <name> <tag>")
        print("  todo due <name> <YYYY-MM-DD>")
        print("  todo done <name1>, <name2>, ...")


if __name__ == "__main__":
    main()
