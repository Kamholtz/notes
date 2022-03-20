---
id: s3ibshdy8z3ang12arl3teq
title: Loop Uv
desc: ''
updated: 1647160154802
created: 1647159339172
---

Access to vim events + asynchronous IO via the Lua implementation of libuv [[software.libuv]].

- `vim.loop`


## Docs

[luv/docs.md at master · luvit/luv](https://github.com/luvit/luv/blob/master/docs.md)

## Examples

- Official Lua Libuv: [luv/examples at master · luvit/luv](https://github.com/luvit/luv/tree/master/examples)
- Blog post with markdown export and async grep examples: [using libuv inside neovim](https://teukka.tech/vimloop.html)
- GitHub issue "simple example" that works (but eventually crashes neovim from too much output): [Plenary.job crashes on Windows · Issue #146 · nvim-lua/plenary.nvim](https://github.com/nvim-lua/plenary.nvim/issues/146#issuecomment-840821591)

## Wrapper

[[vim.plugins.plenary]] provides a wrapper (but not everything works with windows, as suggested in various GitHub issues) [GitHub - nvim-lua/plenary.nvim: plenary: full; complete; entire; absolute; unqualified. All the lua functions I don&#39;t want to write twice.](https://github.com/nvim-lua/plenary.nvim)
