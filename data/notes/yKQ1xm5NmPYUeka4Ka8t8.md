

## Using with fennel

This plugin does not seem to work immediately with fennel when loaded with packer. Errors indicated that despite being installed, BQF was not loaded into cache and thus wasn't acccessible when `require('bqf')` was called. Checking [[Packer Status|vim.plugins.packer.status]] showed that BQF was not yet loaded. Simply opening quickfix with `:copen` loads the plugin (which was verified in `packer status`). At this point `require('bqf')` will work and [[Packer Compile|vim.plugins.packer.compile]] can be called. From this point on, when `nvim` is run it `bqf` will be loaded correctly.
