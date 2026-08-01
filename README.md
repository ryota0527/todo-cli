# todo-cli

This is a simple command-line todo management tool for linux environment.

## Requirements

python > 3.8 is recommended.

## Installation

Clone this repository and run: `./install.sh`

Then you can use just by running `todo init` .<br>
To check the usage, type `todo` .

## Commands List

| command | Description |
|---------|-------------|
| `todo init` | Initialize |
| `todo view [-a]` | show current todos |
| `todo make <name1>, <name2>, ...` | make new todos |
| `todo done <name1>, <name2>, ...` | mark todos as finished |
| `todo del <name1>, <name2>, ...` | remove todos which are not finished |
| `todo note <todo>` | add notes in the todo (vim opens) |
| `todo tag <todo name> <tag name>` | add a tag on the todo |
| `todo due <todo name> <YYYY-MM-DD>` | set due date for the todo |

## Tips

- Shell completion is available for todo names when you run such as `todo done` or `todo note`. Press Tab key to use the completion just as you usually do in command line.

## Customize

- The editor used for `todo note` can be changed by editing constant `EDITOR_FOR_NOTES` in `src/config.py` e.g. `EDITOR_FOR_NOTES = "nvim"`. (Default: vim)

- Finished todos are automatically deleted when the number of it become more than 15. This number can be changed by editing `CLEAN_NUM` in `src/config.py` .

## Examples
- Initialize: `todo init`

- Add a todo "read an article": `todo make "read an article"`<br>
(*Use quotation mark for todo's name, if it contains space!)

- View: `todo view`<br>
(Output: `- read an article`)

- Set the due date: `todo due "read an article" 2026-08-01`

- Add a tag: `todo tag "read an article" research`

- View again: `todo view`<br>
(Output: `- read an article | Due: 2026-08-01 | Tag: research `)<br>
![todo-cli demo](fig_ex/view_ex.png)

- Add the link to the article as notes: `todo note "read an article"`<br>
(One can paste the link in the todo file)

- Mark it as done: `todo done "read an article"`
