---
id: UTyVZZrIY615EpsVASnyB
title: Dongle
desc: ''
updated: 1652510133044
created: 1644056764210
---

## Datasheet

[https://infocenter.nordicsemi.com/pdf/nRF52840_Dongle_User_Guide_v1.0.pdf](https://infocenter.nordicsemi.com/pdf/nRF52840_Dongle_User_Guide_v1.0.pdf)

## Pinout

![](assets/images/2022-02-05-20-26-18.png)

## Layout

![](assets/images/2022-02-10-21-40-45.png)

## Buttons and LEDs

![](assets/images/2022-02-10-21-33-13.png)

| Part | Description | GPIO |
| ---- | ----------- | ---- |
| SW1 | Button | P1.06 |
| SW2 | Reset | P0.18 (1) |
| LD1 | Green | P0.06 |
| LD2 | Red | P0.08 |
| LD2 | Green | P1.09 |
| LD2 | Blue | P0.12 |

- What do the GPIO numbers mean?


> 1) SW2 is also connected to P0.19, P0.21, P0.23, and P0.25. This is done to simplify PCB routing. These
> GPIOs should not be used and should be left as input with no pull or be disconnected by firmware.

## Zephyr Docs

[[ee.zephyr]]
[nRF52840 Dongle - Zephyr Project Documentation](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/zephyr/boards/arm/nrf52840dongle_nrf52840/doc/index.html)

## Programming the dongle

[How to use the NRF52840 Dongle (PCA10059) as development board](https://jimmywongiot.com/2019/10/25/how-to-use-the-nrf52840-dongle-pca10059-as-development-board/)

![[Usage|ee.nrfutil#usage]]