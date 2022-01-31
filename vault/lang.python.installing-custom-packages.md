---
id: d0105e20-ee3b-4cd2-b2e8-c31e8c816429
title: Installing custom packages
desc: ''
updated: 1616979236378
created: 1616978909255
---


## Using setuptools

Run the following command on `setup.py`:

```bash
python setup.py develop
```

Where `setup.py` consists of:

```python
import setuptools
setuptools.setup(name="custom_packages")
```

Where "custom_packages" is a folder containing a locally developed package with an `__init__.py` file. The folder is in the same directory as the `setup.py` file.

### Example

[Setup.py for custom packages](gtd\resources\scripts\setup.py)
