---
id: UN5ygEfGQgASMxZdZ2426
title: Py Launcher
desc: ''
updated: 1645184860989
created: 1645169083170
---

Lauch specific python versions

## List available versions

```batch
C:\Users> py --list
Installed Pythons found by py Launcher for Windows
 -3.9-64 *
 -3.5-64
 -2.7-64
```

## Use a specific version

```batch
py -3.9

```

## Use a commmand with a specific version e.g. pip

```batch
py -3.9 -m pip freeze
```

## Set an alias

```ps1
Set-Alias -Name <new_command_name> -Value python3
```