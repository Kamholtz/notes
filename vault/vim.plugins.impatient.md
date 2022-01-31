---
id: t9ZP4Om5DuVpUMq9nDib1
title: Impatient
desc: ''
updated: 1643166050703
created: 1643165226230
---

[GitHub - lewis6991/impatient.nvim: Improve startup time for Neovim](https://github.com/lewis6991/impatient.nvim)


## Installation

### Common errors

- Need to run ":PackerCompile" before  this can be used... you will see errors about not being able to find `packer_compiled` without doing this.

### Cache Packer's compiled file

To get impatient to cache [[vim.plugins.packer]]'s compiled file we change the path used for packer's compilation:

- Fennel does not like mixing associating and sequential tables, so you will need to create the `spec` parameter for `packer.startup` manually in the `use` command from `Olical`:
  - [GitHub - wbthomason/packer.nvim: A use-package inspired plugin manager for Neovim. Uses native packages, supports Luarocks dependencies, written in Lua, allows for expressive config](https://github.com/wbthomason/packer.nvim#the-startup-function)
    - The form we want is:

    ```lua
    packer.startup({function() use 'tjdevries/colorbuddy.vim' end, config = { ... }})
    ```

  - this can be done with `aniseed.core.assoc`

    ```lisp
    (defn- use [...]
    "Iterates through the arguments as pairs and calls packer's use function for
    each of them. Works around Fennel not liking mixed associative and sequential
    tables as well."
    (let [pkgs [...]
            spec-func
            (fn [use]
            (for [i 1 (a.count pkgs) 2]
                (let [name (. pkgs i)
                    opts (. pkgs (+ i 1))]
                (-?> (. opts :mod) (safe-require-plugin-config))
                (use (a.assoc opts 1 name)))))

            spec-config {:config {:compile_path (.. (vim.fn.stdpath "config") "/lua/packer_compiled.lua")}}
            spec (a.assoc spec-config 1 spec-func)]

        ;(print (vim.inspect spec))
        (packer.startup spec))
    nil)
    ```

    the result for the spec `param` is something like

    ```lisp
    {function () use 'some/plugin' end, {:config {:compile_path "compile/path/"}}}
    ```


- It would seem that the main slow down is due to loading sessions and failing to find some files due to different home-dirs (which we don't really want if loading nvim without params)