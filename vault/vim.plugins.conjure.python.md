---
id: kshyhpkohl8klsjrwbj6bhm
title: Python
desc: ''
updated: 1657538806514
created: 1654930546862
---

A python client does not exist yet. I tried implementing one using the [[vim.plugins.conjure.hy]] client as a base but have not had success.

The major issue I encountered is that the python process spawned does not seem response. [Search results for uv.spawn("python"...)](https://github.com/search?q=uv.spawn%28%22python%22%29&type=code) are very siilar to what is done in Conjure.

Some relevant information:

- [Initial Python client support · Issue #134 · Olical/conjure](https://github.com/Olical/conjure/issues/134)


## Setting up dev environment

- Make sure python is installed
- Install the treesitter grammar for python in, otherwise the form evaluations won't work and there will not be an error
  - `TSInstall python`
- Install IPython
  - `python3 -m pip install IPython`
- Install matplot lib
  - `python3 -m pip install matplotlib`
  - Note that this will not work in [[os.windows.wsl2]]. You will see the following error
  > UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.↵