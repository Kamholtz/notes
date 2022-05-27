---
id: 2torquuzh3kpr666gisn7ir
title: Solar Charging
desc: ''
updated: 1653305971967
created: 1653116476988
---

## Power Path using a P-channel MOSFET

[[ee.hw.tp4056]] and [[ee.hw.dw01A]] with power path using [[ee.hw.fqp27p06]].

- Solar panel voltage present results in power supplied to MCU via solar panel only + battery continues charging

![](/assets/images/2022-05-21-17-04-01.png)

- Source: [#383 Cheap and simple Solar Power for our small Projects (ESP32, ESP8266, Arduino)](https://www.youtube.com/watch?v=37kGva3NW8w)


- Discussion on when the solar voltage is somewhere between 0-5V, where the P-channel mosfet is still on
  - [Solar powered LIPO charger with power path - Page 1](https://www.eevblog.com/forum/projects/solar-powered-lipo-charger-with-power-path/)
  - Andreas Spiess design is almost identical to that shown in the [[ee.hw.mcp73837-li-ion-battery-charger]] application note
  - ![[Application Note|ee.hw.mcp73837-li-ion-battery-charger#application-note]]

## Related Discussions

- [r/AskElectronics - Methods for charging and load sharing between solar panels and li-ion batteries?](https://www.reddit.com/r/AskElectronics/comments/kgujq9/methods_for_charging_and_load_sharing_between/)

- [Help with li-ion solar charging with load-sharing](https://forum.arduino.cc/t/help-with-li-ion-solar-charging-with-load-sharing/655618)

- [r/AskElectronics - Looking for an IC/circuit that would allow me to safely charge a lipo battery that is still connected to a device (like a cellphone)](https://www.reddit.com/r/AskElectronics/comments/po8q3c/looking_for_an_iccircuit_that_would_allow_me_to/)

  - > Anything that lists 1) powerpath, 2) Vsys output, or 3) uses an external current sense resistor should work fine - so BQ25606, CN3791, STNS01 (if your phone's current draw is unusually low), but not TP4056 or MCP738xx.

    - [[ee.hw.cn3791-solar-mppt-approx-charger]] (for solar with MPPT approximation)
    - [[ee.hw.bq25606-buck-lipo-battery-charger]] (not specifically for solar or MPPT like)
    - [[ee.hw.stns01-li-ion-linear-battery-charger-with-ldo]] - Package and LDO make it unsuitable for my needs as the [[ee.nrf52840]] has an inbuilt DC converter so regulating twice would be inefficient

    - Although [[ee.hw.tp4056]] and [[ee.hw.mcp73837-li-ion-battery-charger]] do not have an external current sense resistor, a power path can be created used the application not for the MCP73837 mentioned in [[Power Path using a P-channel MOSFET|ee.hw.solar-charging#power-path-using-a-p-channel-mosfet]]

  - > The reason for these precautions is that lithum-ion batteries do not like being float-charged (held at 4.2v while current asymptotes to zero) as it causes them to grow dendrites and stab themselves to a fiery death.

## Solar Calculations

[Solar Irradiance Calculator](http://www.solarelectricityhandbook.com/solar-irradiance.html)
[Solar resource maps of Australia](https://solargis.com/maps-and-gis-data/download/australia)

## To Continue With

- Great Scott video [Electronic Basics #29: Solar Panel and Charge Controller](https://www.youtube.com/watch?v=sU-hSFFwSmo&t=2s)
- A final year EE project
  - [My Final Year Project: NiMH Solar Battery Charger](https://www.youtube.com/watch?v=Oz_6qOgm4-g)
    - [solar-charger-arduino-nano-v3/schematic.png at 06923ca40dcb1bf5046b793ef778ebeff19c3275 · hadefuwa/solar-charger-arduino-nano-v3](https://github.com/hadefuwa/solar-charger-arduino-nano-v3/blob/06923ca40dcb1bf5046b793ef778ebeff19c3275/schematic.png)

- Google sheet with solar battery chargers [SolarBatteryChargers](https://docs.google.com/spreadsheets/d/1LVohmn0nc7Ttsbt9npN3JESeZj8wxoR_L95ZPLOyowU/edit#gid=0)
  - Unsure where I found this...
