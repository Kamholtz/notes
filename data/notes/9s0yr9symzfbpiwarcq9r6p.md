
## Examples

### Symbolic Link

An example of making a symbolic link to make the `nvim` command point to an [[os.linux.appimage]] without using an alias. This has the advantage of `nvim` being accessible within scripts.

```bash
sudo ln -s /usr/local/bin/nvim.appimage /usr/local/bin/nvim
```
