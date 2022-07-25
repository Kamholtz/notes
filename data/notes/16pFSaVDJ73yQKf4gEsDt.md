


## DAP

[GitHub - jbyuki/one-small-step-for-vimkind: Debug adapter for Neovim plugins](https://github.com/jbyuki/one-small-step-for-vimkind)

## General

[Difference between the various VIM APIs](https://www.reddit.com/r/neovim/comments/muxuc3/difference_between_the_various_vim_apis/)


> `vim.cmd`: Invokes an Ex command (the ":" commands, Vimscript statements). Example:
>

`vim.cmd('echo 42')`

>
> same value as vim.api.nvim_command.
>
>
>
> vim.fn: Invokes vim-function or user-function {func} with arguments {...}.
>
> To call autoload functions, use the syntax: >
>

`vim.fn['some#function']({...})`

>
> Unlike `vim.api.nvim_call_function` this converts directly between Vim
>
> objects and Lua objects. If the Vim function returns a float, it will
>
> be represented directly as a Lua number. Empty lists and dictionaries
>
> both are represented by an empty table.
>
>
>

`vim.api.nvim_command`: same value as vim.cmd.

>
>
>
> `vim.api.nvim_exec`: This function evaluates a chunk of Vimscript code. It takes in a string containing the source code to execute and a boolean to determine whether the output of the code should be returned by the function (you can then store the output in a variable, for example).
>

```lua
local result = vim.api.nvim_exec(
[[
let mytext = 'hello world'

function! MyFunction(text)
echo a:text
endfunction

call MyFunction(mytext)
]],
true)
print(result) -- 'hello world'
```
