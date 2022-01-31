---
id: 6207f4f6-3548-49e0-93fa-0e2ea5e41cd6
title: Repl
desc: ''
updated: 1619834374551
created: 1619834182811
---



## Switching namespace

Use `(ns xxx)` where `xxx` is the name space you want to change to. Note that while the function returns `nil` the promp on the repl will now match the namespace name to indicate that you have changed

```clj
server> (ns server.main)
;; => nil
server.main> (main!)
App loaded!
```
