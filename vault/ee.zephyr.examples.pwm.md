---
id: 3FCH9gXvR5hmtBYenyzGk
title: Pwm
desc: ''
updated: 1645097939393
created: 1645097551940
---

Source: [Using a PWM Device in Zephyr](https://medium.com/home-wireless/using-a-pwm-device-in-zephyr-7100d089f15c)

## Zephyr/Devicetree config core points

1. Channel-to-pin:

  ```json
  &pwm0 {
    status = "okay";
    ch0-pin = <33>;
    ch0-inverted;
   };
  ```

2. PWM definition, which matches the pin in the pin-to-channel config above:

  ```json
  aliases {
      pwmsound = &pwm_dev0;
  };
  pwmdevs {
    compatible = "pwm-leds";
    pwm_dev0: pwm_dev_0 {
     pwms = <&pwm0 33>;
    };
   };
  ```

3. Enable PWM in project config `prj.conf`

```json
CONFIG_PWM=y
```

4. Now the PWM channel-to-pin config can be referenced in code e.g. `DT_ALIAS()` or other