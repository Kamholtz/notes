---
id: e75c468f-ccc0-4533-b9ef-22ce0f9b0ef5
title: Lispyville
desc: ""
updated: 1620457987525
created: 1619348502245
---

> lispyville.el’s main purpose is to provide a lisp-editing environment suited towards evil users. It can serve as a minimal layer on top of lispy-mode for better integration with evil, but it does not require use of lispy’s keybinding style. The provided commands allow for editing lisp in normal state and will work even without lispy-mode enabled. If you are just looking for a way to prevent evil’s operators from unbalancing parentheses, you can enable lispyville-mode in your configuration and just ignore the rest of its features.

[noctuid/lispyville](https://github.com/noctuid/lispyville)

## Doom Emacs Lispyville config

```elisp
(use-package! lispyville
  :when (featurep! :editor evil)
  :hook (lispy-mode . lispyville-mode)
  :init
  (setq lispyville-key-theme
        '((operators normal)
          c-w
          (prettify insert)
          (atom-movement t)
          slurp/barf-lispy
          additional
          additional-insert))
  :config
  (lispyville-set-key-theme))
```

### Relevant shortcuts

#### Operators Normal

| key                               | command                                    |
| --------------------------------- | ------------------------------------------ |
| [remap evil-yank]                 | lispyville-yank                            |
| [remap evil-delete]               | lispyville-delete                          |
| [remap evil-change]               | lispyville-change                          |
| [remap evil-yank-line]            | lispyville-yank-line                       |
| [remap evil-delete-line]          | lispyville-delete-line                     |
| [remap evil-change-line]          | lispyville-change-line                     |
| [remap evil-delete-char]          | lispyville-delete-char-or-splice           |
| [remap evil-delete-backward-char] | lispyville-delete-char-or-splice-backwards |
| [remap evil-substitute]           | lispyville-substitute                      |
| [remap evil-change-whole-line]    | lispyville-change-whole-line               |
| [remap evil-join]                 | lispyville-join                            |

#### c-w

| key                               | command                         |
| --------------------------------- | ------------------------------- |
| [remap evil-delete-backward-word] | lispyville-delete-backward-word |

#### Preffify Insert

Will prettify when making changes in insert mode. Note that prettify won't be triggered when changes are made from normal mode e.g. deleting a line.

| key                 | command             |
| ------------------- | ------------------- |
| [remap evil-indent] | lispyville-prettify |

#### Atom Movement

| key                              | command                        |
| -------------------------------- | ------------------------------ |
| [remap evil-forward-WORD-begin]  | lispyville-forward-atom-begin  |
| [remap evil-forward-WORD-end]    | lispyville-forward-atom-end    |
| [remap evil-backward-WORD-begin] | lispyville-backward-atom-begin |
| [remap evil-backward-WORD-end]   | lispyville-backward-atom-end   |

#### Slurp/Barf

| key | command          |
| --- | ---------------- |
| >   | lispyville-slurp |
| <   | lispyville-barf  |

#### Additional

| key | command                  |
| --- | ------------------------ |
| M-j | lispyville-drag-forward  |
| M-k | lispyville-drag-backward |
| M-J | lispy-join               |
| M-s | lispy-splice             |
| M-S | lispy-split              |
| M-r | lispy-raise-sexp         |
| M-R | lispyville-raise-list    |
| M-t | transpose-sexps          |
| M-v | lispy-convolute-sexp     |

#### Additional Insert

| key | command                                |
| --- | -------------------------------------- |
| M-i | lispyville-insert-at-beginning-of-list |
| M-a | lispyville-insert-at-end-of-list       |
| M-o | lispyville-open-below-list             |
| M-O | lispyville-open-above-list             |


