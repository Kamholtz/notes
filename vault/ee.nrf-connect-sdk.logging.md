---
id: 4PuwOPO63AOwRwcaNwrUX
title: Logging
desc: ''
updated: 1651144661981
created: 1645246995788
---

## RTT

- Enabled with minimum config in this commit [Minimal config for RTT · Kamholtz/zb-lightbulb@019d5a1](https://github.com/Kamholtz/zb-lightbulb/commit/019d5a1a003afaa8745cb9480884b6c23e0c9b26)

- Add to [[ee.zephyr.config.prj-conf]]:

  ```ini
  CONFIG_USE_SEGGER_RTT=y
  CONFIG_RTT_CONSOLE=y
  CONFIG_UART_CONSOLE=n
  ```

  - Notably **UART had to be disabled**

  - [[vscode.extensions.nrf-terminal]] seems to work intermittently for RTT and UART. I found it was best just to use [[ee.sw.j-link-rtt-viewer]] for RTT and [[ee.sw.putty]] for UART

- Source: [Testing an application - nRF Connect SDK 1.9.99 documentation](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/nrf/gs_testing.html#how-to-use-rtt)

- Relevant Kconfig: [Logging in nRF Connect SDK - nRF Connect SDK 1.9.99 documentation](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/nrf/ug_logging.html#rtt)

- Logging API - [Logging - Zephyr Project Documentation](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/zephyr/reference/logging/index.html#logging-api)

- Investigation notes: [[RTT Investigation|ee.nrf-connect-sdk.logging.rtt-investigation]]

## UART

- Add to [[ee.zephyr.config.prj-conf]]:

  ```ini
  CONFIG_UART_CONSOLE=y
  ```

  - Notably, **enabling this prevents RTT from working**

- [CONFIG_UART_CONSOLE &mdash; Kconfig reference](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/kconfig/CONFIG_UART_CONSOLE.html#config-uart-console)

- The default baud rate appears to be `115200` and and uses the COM port that appears on the USB port used to debug/and program via VSCode. Other UART settings were default as per KiTTY and PuTTY