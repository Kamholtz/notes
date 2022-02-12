---
id: klYXMhJwjd4IVEwl3OFOe
title: ESPHome
desc: ''
updated: 1644654667320
created: 1643519679127
---


## Sensors integrations

Integration of [[ee.sensors.ds18b20]] in ESPHome:

Important points:

- Need to get the address of the individual sensor + specify in ESPHome config
  - How to acquire addresses: [Dallas Temperature Sensor](https://esphome.io/components/sensor/dallas.html#dallas-getting-ids)

## Configuration

General

- Pins in config are "board pins" not "mcu pins"

ESP8266

- Board type: `nodemcu`
