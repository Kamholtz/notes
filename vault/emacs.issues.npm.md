---
id: 563e2797-65b6-4d58-8605-bc0c5931face
title: Npm
desc: ''
updated: 1619787636440
created: 1619786966356
---
## Error

> bash: /c/Program Files/nodejs/npm: /bin/sh^M: bad interpreter: No such file or directory

## Solution

> Not my solution, but this seemed to work for me. Appears that having the Windows folder structure in $PATH while using WSL2 was causing that parse error, but I'm not exactly sure why.
>
> Go to your user root (cd ~)
> Open .bashrc in your chosen editor (vi, nano, etc.)
> Append to the end of the file: PATH=$(echo "$PATH" | sed -e 's/:\/mnt.*//g') # strip out problematic Windows %PATH%
> Close and re-open all terminal windows
> Source: https://hackmd.io/@badging/wsl2#Troubleshooting-PATH

[Cannot run NPM Commands](https://stackoverflow.com/questions/39311147/cannot-run-npm-commands)