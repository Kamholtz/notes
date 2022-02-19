---
id: 4PuwOPO63AOwRwcaNwrUX
title: Logging
desc: ''
updated: 1645259764814
created: 1645246995788
---

## RTT

- Enabled with minimum config in this commit [Minimal config for RTT · Kamholtz/zb-lightbulb@019d5a1](https://github.com/Kamholtz/zb-lightbulb/commit/019d5a1a003afaa8745cb9480884b6c23e0c9b26)

  ```ini
  CONFIG_USE_SEGGER_RTT=y
  CONFIG_RTT_CONSOLE=y
  CONFIG_UART_CONSOLE=n
  ```

- Source: [Testing an application &mdash; nRF Connect SDK 1.9.99 documentation](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/nrf/gs_testing.html#how-to-use-rtt)

- Relevant Kconfig: [Logging in nRF Connect SDK - nRF Connect SDK 1.9.99 documentation](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/nrf/ug_logging.html#rtt)

- Logging API - [Logging - Zephyr Project Documentation](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/zephyr/reference/logging/index.html#logging-api)

- Investigation notes: [[RTT Investigation|ee.nrf-connect-sdk.logging.rtt-investigation]]


