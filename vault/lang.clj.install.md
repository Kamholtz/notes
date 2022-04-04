---
id: 7ykub1hzou506knsdyx5pf9
title: Install
desc: ''
updated: 1649070433603
created: 1649070433603
---

## Windows

Prerequisites:

- Java installed

  - [Semeru Runtimes Downloads](https://developer.ibm.com/languages/java/semeru-runtimes/downloads)

    - 11.0.14.1
    - OpenJDK 11.0.14.1+1
    - OpenJ9 0.30.1

- `JAVA_HOME` (parent of `bin` directory, not `bin` itself)

[clj on Windows · clojure/tools.deps.alpha Wiki](https://github.com/clojure/tools.deps.alpha/wiki/clj-on-Windows)


Run something like `Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://download.clojure.org/install/win-install-1.11.0.1100.ps1')`

- Actual expression depends on actual latest Clojure version