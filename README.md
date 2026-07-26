# todo-cli

This is a simple command-line todo management tool for linux environment.

## Installation

Clone this repository and run: `./install.sh`

install.sh copies the execution file named "todo" in `~/.local/bin` .
(It creates the directory before the installation if it doesn't exist)

Then you can use just by `todo init` .
To check the usage, type `todo` .

## Commands List

| command | Description |
|---------|-------------|
| `todo init` | Initialize |
| `todo view [-a]` | show current todos |
| `todo make <name>` | make a new todo |
| `todo done <name>` | mark a todo as finished |
| `todo del <name>` | remove a todo which is not finished |
| `todo cleanup` | remove finished todos |
| `todo note <todo>` | add notes in the todo (vim opens) |
| `todo tag <todo name> <tag name>` | add a tag on the todo |

(* tag feature is not completely implemented yet. wait for the next update)
