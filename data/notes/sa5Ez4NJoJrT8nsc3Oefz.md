
## VSCode installation

[Installing dependencies - nRF Connect extensions for VS Code](https://nrfconnect.github.io/vscode-nrf-connect/connect/install.html)

## Documentation

[About the nRF Connect SDK &mdash; nRF Connect SDK 1.8.99 documentation](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/nrf/introduction.html#documentation-pages)
## Software Configuration


> The single .config file in the <build_dir>/zephyr/ directory describes the entire software configuration of the constructed binary.


### Temporary SDK changes

- Edit `.config`
- Changes are lost during `pristine` build

[Modifying an application &mdash; nRF Connect SDK 1.8.99 documentation](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/nrf/gs_modifying.html#changing-the-configuration-permanently)

### Permanent SDK changes

- Modify `.prj.conf`

[Modifying an application &mdash; nRF Connect SDK 1.8.99 documentation](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/latest/nrf/gs_modifying.html#changing-the-configuration-permanently)