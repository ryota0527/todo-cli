#!/bin/bash

set -e

mkdir -p "$HOME/.local/bin"
mkdir -p "$HOME/todo_cli"

#install
cp -r ./src "$HOME/todo_cli/src"
cp ./todo "$HOME/.local/bin/todo"
chmod +x "$HOME/.local/bin/todo"

case ":$PATH:" in
    *":$HOME/.local/bin:"*)
        ;;
    *)
        echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
        ;;
esac


echo "Installation completed."
echo "Run: source ~/.bashrc"
echo "Then you can use: todo init"
