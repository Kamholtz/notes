---
id: 9s0yr9symzfbpiwarcq9r6p
title: Ln
desc: ''
updated: 1657427044065
created: 1657426747584
---

## Examples

### Symbolic Link

An example of making a symbolic link to make the `nvim` command point to an [[os.linux.appimage]] without using an alias. This has the advantage of `nvim` being accessible within scripts.

```bash
sudo ln -s /usr/local/bin/nvim.appimage /usr/local/bin/nvim
```
