---
id: 9fc49e04-0641-4b47-836b-dfeae625a027
title: Not in Project or Blacklisted
desc: ''
updated: 1619415549856
created: 1619415518090
---

[what &#39;s the reason ? LSP :: one.py not in project or it is blacklisted. · Issue #2392 · emacs-lsp/lsp-mode](https://github.com/emacs-lsp/lsp-mode/issues/2392)

> You probably pressed "Esc" when the "LSP import project" prompt came, unless you blacklisted it explicitly using lsp-blacklist-project (which is unlikely).
>
> All you need to do to fix this is to press M-x lsp followed by i, with one.py as the current buffer.