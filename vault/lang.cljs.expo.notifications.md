---
id: ggshrd5md6uuzfwhexzdebo
title: Notifications
desc: ''
updated: 1649590965969
created: 1649572582786
---

[Notifications - Expo Documentation](https://docs.expo.dev/versions/v40.0.0/sdk/notifications/#setnotificationhandlerhandler-notificationhandler--null-void)


## Interpreting the iOS permissions response

[Notifications - Expo Documentation](https://docs.expo.dev/versions/latest/sdk/notifications/#interpreting-the-ios-permissions-response)

On iOS, permissions for sending notifications are a little more granular than they are on Android. Because of this, you should rely on the NotificationPermissionsStatus's ios.status field, instead of the root status field. This value will be one of the following, accessible under Notifications.IosAuthorizationStatus:

- 0) NOT_DETERMINED: The user hasn't yet made a choice about whether the app is allowed to schedule notifications
- 1) DENIED: The app isn't authorized to schedule or receive notifications
- 2) AUTHORIZED: The app is authorized to schedule or receive notifications
- 3) PROVISIONAL: The application is provisionally authorized to post noninterruptive user notifications
- 4) EPHEMERAL: The app is authorized to schedule or receive[[ notifications for a limited amount of time|lang.cljs.require-local-js-file]]