---
id: v3K06639TokG0fDufJlPY
title: Initial Install
desc: ''
updated: 1656935405701
created: 1641195331001
---

## Dependencies

### Python (for General + CHADTree)

- `pip install pynvim`

### Chadtree

Run the command

- `CHADdeps`

### junegunn\fzf

- fzf
  - `fzf#install()`
  - this has been added to fzf.fnl so it should now install automatically

Input being overwritten while typing quickly
  https://github.com/junegunn/fzf.vim/issues/1011

### telescope-fzf-native

[GitHub - nvim-telescope/telescope-fzf-native.nvim: FZF sorter for telescope written in c](https://github.com/nvim-telescope/telescope-fzf-native.nvim)

This needs to be built using something like mingw. There are two builds of Mingw that I have used for this plugin shown below.

#### Option 1

LLVM Mingw seems to be a newer version but I have not extensively tested the result of this build yet

- [Releases · mstorsjo/llvm-mingw](https://github.com/mstorsjo/llvm-mingw/releases), which has `mingw32-make`

#### Option 2

Using make from `C:\Program Files\mingw-w64\x86_64-8.1.0-posix-seh-rt_v6-rev0\mingw64\bin\mingw32-make.exe`

```bat
C:\Users\c.kamholtz\AppData\Local\nvim-data\site\pack\packer\start\telescope-fzf-native.nvim [main ≡]> mingw32-make.exe
mkdir build
gcc -O3 -Wall -Werror -fpic -std=gnu99 -shared src/fzf.c -o build/libfzf.dll
```

### Node

- install with visual studio build tools

![](/assets/images/2022-03-26-13-54-27.png)

#### Install log

> ====================================================
> Tools for Node.js Native Modules Installation Script
> ====================================================
>
> This script will install Python and the Visual Studio Build Tools, necessary
> to compile Node.js native modules. Note that Chocolatey and required Windows
> updates will also be installed.
>
> This will require about 3 Gb of free disk space, plus any space necessary to
> install Windows updates. This will take a while to run.
>
> Please close all open programs for the duration of the installation. If the
> installation fails, please ensure Windows is fully updated, reboot your
> computer and try to run this again. This script can be found in the
> Start menu under Node.js.
>
> You can close this window to stop now. Detailed instructions to install these
> tools manually are available at https://github.com/nodejs/node-gyp#on-windows
>
> Press any key to continue . . .


>
> - chocolatey-dotnetfx.extension v1.0.1
> - kb3033929 v1.0.5
> - visualstudio2019buildtools v16.11.11.0
> - python3 v3.10.4
> - chocolatey-windowsupdate.extension v1.0.4
> - vcredist140 v14.31.31103
> - kb2999226 v1.0.20181019
> - visualstudio-installer v2.0.2
> - kb2919355 v1.0.20160915
> - chocolatey-core.extension v1.3.5.1
> - kb2919442 v1.0.20160915
> - chocolatey-visualstudio.extension v1.10.0
> - vcredist2015 v14.0.24215.20170201
> - dotnetfx v4.8.0.20190930
> - visualstudio2019-workload-vctools v1.0.1
> - kb3035131 v1.0.3
> - python v3.10.4


## WSL2

Same as above for WSL2, Ubuntu

```bash
  102  mv /mnt/c/Users/carlk/Downloads/nvim.appimage .
  104  sudo mv /mnt/c/Users/carlk/Downloads/nvim.appimage .

  106  chmod u+x nvim.appimage && ./nvim.appimage
  107  sudo chmod u+x nvim.appimage && ./nvim.appimage

  131  python3 -m pip3 install pynvim

  138  sudo apt-get install fzf
  139  sudo apt-get install ripgrep
  140  sudo apt-get install cmake
  141  sudo apt-get install gcc

  152  cd site/pack/packer/start/telescope-fzf-native.nvim/
  153  make
```

  Need this for treesitter or you will encounter `/usr/bin/ld: cannot find -lstdc++ `

```bash
  162  sudo apt install build-essential

  174  sudo apt install python3-pip
  175  pip3 install pynvim
```

Add the following to your `.bashrc`

```bash
alias python=python3
alias nvim=nvim.appimage

```

### Configuring Git in WSL2

[[For Windows|git.for-windows]]