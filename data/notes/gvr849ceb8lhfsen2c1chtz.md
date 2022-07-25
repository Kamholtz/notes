
## Defining Project Specific Settings

[Project local settings · neovim/nvim-lspconfig Wiki](https://github.com/neovim/nvim-lspconfig/wiki/Project-local-settings)

```lua
local nvim_lsp = require('lspconfig')

nvim_lsp.rust_analyzer.setup {
  on_init = function(client)
    client.config.settings.xxx = "yyyy"
    client.notify("workspace/didChangeConfiguration")
    return true
  end
}
```