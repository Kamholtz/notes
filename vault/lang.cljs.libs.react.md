---
id: bzx7q88mrdzt3ylj90e8b6v
title: React
desc: ''
updated: 1649402877011
created: 1649402877011
---



## Creating Reactive Components

- `r/reactify-component`
- `r/as-element`

> As to your issue, I'm 90% certain that it'll be fixed when you replace (paper/withTheme screen-main) with (paper/withTheme (r/reactify-component)) and remove the call to r/as-element from within screen-main.
>
> The explanation is that by wrapping the body of screen-main in r/as-element, you prevent it from being a part of the reactive context. Any reaction (subscriptions are reactions) used outside of a reactive context cannot trigger re-render.