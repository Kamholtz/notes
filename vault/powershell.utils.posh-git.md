---
id: b090bba0-6462-403c-b9a2-674547a7be0e
title: Posh-git
desc: ''
updated: 1616371411500
created: 1616370848950
---


CLI too for providing a nicer git command line experience (with colours, command line status, etc)

## Install

Don't bother using choco. Instead just install the Powershell modulle

From [dahlbyk/posh-git](https://github.com/dahlbyk/posh-git):

```powershell
PowerShellGet\Install-Module posh-git -Scope CurrentUser -AllowPrerelease -Force
```

Command I actually ran because `-AllowPrerelease` was not recognised and we actually want the module accessible by all users (i.e. Admin and regular user account). See [Install-Module (PowerShellGet) - PowerShell](https://docs.microsoft.com/en-us/powershell/module/powershellget/install-module?view=powershell-7.1) for more information.

```powershell
PowerShellGet\Install-Module posh-git -Scope AllUsers  -Force
```

## Automatically load for profile

To make the module load each time a powershell session is opened, use:

```powershell
Add-PoshGitToProfile
```
