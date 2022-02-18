---
id: 4hqUGCEUyFhWBqlocNhLF
title: Nrfutil
desc: ''
updated: 1645183273267
created: 1644491203985
---

[nRF52840 Dongle Programming Tutorial](https://devzone.nordicsemi.com/guides/short-range-guides/b/getting-started/posts/nrf52840-dongle-programming-tutorial)

## Install

- **Run as admin**

```bash
pip install nrfutil
```

## Usage

Example of usage with thread which is applicable to [[ee.nrf-connect-sdk.zb]] - [Thread tools - nRF Connect SDK 1.9.99 documentation](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/nrf/ug_thread_tools.html?highlight=nrfutil)

> Generate the RCP firmware package:

```batch
nrfutil pkg generate --hw-version 52 --sd-req=0x00 \
 --application build/zephyr/zephyr.hex --application-version 1 build/zephyr/zephyr.zip
```

| Flag | Description | Mandatory |
| ---- | ----------- | --------- |
| `--hw-version 52` | Hardware version indicating this build is for the dongle | Yes |
| `--sd-req=0x00` | Presumably this indicates no soft device is required | Yes |

> Connect the nRF52840 Dongle to the USB port.

> Press the RESET button on the dongle to put it into the DFU mode. The LED on the dongle starts blinking red.

> Install the RCP firmware package onto the dongle by running the following command, with /dev/ttyACM0 replaced with the device node name of your nRF52840 Dongle:

```batch
 nrfutil dfu usb-serial -pkg build/zephyr/zephyr.zip -p /dev/ttyACM0
```

## Troubleshooting

### No moduled named 'constants'

> ModuleNotFoundError: No module named 'constants'

[nrfutil ModuleNotFoundError: No module named constants - Nordic Q&amp;A - Nordic DevZone - Nordic DevZone](https://devzone.nordicsemi.com/f/nordic-q-a/65889/nrfutil-modulenotfounderror-no-module-named-constants)

- Python 3.8.6 seems to be a compatible version

**Solution**: install using python 3.8 with [[lang.python.py-launcher]]

```batch
py -3.8 -m pip install nrfutil
```

Reference:

![[Use a commmand with a specific version e.g. pip|lang.python.py-launcher#use-a-commmand-with-a-specific-version-eg-pip]]


## Notes

- Soft devices must be included
  - Is there one for ZigBee?
    - There does not appear to be one for ZigBee, rather the ZBOSS binary is included in the build?