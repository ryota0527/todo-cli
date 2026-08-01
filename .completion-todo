#!/bin/bash

completion() {
    local cur

    cur="${COMP_WORDS[COMP_CWORD]}"

    COMPREPLY=(
        $(compgen -W "$(todo comp)" -- "$cur")
    )
}

complete -F completion todo
