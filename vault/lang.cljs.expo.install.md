---
id: yrtsvo9ylwmcoz8svps5kko
title: Install
desc: ''
updated: 1650106637688
created: 1649066675383
---
API Reference

[API Reference - Expo Documentation](https://docs.expo.dev/versions/latest/)


- expo-cli

  ```bash
  npm install --global expo-cli
  ```

- Clojure/Java: [[Install|lang.clj.install]]

- shadow-cljs
  - `yarn add --dev shadow-cljs`
  - [Shadow CLJS User&#8217;s Guide](https://shadow-cljs.github.io/docs/UsersGuide.html#_installation)

- Expo go on iOS
  - Try
  - [Introduction - Expo Documentation](https://docs.expo.dev/development/introduction/)

## Disable hot reload

Expo hot reload interferes with CLJS hot reload. Disable expo hot reload with the following steps:

- Install expo webpack

[@expo/webpack-config](https://www.npmjs.com/package/@expo/webpack-config)

```bash
expo customize:web
```

- Prevuous step will generate a `webpack.config.js` file. Add the following to the config:

```js
config.devServer.watchOptions.ignored = [/.*/];
```

- Used [initial setup · armincerf/kalm-mobile@ff1ecf7](https://github.com/armincerf/kalm-mobile/commit/ff1ecf72bf9028671964d6ee38ee42585692d3c1#diff-1fb26bc12ac780c7ad7325730ed09fc4c2c3d757c276c3dacc44bfe20faf166f) as a reference

## Limitations

[Limitations - Expo Documentation](https://docs.expo.dev/introduction/why-not-expo/)

## Resources

- [ClojureScript + React Native](https://cljsrn.org/)

### CLJS cheat sheet

![[lang.cljs.resources]]

### Forum

[Forums](https://forums.expo.dev/)


## js-interop

[GitHub - applied-science/js-interop: A JavaScript-interop library for ClojureScript.](https://github.com/applied-science/js-interop)


## TSX

> Developer tools running on http://localhost:19002
> ? It looks like you're trying to use TypeScript but don't have the required dependencies installed. Would you like to
> install typescript, @types/react, @types/react-native? » (Y/n)

### Kalm Routines

[JUXT Blog - Writing Mobile apps in ClojureScript in 2021](https://www.juxt.pro/blog/clojurescript-native-apps-2021)

By the same developer:

- [Making a mobile app with ClojureScript in 2021 - Alex's Blog](https://www.armincerf.com/2021/07/making-a-mobile-app-with-clojurescript-in-2021)

Videos of REPL + app development

[Making a clojurescript mobile app in 2021](https://www.youtube.com/playlist?list=PLHwZuyvdryX34MXqiq9Jb_NaQE0bvgxgw)

## Learning

[[lang.cljs.libs.react]]

Wrapping


## Features

Health kit integration using EAS Build
- [Apple HealthKit/Google Fit Data | Voters | Expo](https://expo.canny.io/feature-requests/p/apple-healthkitgoogle-fit-data)
- [EAS Build - Expo Documentation](https://docs.expo.dev/build/introduction/)

## Template

[create-expo-cljs-app](https://www.npmjs.com/package/create-expo-cljs-app)
- See instructions on page


Success! Created bin-day at C:\Users\carlk\repos\bin-day
Inside that directory, you can run several commands:

```bash
  shadow-cljs watch app
```

Starts the shadow compiler.

```bash
  yarn start
```

Starts the javascript bundler.

Get started by:
```bash
cd bin-day
shadow-cljs watch app
```

Then in another terminal session run:

```bash
  cd bin-day
  yarn start
```

Then in the Expo Client Open this app.

[GitHub - jgoodhcg/create-expo-cljs-app](https://github.com/jgoodhcg/create-expo-cljs-app#readme)