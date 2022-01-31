---
id: b5541a5b-8f72-4b7e-a7f0-5bedbc0ae647
title: Require
desc: ''
updated: 1619856717458
created: 1619856561132
---

## The ns macro converts :require to require

> Requiring
> As for require statements, I'm assuming you found the former in the form of:

```clojure
(ns my.namespace
    (:require [clojure.set :as set]))

```

> ns is a macro that will transform the :require expression into the latter form you described:

```clojure
(require '[clojure.set :as set])
```

[Clojure : loading dependencies at the REPL](https://stackoverflow.com/questions/9810841/clojure-loading-dependencies-at-the-repl)