---
id: b511f194-865d-4929-97b9-c1a655c8857d
title: Getting Started
desc: ''
updated: 1619698369484
created: 1619612875925
---

## Browser + NodeJs Target

[A beginner guide to compile ClojureScript with shadow-cljs](https://jiyinyiyong.medium.com/a-beginner-guide-to-compile-clojurescript-with-shadow-cljs-26369190b786)


[Shadow CLJS User&#8217;s Guide](https://shadow-cljs.github.io/docs/UsersGuide.html#js-deps)

### Issues

> No available JS runtime.
> See https://shadow-cljs.github.io/docs/UsersGuide.html#repl-troubleshootingNo available JS runtime.

Make sure you connect to the running app with the following. If you don't, the JS runtime will not be available.

```bash
shadow-cljs watch app
# in another terminal
node target/main.js
```


