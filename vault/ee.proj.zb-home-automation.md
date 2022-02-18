---
id: vn4QH8axQkezeOvv8cSG5
title: ZigBee Home Automation
desc: ''
updated: 1645187445231
created: 1645185550463
---

Tags:

- [[ee.nrf52840.dongle]]
- [[ee.nrf-connect-sdk]]

Goals:

- Sensors + lighting to interface with [[ee.ha]] using [[ee.zb]]

## 2022.02.10 - Successfully created a dongle lightbulb router using an example project

Using the example code for a [[ee.zb.coordinator]] found in this thread [How to port the Zigbee Network Coordinator sample from the nRF52840DK to the nRF52840 dongle](https://devzone.nordicsemi.com/f/nordic-q-a/84072/how-to-port-the-zigbee-network-coordinator-sample-from-the-nrf52840dk-to-the-nrf52840-dongle) it was possible to modify it to use the code from [[ee.nrf-connect-sdk.zb.samples.light-bulb]].
 The Relevant commit can be found here [light_bulb_dongle can be built to create zigbee dongle with LEDs · Kamholtz/zb-lightbulb@3f964db](https://github.com/Kamholtz/zb-lightbulb/commit/3f964db20870d26157205e55fd1a7dc484374610)

- [Dongle Coordinator Example Download](https://devzone.nordicsemi.com/cfs-file/__key/communityserver-discussions-components-files/4/network_5F00_coordinator_5F00_dongle.zip)
- [Dongle Coordinator with Shell Download](https://devzone.nordicsemi.com/cfs-file/__key/communityserver-discussions-components-files/4/network_5F00_coordinator_5F00_shell_5F00_dongle.zip)
Next steps:

- [ ] Only illumate the LED that represents the lightbulb
- [ ] Enable and analyze PWM on a GPIO pin that can be used to switch power on an actual light
- [ ] Change the name of the device for each build
- [ ] Learn how to create overlays
  - [[Device Tree|ee.zephyr.device-tree]]
- [ ] USB logging
  - This sample may be relevant `SDK\examples\peripherals\usbd_cdc_acm`
- [ ] RTT
  - [](https://devzone.nordicsemi.com/f/nordic-q-a/70628/adding-rtt-to-basic-nrf-connect-sdk-blinky-example-not-working-with-nrf5340dk)
- [x] Create cmdline script for flashing the dongle

  ![[Usage|ee.nrfutil#usage]]