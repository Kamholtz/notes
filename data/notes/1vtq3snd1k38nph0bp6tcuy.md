
I changed the python repl command from `ipython` to be the following because I couldn't not find where `ipython` was meant to be installed. It does not appear to be in the scripts folder

`nvim-python-repl.lua`

```lua
M.repls = {
    python = "python -m IPython", # Use to be "ipython"
    scala = "amm",
    lua = "ilua"
}
```