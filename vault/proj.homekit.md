---
id: 5a309fbb-a682-4852-8291-db915692fe84
title: Homekit
desc: ''
updated: 1619353654835
created: 1619353330617
---

[AC control · Issue #57 · Mixiaoxiao/Arduino-HomeKit-ESP8266](https://github.com/Mixiaoxiao/Arduino-HomeKit-ESP8266/issues/57)


## ESP Homekit Library

[maximkulkin/esp-homekit](https://github.com/maximkulkin/esp-homekit)

Possibly meant to be used with[SuperHouse/esp-open-rtos](https://github.com/SuperHouse/esp-open-rtos)

Contains an enum with AC/heater


```c
typedef enum {
	...
    homekit_accessory_category_heater = 20,
    homekit_accessory_category_air_conditioner = 21,
	...
   mekit_accessory_category_t;
```

### Relevant question on AC

[Question for Air Conditioner accessory  · Issue #119 · maximkulkin/esp-homekit-demo](https://github.com/maximkulkin/esp-homekit-demo/issues/119)


## ESP homekit devices

Looks promising but does not seem to support heater/cooler services

[RavenSystem/esp-homekit-devices](https://github.com/RavenSystem/esp-homekit-devices/wiki/Accessory-Types)