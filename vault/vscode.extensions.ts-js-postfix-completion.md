---
id: 9af717c1-e857-46c1-8ddb-d4eed1d405df
title: TS/JS Postfix Completion
desc: ''
updated: 1616561728102
created: 1616472964162
---


[TS/JS postfix completion - Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=ipatalas.vscode-postfix-ts)

| Template        | Outcome                                                                      |
| --------------- | ---------------------------------------------------------------------------- |
| `.if`           | `if (expr)`                                                                  |
| `.else`         | `if (!expr)`                                                                 |
| `.null`         | `if (expr === null)`                                                         |
| `.notnull`      | `if (expr !== null)`                                                         |
| `.undefined`    | `if (expr === undefined) or if (typeof expr === "undefined") (see settings)` |
| `.notundefined` | `if (expr !== undefined) or if (typeof expr !== "undefined") (see settings)` |
| `.for`          | `for (let i = 0; i < expr.Length; i++)`                                      |
| `.forof`        | `for (let item of expr)`                                                     |
| `.foreach`      | `expr.forEach(item => )`                                                     |
| `.not`          | `!expr`                                                                      |
| `.return`       | `return expr`                                                                |
| `.var`          | `var name = expr`                                                            |
| `.let`          | `let name = expr`                                                            |
| `.const`        | `const name = expr`                                                          |
| `.log`          | `console.log(expr)`                                                          |
| `.error`        | `console.error(expr)`                                                        |
| `.warn`         | `console.warn(expr)`                                                         |
| `.cast`         | `(<SomeType>expr)`                                                           |
| `.castas`       | `(expr as SomeType)`                                                         |
| `.new`          | `new expr()`                                                                 |
| `.promisify`    | `Promise<expr>`                                                              |
