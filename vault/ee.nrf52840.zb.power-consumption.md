---
id: lnab25me8lq1jatowu29nr5
title: Power Consumption
desc: ''
updated: 1656746894628
created: 1656722879364
---

## Goals

reduce the power consumption for [[ee.zb.router]] and [[ee.zb.end-device]]


## Questions

### What kind of devices can be sleepy end devices

- lights
- switches?


### What is the expected power consumption for the different modes

### Sleepy end device

- NRF Connect docs suggest it is possible to achieve `~1.8 uA` current draw for the MCUs mentioned below as a [[ee.zb.sleepy-end-device]]
  - Turn off UART by setting CONFIG_SERIAL to n.
  - For current measurements for the nRF52840 DK (PCA10056), the nRF52833 DK (PCA10100), or the nRF5340 (PCA10095), set SW6 to nRF ONLY position to get the desired results.
  - Enable the `CONFIG_RAM_POWER_DOWN_LIBRARY` Kconfig option.
- For this feature to work, make sure to call the `zb_set_rx_on_when_idle()` ZBOSS API, as described in Configuring sleepy behavior for end devices in the ZBOSS documentation
- [Configuring Zigbee in nRF Connect SDK &mdash; nRF Connect SDK 2.0.99 documentation](http://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/nrf/ug_zigbee_configuring.html#power-saving-during-sleep)

### What happens during [[ee.nrf-connect-sdk.zb.sleepy-end-device]] behaviour for the [[ee.nrf52840]]?

- Do pins maintain state?
- is RAM lost?
  - Suspect not because it's only the radio that needs to turn off

## Findings


## Experiments

2022.07.02

- [ ] Try making a device that just consists of many buttons for controlling devices at home
- [x] Determine baseline current consumption with existing firmware on dongle
  - [Commenting out printing · Kamholtz/zb-lightbulb@23fec57](https://github.com/Kamholtz/zb-lightbulb/commit/23fec578e07bc78841b3462d8552846983d1e72d) had a `7.1mA` consumption with all LEDs off
  - Reduce power consumption
    - [ ] Change from router to end device
      - Currently has `CONFIG_ZIGBEE_ROLE_ROUTER=y` in [[ee.zephyr.config.prj-conf]]... Find the end device equivalent
    - [ ] Enable sleep end device [[ee.zb.sleepy-end-device]]
    - [ ] Disbale UART and RTT
    - [x] Make a test apparatus for measuring power

