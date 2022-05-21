---
id: 2torquuzh3kpr666gisn7ir
title: Solar Charging
desc: ''
updated: 1653119852047
created: 1653116476988
---

[[ee.hw.tp4056]] and [[ee.hw.dw01A]] with power path using [[ee.hw.fqp27p06]].

- Solar panel voltage present results in power supplied to MCU via solar panel only + battery continues charging

![](/assets/images/2022-05-21-17-04-01.png)

- Source: [#383 Cheap and simple Solar Power for our small Projects (ESP32, ESP8266, Arduino)](https://www.youtube.com/watch?v=37kGva3NW8w)


## Related Discussions

- [r/AskElectronics - Methods for charging and load sharing between solar panels and li-ion batteries?](https://www.reddit.com/r/AskElectronics/comments/kgujq9/methods_for_charging_and_load_sharing_between/)

- [Help with li-ion solar charging with load-sharing](https://forum.arduino.cc/t/help-with-li-ion-solar-charging-with-load-sharing/655618)

- [r/AskElectronics - Looking for an IC/circuit that would allow me to safely charge a lipo battery that is still connected to a device (like a cellphone)](https://www.reddit.com/r/AskElectronics/comments/po8q3c/looking_for_an_iccircuit_that_would_allow_me_to/)

  - > Anything that lists 1) powerpath, 2) Vsys output, or 3) uses an external current sense resistor should work fine - so BQ25606, CN3791, STNS01 (if your phone's current draw is unusually low), but not TP4056 or MCP738xx.

    - [[ee.hw.cn3791]]

  - > The reason for these precautions is that lithum-ion batteries do not like being float-charged (held at 4.2v while current asymptotes to zero) as it causes them to grow dendrites and stab themselves to a fiery death.