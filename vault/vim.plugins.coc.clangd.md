---
id: 1Kag9iDQD0sVnvP4NTrLi
title: Clangd
desc: ''
updated: 1640319868672
created: 1640318188003
---

## Prerequisites

Install clangd which is in llvm:

[The LLVM Compiler Infrastructure Project](https://llvm.org/)

- Successfully using v13.0.0 on Windows (though not all definitions can be found in the project I was testing with...)
- Make sure it is added to path during installation

## Creating compile_commands.json


The following is taken from my own comments on this gist:

[PlatformIO-vim.md](https://gist.github.com/neta540/9e65261be52d6cd4d6c17399b78d34bb)


Clangd require a compilation database[Configuration](https://clangd.llvm.org/config#compilationdatabase).

I am guessing everyone here has likely moved to ccls. I personally could not get ccls working on windows. I found that you can get platformio to generate a `compile_commands.json` file for you using the following command:

```batch
pio run -t compiledb
```

This uses the target param `-t` to create the `compile_commands.json`. Could possibly specify the target in `platform.ini` file

![[Settings targets in platformio.ini|platformio.run.targets#settings-targets-in-platformioini]]

By default the `compile_commands.json` file ends up in a directory that clangd will not detect. In my case it was `/.pio/build/nodemcuv2`. There is a `:CocConfig` param for clangd called `compilationDatabasePath` but that did not seem to work for me (config found here: [GitHub - clangd/coc-clangd: clangd extension for coc.nvim](https://github.com/clangd/coc-clangd#configurations)), so I used the work around detailed in [Compilation database compile_commands.json &mdash; PlatformIO latest documentation](https://docs.platformio.org/en/latest/integration/compile_commands.html) which uses a python script to change the where the `compile_commands.json` is created.


`platformio.ini:`

```ini
[env:myenv]
platform = ...
board = ...
extra_scripts = post:extra_script.py
```

`extra_script.py:`

```python
import os
Import("env")

env.Replace(COMPILATIONDB_PATH=os.path.join("$PROJECT_DIR", "compile_commands.json"))

```

~~There is also a `--compile-commands-dir` option for `clangd` which might be worth investigating.~~

## Detecting compile_commands.json with clangd

[Would coc-clangd find compilation database under current directory or parent path ? · Issue #77 · clangd/coc-clangd](https://github.com/clangd/coc-clangd/issues/77)

I can now confirm that the following `:CocLocalConfg` will detect the `compile_commands.json` file in the specified directory using `clangd.args` and `--compile-commands-dir`:

```json
{
  "languageserver": {
    "clangd": {
      "command": "clangd",
      "args": ["--background-index", "--compile-commands-dir", ".pio/build/nodemcuv2" ],
      "rootPatterns": [
        "compile_flags.txt",
        "compile_commands.json",
        ".vim/",
        ".git/",
        ".hg/"
      ],
      "filetypes": ["c", "cpp", "objc", "objcpp"]
    }
  }
}
```


## Per-file compilation database

[Add the possibility to specify per-file compilation database path · Issue #182 · clangd/coc-clangd](https://github.com/clangd/coc-clangd/issues/182)