import sys
from pathlib import Path
import json
from task import make, done, undone, delete, clean, rename
from tag import maketag, rmtag
from note import note
from show import show_sort_by_tags, show_sort_by_due, show_find_tag
from due import dueset, rmdue
from completion import comp
from initialize import init
from branch import switch, show_br


def main():
    if len(sys.argv) > 1:
        command = sys.argv[1]

        if command == "init":
            init("main")

        elif command == "view":
            if len(sys.argv) > 2 and "-t" in sys.argv:
                if "-a" in sys.argv:
                    show_sort_by_tags(al=True)

                else:
                    show_sort_by_tags(al=False) 

            elif len(sys.argv) > 2 and "-f" in sys.argv:
                if "-a" in sys.argv:
                    show_find_tag(al=True, arg=sys.argv[-1])

                else:
                    show_find_tag(al=False, arg=sys.argv[-1])

            else:
                if len(sys.argv) > 2 and "-a" in sys.argv:
                    show_sort_by_due(al=True)
                
                else:
                    show_sort_by_due(al=False)

        elif command == "make":
            make(sys.argv[2:])

        elif command == "rename":
            rename(sys.argv[2], sys.argv[3])

        elif command == "del":
            delete(sys.argv[2:])

        elif command == "done":
            done(sys.argv[2:])

        elif command == "undone":
            undone(sys.argv[2:])

        elif command == "tag":
            if len(sys.argv) > 2 and "-rm" in sys.argv:
                rmtag(sys.argv[3:])

            else:
                maketag(sys.argv[2:])

        elif command == "note":
            note(sys.argv[2])

        elif command == "due":
            if len(sys.argv) > 2 and "-rm" in sys.argv:
                rmdue(sys.argv[3:])

            else:
                dueset(sys.argv[2:])

        elif command == "branch":
            if len(sys.argv) > 2:
                init(sys.argv[2])
            
            else:
                show_br()

        elif command == "switch":
            switch(sys.argv[2])

        elif command == "clean":
            clean(manual=True)

        elif command == "comp":
            comp()

    else:
        print("Usage:")
        print("  todo init")
        print("  todo make <name1>, <name2>, ...")
        print("  todo del <name1>, <name2>, ...")
        print("  todo note <name>")
        print("  todo view [-a]")
        print("  todo tag [-rm] <name> <tag>")
        print("  todo due [-rm] <name> <YYYY-MM-DD>")
        print("  todo done <name1>, <name2>, ...")
        print("  todo undone <name1>, <name2>, ...")
        print("  todo clean")


if __name__ == "__main__":
    main()
