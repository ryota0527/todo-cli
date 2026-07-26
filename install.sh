#!/bin/bash

set -e

mkdir -p "$HOME/.local/bin"

#install
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
