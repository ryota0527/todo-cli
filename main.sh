#!/bin/bash

todo() {
    if [[ $1 == "init" ]]; then
        mkdir -p ~/todo_cli/todo
        mkdir -p ~/todo_cli/finished

    elif [[ $1 == "make" ]]; then
        touch ~/todo_cli/todo/-"$2"

    elif [[ $1 == "del" ]]; then
        rm ~/todo_cli/todo/-"$2"

    elif [[ $1 == "note" ]]; then
        vim ~/todo_cli/todo/-"$2"

    elif [[ $1 == "view" ]]; then
        if [[ $2 == "-a" ]]; then
            tree ~/todo_cli/
        else
            ls ~/todo_cli/todo/
        fi

    elif [[ $1 == "tag" ]]; then
        sed -i "1s|.*|#tag: $3|" ~/todo_cli/todo/-"$2"

    elif [[ $1 == "done" ]]; then
        mv ~/todo_cli/todo/-"$2" ~/todo_cli/fin/-"$2"

    elif [[ $1 == "cleanup" ]]; then
        rm -f ~/todo_cli/fin/*
    else
        echo "Usage:"
        echo "  todo init"
        echo "  todo make <name>"
        echo "  todo del <name>"
        echo "  todo note <name>"
        echo "  todo view [-a]"
        echo "  todo tag <name> <tag>"
        echo "  todo done <name>"
        echo "  todo cleanup #delete finished todos"
    fi
}

todo "$@"
