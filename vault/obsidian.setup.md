---
id: OK438JlkQKGS75dmFKYfB
title: Setup
desc: ''
updated: 1643507634585
created: 1643501302411
---

## Files and Links

- Where to create new notes

  ![](assets/images/20220130092308.png)

- Where to store attachments/images

  ![](assets/images/20220130092423.png)

- Relative links
  - Using `Shortest path when possible` will result in pasted images being linked to incorrectly
    - The image will be copied (corectly) into `assets/images` but the link will look like `![](img.png)` where there is no path specified. Dendron will not be able to resolve the image's location

    ![](assets/images/20220130092446.png)

- Use markdown links if you mostly add images, use wiki-links if you mostly write notes linking to other notes (this will be further addressed in the plugins section)


## Plugins

### Wikilinks to MDLinks

[agathauy/wikilinks-to-mdlinks-obsidian: An Obsidian md plugin which allows for the conversion of individually selected wikilinks to markdown links, and vice versa. (github.com)](https://github.com/agathauy/wikilinks-to-mdlinks-obsidian)

- To be explored...
  - Goal is to paste images as "markdown links" and create note links as "wiki links"

### Breadcrumbs

#### Views

##### Trail/Grid/Juggl

- Enable showing trail view for `up` in `Limit Trail View to only show certain fields`

  ![](assets/images/20220130093924.png)

- Specify `Index Notes(s)` as `root` (yet to see this actually take effect in trail-view)

  ![](assets/images/20220130094001.png)

#### Alternative Hierarchies

##### Dendron Notes

- Enable `Add Dendron notes to graph`

  ![](assets/images/20220130094021.png)

- Enable `Trim Dendron Note Names` (useful on mobile) and in "trail view"

  ![](assets/images/20220130094034.png)

## Outstanding Issues

- [ ] Look into how to paste images with a custom name
  - Images with spaces in the name (represented as `%`) do not get displayed in Dendron. Obisidian creates filenames with spaces for pasted images by default
  - Example: `![](assets/images/Pasted%20image%2020220130092423.png)`
    - [File links with spaces · Issue #2228 · dendronhq/dendron](https://github.com/dendronhq/dendron/issues/2228)
    - [Bug: Image Markdown fails with spaces and caps in name of file · Issue #200 · dendronhq/dendron](https://github.com/dendronhq/dendron/issues/200)

  - Workaround: immediately rename the file within Obsidian to not have spaces
    - Obsidian will update the reference to the file