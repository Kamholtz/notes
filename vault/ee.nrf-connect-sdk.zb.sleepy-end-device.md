---
id: dv1cp7kcj760dht09piu3pj
title: Sleepy End Device
desc: ''
updated: 1652785970796
created: 1652785776853
---

- [[ee.zb.sleepy-end-device]]

> make sure your application calls the `zb_set_rx_on_when_idle()` function with the `ZB_FALSE` parameter, but before starting the ZBOSS stack. This function specifies whether the device should have the radio disabled between the polls to parent.

[Developing with ZBOSS for Zigbee : Programming principles](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/zboss/3.11.2.0/zigbee_prog_principles.html#zigbee_power_optimization_sleepy)

[Configuring Zigbee in nRF Connect SDK &mdash; nRF Connect SDK 1.9.99 documentation](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/nrf/ug_zigbee_configuring.html?highlight=sleepy#sleepy-end-device-behavior)