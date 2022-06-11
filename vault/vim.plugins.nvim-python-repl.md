---
id: 1vtq3snd1k38nph0bp6tcuy
title: Nvim Python Repl
desc: ''
updated: 1654931607613
created: 1654931418645
---

I changed the python repl command from `ipython` to be the following because I couldn't not find where `ipython` was meant to be installed. It does not appear to be in the scripts folder

`nvim-python-repl.lua`

```lua
M.repls = {
    python = "python -m IPython", # Use to be "ipython"
    scala = "amm",
    lua = "ilua"
}
```