---
id: kWFdZQuRbvz7uwXfqCA8n
title: Nrf52840
desc: ''
updated: 1644729955555
created: 1644491156028
stub: true
---


## Datasheet

[https://infocenter.nordicsemi.com/pdf/nRF52840_PS_v1.1.pdf](https://infocenter.nordicsemi.com/pdf/nRF52840_PS_v1.1.pdf)



### 6.17 PWM

- 4 PWM Channels
- Can PWM be used on any GPIO?

#### PWM Zephyr Bindings

[[ee.zephyr.bindings]]

The `chn-pin` (`n=0,1,2,3`) properties are a little confusing. As an example, the [[ee.zephyr.device-tree]] for the dongle straightforwardly sets `ch0-pin = < 0x8 >` to map channel 0 to to pin `P0.8`. In contrast, `ch1-pin = < 0x29 >` maps to pin `P1.9`:

```js
    pwm0: pwm@4001c000 {
        compatible = "nordic,nrf-pwm";
        reg = < 0x4001c000 0x1000 >;
        interrupts = < 0x1c 0x1 >;
        status = "okay";
        label = "PWM_0";
        #pwm-cells = < 0x1 >;
        ch0-pin = < 0x8 >;
        ch0-inverted;
        ch1-pin = < 0x29 >;
        ch1-inverted;
        ch2-pin = < 0xc >;
        ch2-inverted;
        phandle = < 0x5 >;
    };
```

The note on `ch0-pin` in [nordic,nrf-pwm - Zephyr Project Documentation](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/zephyr/reference/devicetree/bindings/pwm/nordic%2Cnrf-pwm.html#dtbinding-nordic-nrf-pwm) explains the difference in mappings:

> The channel 0 pin to use.
>
> For pins P0.0 through P0.31, use the pin number. For example,
> to use P0.16 for channel 0, set:
>
> ch0-pin = <16>;
>
> For pins P1.0 through P1.31, add 32 to the pin number. For
> example, to use P1.2 for channel 0, set:
>
> ch0-pin = <34>;  /* 32 + 2 */

### 7 Hardware and layout

#### 7.1 Pin assignment

p 576

## Zephyr

[[ee.zephyr]]

### Bindings Documentation

[nordic,nrf-pwm - Zephyr Project Documentation](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/zephyr/reference/devicetree/bindings/pwm/nordic%2Cnrf-pwm.html#dtbinding-nordic-nrf-pwm)