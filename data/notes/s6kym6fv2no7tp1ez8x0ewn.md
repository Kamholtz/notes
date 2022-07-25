
[GitHub - carlosrocha/vim-chrome-devtools: Neovim integration with Chrome DevTools](https://github.com/carlosrocha/vim-chrome-devtools)


I have not succeeded on getting this to work on windows yet, but the following steps seem to be in the right direction

## Installation on Windows

The install script in the installation folder, `install.sh` does not work on windows. Perhaps in WSL, but I could not get that to work either. The script contains:

Root installation folder: `C:\Users\xxx\AppData\Local\nvim-data\site\pack\packer\start\vim-chrome-devtools`

```bash
npm --prefix=rplugin/node/vim-chrome-devtools install && npm --prefix=rplugin/node/vim-chrome-devtools run build
```

Which seems to just install and build the remote plugin in the `--prefix` folder. Simply running this from the root installation folder did not work. Seemingly the `--prefix` option did not apply and `&&` was not recognised in powershell. I did the following steps instead:

```bash
cd rplugin/node/vim-chrome-devtools
npm install
npm run build
npm install -g neovim
```

I subsequently ran `:UpdateRemotePlugins` in neovim

## Launching an Edge instance with a debugging port

```bash
C:\Program Files (x86)\Microsoft\Edge\Application> .\msedge.exe --remote-debugging-port=9222
```

- Perhaps this really only works with `Chrome` and not just browsers using the chrome engine.
  - [x] Tested on chrome instead. I did not receive an error about the connection being rejected on `:ChromeDevToolsConnect` but also did not see confirmation
  - `C:\Program Files\Google\Chrome\Application> .\chrome.exe --remote-debugging-port=9222`