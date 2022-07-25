
## Download

[Releases · git-for-windows/git](https://github.com/git-for-windows/git/releases)

## Share credentials between Windows and WSL

I encountered difficulty entering Github token via the WSL2 terminal. It was easier to to use [[git.git-credential-manager]] to share the credentials that have already been entered in Windows.

[Get started using Git on WSL](https://docs.microsoft.com/en-us/windows/wsl/tutorials/wsl-git)

> It is recommended to install the latest Git for Windows in order to share credentials & settings between WSL and the Windows host.

> If GIT installed is >= v2.36.1

```bash
git config --global credential.helper "/mnt/c/Program\ Files/Git/mingw64/bin/git-credential-manager-core.exe"
```

