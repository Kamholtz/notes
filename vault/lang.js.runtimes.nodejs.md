---
id: 8abd350d-0020-462d-9124-e620166a1515
title: Nodejs
desc: ''
updated: 1619922384498
created: 1619831200263
---

## Upgrading on Ubuntu

[How to Update Node.js to Latest Version {Linux, Windows, and MacOS}](https://phoenixnap.com/kb/update-node-js-version)


1. Start by updating the package repository with the command:

```bash
sudo apt update
```

2. Download the following dependencies by typing:

```bash
sudo apt install build-essential checkinstall libssl-dev
```

3. Install NVM using the curl command:

```bash
curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.35.1/install.sh | bash
```

4. Close and reopen the terminal.

5. Then, verify if you have successfully installed NVM:

```bash
nvm --version
check nvm version to update Node.js
```

6. Before upgrading Node.js, check which version you have running on the system:

```bash
nvm ls
```

7. Now you can check for newly available releases with:

```bash
nvm ls-remote
```

see a list of all available Node.js versions

8. To install the latest version, use the nvm command with the specific Node.js version:

```
nvm install [version.number]
```

e.g.

```
nvm install v14.16.1
```