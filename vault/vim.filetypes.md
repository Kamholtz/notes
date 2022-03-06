---
id: yf8d4qvk9xuqytu2nb2eh5y
title: Filetypes
desc: ''
updated: 1646453899096
created: 1646447307486
---

## List of filetypes

[vim/filetype.vim at master · vim/vim](https://github.com/vim/vim/blob/master/runtime/filetype.vim)

## Get the filetype

`:set filetype?`

`echo &filetype`

## Set the filetype

`:set filetype=cpp`

## C/C++

### Vim recognising header files as C++ instead of C

[r/neovim - [Question] Does the C parser from nvim-treesitter parse header files?](https://www.reddit.com/r/neovim/comments/orfpcd/question_does_the_c_parser_from_nvimtreesitter/)

> Check whether Neovim is setting the filetype to cpp instead of c.
>
> If it's setting it to cpp you probably want to write let `g:c_syntax_for_h = 1` in your config. See :help c.vim.

### Filetype detection for .h files as C with Doxygen

Useful points from [Using Vim as C/C++ IDE](https://www.alexeyshmalko.com/2014/using-vim-as-c-cpp-ide/
)

- Filetype detection:

```vim
augroup project
  autocmd!
  autocmd BufRead,BufNewFile *.h,*.c set filetype=c.doxygen
augroup END
```

- This will trigger for ALL `.h` files. There is likely a way to set this on a per project basis with a per project config. I have not investigated this yet.