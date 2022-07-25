
[nRF52840 Dongle Programming Tutorial](https://devzone.nordicsemi.com/guides/short-range-guides/b/getting-started/posts/nrf52840-dongle-programming-tutorial)

## Install

- **Run as admin**

```bash
pip install nrfutil
```

## Usage

Example of usage with thread which is applicable to [[ee.nrf-connect-sdk.zb]]

1. Reset the board into the Nordic bootloader by pressing the RESET button.

  ![Dongle PCB](assets/images/2022-02-18-21-36-10.png)

2. Compile a Zephyr application; we’ll use blinky.

  ```batch
  west build -b nrf52840dongle_nrf52840 zephyr/samples/basic/blinky
  ```

3. Package the application for the bootloader using nrfutil:

  ```batch
  nrfutil pkg generate --hw-version 52 --sd-req=0x00 \
          --application build/zephyr/zephyr.hex \
          --application-version 1 blinky.zip
  ```

  | Flag | Description | Mandatory |
  | ---- | ----------- | --------- |
  | `--hw-version 52` | Hardware version indicating this build is for the dongle | Yes |
  | `--sd-req=0x00` | Presumably this indicates no soft device is required | Yes |
  | `--application build/zephyr/zephyr.hex` | `.hex` file to be packaged` | Yes |
  | `--application-version 1` | App version | No |

4. Flash it onto the board. Note /dev/ttyACM0 is for Linux; it will be something like COMx on Windows, and something else on macOS.

  ```batch
  nrfutil dfu usb-serial -pkg blinky.zip -p /dev/ttyACM0
  ```

Source:

- [nRF52840 Dongle - Zephyr Project Documentation](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/zephyr/boards/arm/nrf52840dongle_nrf52840/doc/index.html?highlight=nrfutil#option-1-using-the-built-in-bootloader-only)
- [Thread tools - nRF Connect SDK 1.9.99 documentation](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/nrf/ug_thread_tools.html?highlight=nrfutil)

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

- Soft devices must be included [Overview of SoftDevices for the nRF5 Series](https://infocenter.nordicsemi.com/topic/ug_gsg_ses/UG/gsg/softdevices.html)
  - Is there one for ZigBee?
    - There does not appear to be one for ZigBee, rather the ZBOSS binary is included in the build?
