---
id: fe3d08bb-d6f0-4d4b-9a4d-3eae285c8f70
title: VSCode
desc: ''
updated: 1643628673416
created: 1613968506296
---



- [x] Investigate Dendron
- [ ] investigate NeoVim Ui Modifier
- [ ] Code chunks in Markdown Preview Enhanced
- [ ] Vspacecode for [[dendron]]

```json
{"vspacecode.bindingOverrides": [
    {
      "keys": "n",
      "name": "Notes+",
      "type": "bindings",
      "bindings": [
        {
          "key": "j",
          "name": "Open today's Dendron journal",
          "type": "command",
          "command": "dendron.createDailyJournalNote"
        },
        {
          "key": "p",
          "name": "Open Dendron preview",
          "type": "command",
          "command": "dendron.showPreview"
        },
        {
          "key": "s",
          "name": "Lookup a Dendron schema",
          "type": "command",
          "command": "dendron.lookupSchema"
        },
        {
          "key": "l",
          "name": "Lookup a Dendron note",
          "type": "command",
          "command": "dendron.lookup"
        },
        {
          "key": "g",
          "name": "Open Dendron graph",
          "type": "command",
          "command": "dendron.showNoteGraph"
        },
        {
          "key": "r",
          "name": "Rename note",
          "type": "command",
          "command": "dendron.renameNote"
        }
      ]
    }
  ],
}
```

![[vscode.extensions.*]]
