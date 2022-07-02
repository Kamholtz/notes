---
id: lnab25me8lq1jatowu29nr5
title: Power Consumption
desc: ''
updated: 1656724054946
created: 1656722879364
---

## Goals

reduce the power consumption for [[ee.zb.router]] and [[ee.zb.end-device]]


## Questions

### What kind of devices can be sleepy end devices

- lights
- switches?


### What is the expected power consumption for the different modes

- NRF Connect docs suggest it is possible to achieve `~1.8 uA` current draw for the MCUs mentioned below as a [[ee.zb.sleepy-end-device]]
  - Turn off UART by setting CONFIG_SERIAL to n.
  - For current measurements for the nRF52840 DK (PCA10056), the nRF52833 DK (PCA10100), or the nRF5340 (PCA10095), set SW6 to nRF ONLY position to get the desired results.
  - Enable the `CONFIG_RAM_POWER_DOWN_LIBRARY` Kconfig option.
- For this feature to work, make sure to call the `zb_set_rx_on_when_idle()` ZBOSS API, as described in Configuring sleepy behavior for end devices in the ZBOSS documentation
- [Configuring Zigbee in nRF Connect SDK &mdash; nRF Connect SDK 2.0.99 documentation](http://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/nrf/ug_zigbee_configuring.html#power-saving-during-sleep)

### What happens during [[ee.nrf-connect-sdk.zb.sleepy-end-device]] behaviour for the [[ee.nrf52840]]?

- Do pins maintain state?
- is RAM lost?

## Findings
