
## Limitations

Aliases cannot be exported

> Aliases can't be exported so they're not available in shell scripts in which they aren't defined. In other words, if you define them in ~/.bashrc they're not available to your_script.sh (unless you source ~/.bashrc in the script, which I wouldn't recommend but there are ways to do this properly).

- Source: [Why doesn&#x27;t my Bash script recognize aliases?](https://unix.stackexchange.com/questions/1496/why-doesnt-my-bash-script-recognize-aliases)

### Alternative

Create a symbolic link with [[os.linux.cli.ln]]. This will be accessible from scripts

## Examples

```bash
alias python=python3
alias nvim=nvim.appimage
```
