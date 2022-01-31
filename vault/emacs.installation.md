---
id: 3f4d3007-34ed-4813-90c3-f51ffff12f82
title: Installation
desc: ''
updated: 1619769783240
created: 1618468510678
---


## Errors

The following messages occurs when trying to use swiper in a large file.

Messages buffer:

> user-error: Required program "C:\msys64\usr\bin\grep" not found in your path

Install MSYS2 which contains grep from here:

https://www.msys2.org/


## WSL Guide

Have not used the following guide to install on WSL2 but am using MobaXterm instead of vcxsrv

Encountered this error [[Apt Fix Broken Install|os.ubuntu.errors.apt-fix-broken-install]] during installation.

[The ultimate Emacs hacking tutorial in Windows 10 WSL 2](https://hkvim.com/post/windows-setup/)

## Guide followed for WSL

[hubisan/emacs-wsl](https://github.com/hubisan/emacs-wsl#install-emacs-272)

### Install Dependencies

> If you are on Ubuntu 18.04 use the dependencies from ./install-emacs/ubuntu-18.04-dependencies.sh. In that case you will also have to modify the scripts (if you plan to use them) as the distribution is hardcoded into them to make sure to use the right distribution even if it is not set as default.

```bash
# Dependencies for Ubuntu 18.04

sudo apt install -y autoconf automake autotools-dev bsd-mailx build-essential \
    diffstat gnutls-dev imagemagick libasound2-dev libc6-dev libdatrie-dev \
    libdbus-1-dev libgconf2-dev libgif-dev libgnutls28-dev libgpm-dev libgtk2.0-dev \
    libgtk-3-dev libice-dev libjpeg-dev liblockfile-dev liblqr-1-0 libm17n-dev \
    libmagickwand-dev libncurses5-dev libncurses-dev libotf-dev libpng-dev \
    librsvg2-dev libsm-dev libthai-dev libtiff5-dev libtiff-dev libtinfo-dev libtool \
    libx11-dev libxext-dev libxi-dev libxml2-dev libxmu-dev libxmuu-dev libxpm-dev \
    libxrandr-dev libxt-dev libxtst-dev libxv-dev quilt sharutils texinfo xaw3dg \
    xaw3dg-dev xorg-dev xutils-dev zlib1g-dev libjansson-dev libxaw7-dev \
    libselinux1-dev libmagick++-dev libacl1-dev gir1.2-javascriptcoregtk-4.0 \
    gir1.2-webkit2-4.0 libenchant1c2a libglvnd-core-dev libicu-le-hb-dev \
    libidn2-0-dev libjavascriptcoregtk-4.0-dev liboss4-salsa2 libsoup2.4-dev \
    libsystemd-dev libwebkit2gtk-4.0-dev libx11-xcb-dev libxcb-dri2-0-dev \
    libxcb-dri3-dev libxcb-glx0-dev libxcb-present-dev libxshmfence-dev \
    x11proto-composite-dev x11proto-core-dev x11proto-damage-dev \
    x11proto-fixes-dev
```

> There will be a dialog about the mail server configuration, just select no configuration to leave it as it is and confirm with OK (use TAB and RET to get through this).

### Download and extract Emacs

```bash
cd ~
wget https://ftp.gnu.org/pub/gnu/emacs/emacs-27.2.tar.gz
tar -xzvf emacs-27.2.tar.gz
```

### Configure and install Emacs

This will make and install emacs such that the alias `emacs` should now point to version 27.2

```
cd ~/emacs-27.2
./configure --with-cairo
make
sudo make install
rm ~/emacs-27.2.tar.gz
```

### Optional dependencies

[BurntSushi/ripgrep](https://github.com/BurntSushi/ripgrep)

If you're a Debian user (or a user of a Debian derivative like Ubuntu), then ripgrep can be installed using a binary .deb file provided in each ripgrep release.

$ curl -LO https://github.com/BurntSushi/ripgrep/releases/download/12.1.1/ripgrep_12.1.1_amd64.deb
$ sudo dpkg -i ripgrep_12.1.1_amd64.deb
