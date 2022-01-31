---
id: 9c374c5b-d7aa-43f4-b2f5-94bb68e5c3f1
title: Apt Fix Broken Install
desc: ''
updated: 1619350297689
created: 1619350198716
---

Reading package lists... Done
Building dependency tree
Reading state information... Done
You might want to run 'apt --fix-broken install' to correct these.
The following packages have unmet dependencies:
 emacs25 : Depends: emacs25-common but it is not installed
E: Unmet dependencies. Try 'apt --fix-broken install' with no packages (or specify a solution).

```bash
sudo dpkg -i --force-overwrite /var/cache/apt/archives/emacs27-common_27.1~1.git86d8d76aa3-kk2+18.04_all.deb && sudo apt-get -f install
```
