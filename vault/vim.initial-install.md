---
id: v3K06639TokG0fDufJlPY
title: Initial Install
desc: ''
updated: 1641269554734
created: 1641195331001
---

## Dependencies:

Chadtree:

run the command
- `CHADdeps`

### junegunn\fzf

- fzf
  - `fzf#install()`
  - this has been added to fzf.fnl so it should now install automatically

Input being overwritten while typing quickly
  https://github.com/junegunn/fzf.vim/issues/1011

### telescope-fzf-native

Using make from `C:\Program Files\mingw-w64\x86_64-8.1.0-posix-seh-rt_v6-rev0\mingw64\bin\mingw32-make.exe`

```bat
C:\Users\c.kamholtz\AppData\Local\nvim-data\site\pack\packer\start\telescope-fzf-native.nvim [main ≡]> mingw32-make.exe
mkdir build
gcc -O3 -Wall -Werror -fpic -std=gnu99 -shared src/fzf.c -o build/libfzf.dll
```
