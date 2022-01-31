---
id: c5ba41e5-eb29-452e-b627-dd083dfa78ea
title: Rsync
desc: ''
updated: 1620458247657
created: 1620020443825
---


## Guide

[How to Transfer Files with Rsync over SSH {With Examples}](https://phoenixnap.com/kb/how-to-rsync-over-ssh)

## Handling Hidden files

Particularly useful for .env files
te
> The problem is not rsync, but the shell.
>
> Normally in Ubuntu, dotglob is disabled, meaning that files starting with . are excluded from * expansion.
>
> You can turn this on running.
>
> shopt -s dotglob
> Then your command should work (I think you're just missing -e ssh)
>
> It's sensible to unset dotglob after use with:
>
> shopt -u dotglob
> Alternatively, you can simply tell rsync to copy the folder contents to target_dir, which includes hidden files:
>
> rsync --ab -e ssh myuser@sourcehost:/source_dir/ target_dir

[how to migrate the hidden files using rsync](https://askubuntu.com/questions/1098640/how-to-migrate-the-hidden-files-using-rsync)
