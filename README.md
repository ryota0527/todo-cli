# todo-cli

This is a simple command-line todo management tool for linux environment.

## Installation

Clone this repository and run: `./install.sh`

install.sh copies the execution file named "todo" in `~/.local/bin` .<br>
(It creates the directory before the installation if it doesn't exist)

Then you can use just by `todo init` .<br>
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

## Examples
Initialize: `todo init`

Add a todo "read an article": `todo make "read an article"`<br>
(*Use quotation mark for todo's name, if it contains space!)

View: `todo view`<br>
(Output: `-read an article`)

Add the link to the article as notes: `todo note "read an article"`<br>
(One can paste the link in the todo file)
