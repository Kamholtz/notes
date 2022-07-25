


Overall guide with suggested keymaps, ui, telescope


[Neovim DAP Enhanced](https://alpha2phi.medium.com/neovim-dap-enhanced-ebc730ff498b)


## Installation

[Debug Adapter installation · mfussenegger/nvim-dap Wiki](https://github.com/mfussenegger/nvim-dap/wiki/Debug-Adapter-installation)

> build vscode-chrome-debug
>
> git clone https://github.com/Microsoft/vscode-chrome-debug
> cd ./vscode-chrome-debug
> npm install
> npm run build
> add the adapter cfg:

Notice that the path to vscode-chrome-debug needs to be set

```lua
dap.adapters.chrome = {
    type = "executable",
    command = "node",
    args = {os.getenv("HOME") .. "/path/to/vscode-chrome-debug/out/src/chromeDebug.js"} -- TODO adjust
}

dap.configurations.javascriptreact = { -- change this to javascript if needed
    {
        type = "chrome",
        request = "attach",
        program = "${file}",
        cwd = vim.fn.getcwd(),
        sourceMaps = true,
        protocol = "inspector",
        port = 9222,
        webRoot = "${workspaceFolder}"
    }
}

dap.configurations.typescriptreact = { -- change to typescript if needed
    {
        type = "chrome",
        request = "attach",
        program = "${file}",
        cwd = vim.fn.getcwd(),
        sourceMaps = true,
        protocol = "inspector",
        port = 9222,
        webRoot = "${workspaceFolder}"
    }
}

```
