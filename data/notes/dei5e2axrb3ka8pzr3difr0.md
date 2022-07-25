

## Issues

### Tried to register two views with the same name

`react-native-picker-select` depends on an old version of [[lang.js.libs.react-native-picker-picker]] and so it needs to be forced to use the latest version to prevent having two version of the same control being registered

See: [Invariant Violation: Tried to register two views with the same name RNCPicker · Issue #403 · lawnstarter/react-native-picker-select](https://github.com/lawnstarter/react-native-picker-select/issues/403)


NPM solution:

```json
  "overrides": {
    "react-native-picker-select": {
      "@react-native-picker/picker": "2.2.1"
    }
  },
```


Yarn solution

```json
  "overrides": {
    "react-native-picker-select": {
      "@react-native-picker/picker": "2.2.1"
    }
  },
```