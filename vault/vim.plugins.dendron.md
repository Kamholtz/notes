---
id: cAD0INalu1NbwRP1DNeIz
title: Dendron
desc: ''
updated: 1642909239449
created: 1642908515283
---


## Thoughts on creating Dendron support in Neovim

[2021-11-24 Office Hours](https://wiki.dendron.so/notes/6iPfPKI8nOwQLVF6KgfJU/)

[Dendron Office Hours | 2021-11-24](https://www.youtube.com/watch?v=LuoD8ibOazE)

33:30 Q&A: Dendron's Client/Server Design vs. Pure CLI

- Dendron uses a client/server architecture (express server) but it does not yet support LSP
  - Could use [GitHub - neovim/node-client: Nvim Node.js client and plugin host](https://github.com/neovim/node-client) to communicate with the server? Could maybe just for the client part of dendron
  - LSP is planned, at which point SOME of the features could be accessed by biult in LSP or coc
    - Creating a coc-plugin
      - [How to write a coc.nvim extension | Sam's world](https://samroeca.com/coc-plugin.html)
- There is also a CLI but that would involve parsing strings from pipes or something like that


Someone's early work on CLI integration

[vimdendron/dendron.vim at main · icedwater/vimdendron](https://github.com/icedwater/vimdendron/blob/main/dendron.vim)


## Rendering on markdown

- Markdown preview via coc

  - [GitHub - weirongxu/coc-markdown-preview-enhanced: Markdown Preview Enhanced for coc.nvim](https://github.com/weirongxu/coc-markdown-preview-enhanced)

  - It uses webview: [GitHub - weirongxu/coc-webview: Using an external browser to support the webview in coc.nvim.](https://github.com/weirongxu/coc-webview)