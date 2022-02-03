---
id: 43rF3oyntG5gSYcFcPOID
title: Fzf
desc: ''
updated: 1643889548193
created: 1640853235289
---



## Send to quickfix

> Try this:
>
> After searching, use alt-a to select all results and then hit enter. All matches will then be in the quick fix list. You can use :cn and :cp to cycle between them

[r/vim - A problem with fzf](https://www.reddit.com/r/vim/comments/7ylwu3/a_problem_with_fzf/)


## Skipping input bug

[FZF terminal window does not seem to clear completely or have weird input behavior on windows · Issue #1011 · junegunn/fzf.vim](https://github.com/junegunn/fzf.vim/issues/1011)

Workaround:

```vim
let g:fzf_preview_window=''
```

## Search Files from first ancestor containing .git

Search upwards from current path to an ancestor containing `.git` and then call `:Files` from that parent. Useful for searching through a large repo of many sub-projects, where one of the sub-projects is your current working directory (`:cd`).

[.vim/vimrc at e9312935fb915fd6bfc4436b70b300387445aef8 · habamax/.vim](https://github.com/habamax/.vim/blob/e9312935fb915fd6bfc4436b70b300387445aef8/vimrc#L270-L275)
Fennel equivalent

```lisp
(defn fzf-root []
  (let [expanded (.. (vim.fn.expand "%:p:h") ";")
        path (vim.fn.finddir ".git" expanded)
        subbed (vim.fn.substitute path ".git" "" "")
        result (vim.fn.fnamemodify subbed ":p:h")]

      result))

(autil.fn-bridge "s:fzf_root" "config.plugin.fzf" "fzf-root")
(nvim.set_keymap :n :<leader>fu ":exe 'Files ' . <SID>fzf_root()<CR>" {:noremap true})
```

- [ ] Make a similar command for calling `rg` from a parent `.git` directory 

## Using fd


## previewer on windows

