---
id: N2y2B01sEn8RCAOIRckoW
title: Telescope
desc: ''
updated: 1644556082371
created: 1641381701550
---


## Slowness and Freezing

Consider disabling treesitter in the preview window if telescope is freezing nvim

[Telescope live_grep freezes nvim sometimes · Issue #1379 · nvim-telescope/telescope.nvim](https://github.com/nvim-telescope/telescope.nvim/issues/1379)
```lua
telescope.setup({
	defaults = {
   		preview = {
   			treesitter = false,
   		},
   },
})
```