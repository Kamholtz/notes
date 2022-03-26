---
id: fy4hr46wqzzi13qwknqktmg
title: Fresh Install
desc: ''
updated: 1647863030096
created: 1647862601334
---

## Powershell script execution

![[Enable Scripts|powershell.enable-scripts]]

## AHK

- Add shortcut to `capslock-remap.ahk`

## Fonts

FiraCode NF [Nerd Fonts - Iconic font aggregator, glyphs/icons collection, &amp; fonts patcher](https://www.nerdfonts.com/font-downloads)


## Python


Installing python **version 3.8** to avoid this issue: [[No moduled named 'constants'|ee.nrfutil#no-moduled-named-constants]]

- The node install also includes 3.10 (or the latest version) anyway it appears

## Bin

- rg
  - [Release 13.0.0 · BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep/releases/tag/13.0.0)
    - `ripgrep-13.0.0-x86_64-pc-windows-msvc.zip`
- [[vim.plugins.fzf]]

### Add to path

- `C:\bin`
- `C:\bin\Neovim\bin`
- `C:\bin\llvm-mingw-20220323-msvcrt-x86_64\bin`
- `C:\bin\ripgrep`

## Neovim

![[Initial Install|vim.initial-install]]

### telescope-fzf-native

[GitHub - nvim-telescope/telescope-fzf-native.nvim: FZF sorter for telescope written in c](https://github.com/nvim-telescope/telescope-fzf-native.nvim)
  - mingw sourced from: [Releases · mstorsjo/llvm-mingw](https://github.com/mstorsjo/llvm-mingw/releases) this time, which has `mingw32-make`

### fzf

- Install binaries as above

### Python (for CHADTree/remote)

- `pip install pynvim`

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
