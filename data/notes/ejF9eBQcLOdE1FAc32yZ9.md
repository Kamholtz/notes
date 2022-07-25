

## Errors


In use with [[vim.plugins.telescope]]

`Telescope treesitter`

```
[telescope] [WARN  21:20:56] ...ck\packer\start\telescope.nvim/lua/telescope/pickers.lua:467: Finder failed with msg:  ...ck\packer\start\telescope.nvim/lua/telescope/sorters.lua:596: table index is nil
```

## Troubleshooting

### Cheahealth

`:checkheath nvim_treesitter`

### Get Parser Paths

`:echo nvim_get_runtime_file('parser', v:true)`


## query error: invalid node type at position

[GitHub - nvim-treesitter/nvim-treesitter: Nvim Treesitter configurations and abstraction layer](https://github.com/nvim-treesitter/nvim-treesitter#i-get-query-error-invalid-node-type-at-position)

> query error: invalid node type at position

I was seeing this error in header files within a C project. Using `:set filetype?` indicated that the the file was being recognised as C++ instead of C. This is remedied by configuring filetype detection as `c.doxygen`:

![[Vim recognising header files as C++ instead of C|vim.filetypes#vim-recognising-header-files-as-c-instead-of-c]]

I was still receiving the same `invalid node type` error from a `cpp` parser despite the `:set filetype?` now returning `c.doxygen`. Uninstalling the `cpp` parser was the (immediate) solution to this problem.

- `:TSUninstall cpp` is meant to do this, but the `cpp parser` remained active
- I found I had to remove `cpp.so` from `C:\Users\{user}\AppData\Local\nvim-data\site\pack\packer\start\nvim-treesitter\parser` manually.
