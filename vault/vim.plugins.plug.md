---
id: 3a9f3a38-7cdf-434d-8bae-79e41fc129f6
title: Plug
desc: ''
updated: 1617588398384
created: 1617588312036
---

## Setup

[How am I supposed to user vim-plug with Windows - PowerShell? · Issue #633 · junegunn/vim-plug](https://github.com/junegunn/vim-plug/issues/633)


> Neovim doesn't load files in ~\vimfiles\autoload, the installation instruction for Windows was written when Neovim didn't officially support Windows. I suppose plug.vim should be placed under ~\AppData\Local\nvim\autoload. @justinmk, can you confirm this?

e.g.

```vim
call plug#begin('~/AppData/Local/nvim/autoload')
```
