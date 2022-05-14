---
id: bzx7q88mrdzt3ylj90e8b6v
title: React Native
desc: ''
updated: 1652492505519
created: 1649402877011
---



## Creating Reactive Components

[Slack thread](https://clojurians.slack.com/archives/C073DKH9P/p1649401136457189)

Issue: child component was not updating in response an event which changed data that the child component was subscribed to. Adding the subscription to the parent caused it to update in response to the event, however.

- `r/reactify-component`
- `r/as-element`

> As to your issue, I'm 90% certain that it'll be fixed when you replace (paper/withTheme screen-main) with (paper/withTheme (r/reactify-component)) and remove the call to r/as-element from within screen-main.
>
> The explanation is that by wrapping the body of screen-main in r/as-element, you prevent it from being a part of the reactive context. Any reaction (subscriptions are reactions) used outside of a reactive context cannot trigger re-render.


## Navigation Stack and State Persistence

### NavigationContainer onStateChange and initialState

[NavigationContainer state persistence](https://reactnavigation.org/docs/state-persistence/) describes how to persist state in [[lang.js]]. The [[lang.cljs]] version using an atom is described in the following slack thread:

[Clojurians Slack - NavigationContainer state persistence](https://clojurians.slack.com/archives/C0E1SN0NM/p1652439790706039?thread_ts=1652431961.516389&cid=C0E1SN0NM)

> To persist nav state you could also pass `{:onStateChange on-state-change :initialState @state}` to `NavigationContainer`.
> The code for persisting state could look like:

```clojure
 (defonce state (atom nil))

 (defn- persist-state! [state-obj]
    (js/Promise.
     (fn [resolve _]
       (reset! state state-obj)
       (resolve true))))

  (defn- on-state-change [state]
    (persist-state! state))
```

> And for storing the ref, you could use `useNavigationContainerRef` hook to get the ref. (edited)

### NavigationContainer's resetRoot and getRootState

- Store the state using `getRootState`
- Load it again when the app is reloaded with `resetRoot`

[app-fx.cljs](https://gist.github.com/olivergeorge/981bc5135fa47253cba50fd125495d0b)

### Other approaches I tried or researched

#### AppContainer with persistNavigationState and loadNavigationState

[cljs-react-native-starter/core.cljs at master · eihli/cljs-react-native-starter](https://github.com/eihli/cljs-react-native-starter/blob/master/src/example/core.cljs)

#### Storing in re-frame DB (does not reload it though?)

From Clojurians slack:

> I have a question related to ReactNavigation. I want to be able to reference the root navigator globally. In a regular React I can obtain the reference while rendering a component. How to do the same in CLJS/Reagent?

```clojure
; Store navigator in app db
; Get the navigator from the NavaigationContainer using :ref
(defn app-root []
  [:> appnav/central-app-switch {:ref (fn [this] (dispatch [:set-root-navigator this]))}])


; Effect for navigating
(reg-fx
  :navigate
  (fn [[root-navigator route params]]
    (.dispatch root-navigator (navactions/navigate-to route params))))

; Handler that triggers the effect above
(reg-event-fx
  :handle-login-success
  validate-spec
  (fn [{:keys [db]} [_ session-info]]
    (println db)
    {:db (-> db
         (assoc-in [:dcn-session] (-> session-info
                                      (update-in [:userInfo :gender] keyword)
                                      (update-in [:userInfo :siteRoles] (fn [v] (map #(keyword %) v))))))
     :navigate [(:root-navigator db) :Main]}
    ))
```

### Libraries for storing app state

I ultimately decided not to use any libraries/wrappers for storing state as it seemed like a lot of overhead to include another dependency

- [GitHub - seantempesta/cljs-react-navigation: CLJS wrappers for react-navigation](https://github.com/seantempesta/cljs-react-navigation)

- [GitHub - flexsurfer/rn-shadow-steroid: React Native with shadow-cljs on steroids](https://github.com/flexsurfer/rn-shadow-steroid)
  - Blog post showing how to use `steroid` to perist navigation state [Confidence and Joy: React Native Development with ClojureScript and re-frame - HackMD](https://hackmd.io/@byc70E6fQy67hPMN0WM9_A/rJilnJxE8)
