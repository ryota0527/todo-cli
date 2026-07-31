# todo-cli

This is a simple command-line todo management tool for linux environment.

## Requirements
python > 3.8 is recommended.

## Installation

Clone this repository and run: `./install.sh`

Then you can use just by `todo init` .<br>
To check the usage, type `todo` .

## Commands List

| command | Description |
|---------|-------------|
| `todo init` | Initialize |
| `todo view [-a]` | show current todos |
| `todo make <name1>, <name2>, ...` | make a new todo |
| `todo done <name1>, <name2>, ...` | mark a todo as finished |
| `todo del <name1>, <name2>, ...` | remove a todo which is not finished |
| `todo note <todo>` | add notes in the todo (vim opens) |
| `todo tag <todo name> <tag name>` | add a tag on the todo |
| `todo due <todo name> <YYYY-MM-DD>` | set a due date |

## Examples
- Initialize: `todo init`

- Add a todo "read an article": `todo make "read an article"`<br>
(*Use quotation mark for todo's name, if it contains space!)

- View: `todo view`<br>
(Output: `- read an article`)

- Set the due date: `todo due "read an article" 2026-08-01`

- Add a tag: `todo tag "read an article" research`

- View again: `todo view`<br>
(Output: `- read an article  Tag: research  Due: 2026-08-01`

- Add the link to the article as notes: `todo note "read an article"`<br>
(One can paste the link in the todo file)

- Mark it as done: `todo done "read an article"`
