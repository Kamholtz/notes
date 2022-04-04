---
id: 2rmjybi666991y8rob7q73a
title: Errors
desc: ''
updated: 1648967161747
created: 1648967161747
---

## Invalid choice: 'build'

> usage: west [-h] [-z ZEPHYR_BASE] [-v] [-V] <command> ...
> west: error: argument <command>: invalid choice: 'build' (choose from 'init', 'update', 'list', 'manifest', 'diff', 'status', 'forall', 'help', 'config', 'topdir', 'selfupdate')

- [Build process broken - Nordic Q&amp;A - Nordic DevZone - Nordic DevZone](https://devzone.nordicsemi.com/f/nordic-q-a/81353/build-process-broken)

- [build nrf52 platform with vscode - Nordic Q&amp;A - Nordic DevZone - Nordic DevZone](https://devzone.nordicsemi.com/f/nordic-q-a/85508/build-nrf52-platform-with-vscode/356621#356621)

  > From the command pallette of VS Code, please run the nRF Connect: Generate Support information

  > Downgrading VSCode to 1.64 did the trick.

It appears that installing everything from [[VSCode installation|ee.nrf-connect-sdk#vscode-installation]] made it work again. This includes all the tools and VSCode extensions (but not VSCode itself)

- Order: Commandline tools, NRF Connect for Desktop, Toolchain manager (within desktop app), nRF Connect SDK (within desktop app), open VSCode from within desktop app, install extensions via automatic prompt

The following steps may have also been relevant

- Change all absolute paths to be wrt home via project wide `ctrl + shift + f`
- Set the Zephyr path
