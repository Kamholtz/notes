---
id: 2bb19545-9d75-46c1-a477-f0c05f0135a2
title: Learning
desc: ''
updated: 1615358908148
created: 1614041547384
---

## Shortcuts

- [ ] Determine what is bound to `ctrl + L` which interferes with using dendron's schema lookup
  - Vscode Neovim seems to be using keybinding. Will need to find a different one.
- [x] It's possible to reference/embed a note and specify a range from one heading to another
  - Yes, see [Block Range Reference](https://dendron.so/notes/f1af56bb-db27-47ae-8406-61a98de6c78c.html#block-reference) and [Wildcard Header Reference](https://dendron.so/notes/f1af56bb-db27-47ae-8406-61a98de6c78c.html#wildcard-header-reference)
- [ ] Is it possible to refactor a markdown heading and have links update accordingly
- [ ] Update hierarchy to start with org.*
  - e.g. org.wr.reports...
  - org.fp.projects...
- [ ] "before" icons on tags [CSS: :before and :after pseudo elements in practice](https://krasimirtsonev.com/blog/article/CSS-before-and-after-pseudo-elements-in-practice)
  - Make one for backups and journals

```css

/* Please visit the URL below for more information: */
/*   https://shd101wyy.github.io/markdown-preview-enhanced/#/customize-css */

.markdown-preview.markdown-preview {
  // modify your style here
  // eg: background-color: blue;

  a[href*="correspondence"] {
    background-color: azure;
  }
  a[href*="correspondence"]::before {
    content: "✉️"
  }

  a[href*=".tags."], a[href*=".people."] {
    color: rgb(0, 0, 0);
    background: rgb(255, 255, 255);
    // display: inline-block;
    padding: 0 10px;
    border-radius: 4px;
    border: 1px none black;
    margin: 1px 1px;
    font-style: italic;
  }

  a[href*=".people."] {
    border: 1px dashed black;
  }

  a[href*=".people."]::before {
    content: "🧍 ";
    font-style: normal;
  }

  a[href*=".tags.w"] {
    color: rgb(0, 0, 0);
    background: rgb(255, 220, 23);
  }

  a[href*=".tags.c"] {
    color: rgb(255, 255, 255);
    background: rgb(255, 23, 23);
  }

  a[href*="fp.people."] {
    background: rgb(8, 105, 184);
    color: white;
  }

  a[href*="wr.people."] {
    background: rgb(186, 214, 255);
  }
  a[href*="ca.people."] {
    background: rgb(74, 236, 10);
  }
}

```
