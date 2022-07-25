

Was able to enable RTT in this commit:

- [Added RTT to project. UART logging currently disabled · Kamholtz/zb-lightbulb@deb2d83](https://github.com/Kamholtz/zb-lightbulb/commit/deb2d83f60a54c541c4faaa8d580b703f5ae2e4f)

  - light_bulb_dongle/prj.conf

  - The solution was somewhat excessive. [nRF Connect docs on RTT](https://devzone.nordicsemi.com/f/nordic-q-a/70628/adding-rtt-to-basic-nrf-connect-sdk-blinky-example-not-working-with-nrf5340dk) indicate that only the following `prj.conf` lines are required to enable RTT but I did not find that to be the case:

    ```ini
    CONFIG_USE_SEGGER_RTT=y
    CONFIG_RTT_CONSOLE=y
    CONFIG_UART_CONSOLE=n
    ```

- I suspect `CONFIG_LOG_BACKEND_RTT=y` is mandatory, but the rest will take experimenting to deterine if they are too

- The added config was found by comparing the diff on `build/zephr/.config` files in the [Logging](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/zephyr/samples/subsys/logging/logger/README.html) example against my project and finding the differences.

### Example of adding RTT to blinky sample

[Testing an application - nRF Connect SDK 1.9.99 documentation](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/nrf/gs_testing.html#testing-rtt)

- Have not been able to do the same
  - Not sure if VSCode isn't showing the output or if it's not configured properly
