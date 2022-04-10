---
id: g1hdi46pf8plpddg5gt2wgy
title: Require Local JS File
desc: ''
updated: 1649591256987
created: 1649590965789
---

[How to add shadow cljs watcher on js directory in a re-frame app?](https://stackoverflow.com/questions/59906636/how-to-add-shadow-cljs-watcher-on-js-directory-in-a-re-frame-app)


Basically you put the .js files into the same folder as your .cljs file and then just require it via (:require ["./foo.js" :as foo]). No additional config required.


Might be useful

[export - JavaScript | MDN](https://developer.mozilla.org/en-US/docs/web/javascript/reference/statements/export)


[ClojureScript - Dependencies](https://clojurescript.org/reference/dependencies)