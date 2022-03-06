---
id: he1iazncbd7uor02fhw4u4v
title: Quirks
desc: ''
updated: 1646550333750
created: 1646539785729
---

Components of a quirk

- Signature - To identify and apply the correct quirk
- Replacement - To allow Zigpy and ZHA to correctly work with the device
- device_automation_triggers - To let the Home Assistant Device Automation engine and users interact with the device

## Example of Tradfri 5 Button Remote Quirk

[zha-device-handlers/fivebtnremotezha.py at dev · zigpy/zha-device-handlers](https://github.com/zigpy/zha-device-handlers/blob/dev/zhaquirks/ikea/fivebtnremotezha.py)

### device_automation_triggers

```python
 device_automation_triggers = {
        (SHORT_PRESS, TURN_ON): { # Indicates the text the user will see in the triggers UI
            # Uniquely match the event
            COMMAND: COMMAND_TOGGLE, # Command ID for the specific cluster
            CLUSTER_ID: 6, # On off cluster ID
            ENDPOINT_ID: 1, # Arbitrary endpoint ID - this limits the flexibility of creating custom zigbee devices without also generating a custom quirk for each endpoint
        },
        (LONG_PRESS, TURN_ON): {
            COMMAND: COMMAND_RELEASE, # Not sure which command this is, the scenes cluster doesn't specify a command named "release"
            CLUSTER_ID: 5, # scenes
            ENDPOINT_ID: 1,
            ARGS: [],
        },
        (SHORT_PRESS, DIM_UP): {
            COMMAND: COMMAND_STEP_ON_OFF,
            CLUSTER_ID: 8,
            ENDPOINT_ID: 1,
            ARGS: [0, 43, 5], # Argument for the command
        },
        (LONG_PRESS, DIM_UP): {
            COMMAND: COMMAND_MOVE_ON_OFF,
            CLUSTER_ID: 8,
            ENDPOINT_ID: 1,
            ARGS: [0, 83],
        },
        (SHORT_PRESS, DIM_DOWN): {
            COMMAND: COMMAND_STEP,
            CLUSTER_ID: 8,
            ENDPOINT_ID: 1,
            ARGS: [1, 43, 5],
        },
        (LONG_PRESS, DIM_DOWN): {
            COMMAND: COMMAND_MOVE,
            CLUSTER_ID: 8,
            ENDPOINT_ID: 1,
            ARGS: [1, 83],
        },
        (SHORT_PRESS, LEFT): {
            COMMAND: COMMAND_PRESS,
            CLUSTER_ID: 5,
            ENDPOINT_ID: 1,
            ARGS: [257, 13, 0],
        },
        (LONG_PRESS, LEFT): {
            COMMAND: COMMAND_HOLD,
            CLUSTER_ID: 5,
            ENDPOINT_ID: 1,
            ARGS: [3329, 0],
        },
        (SHORT_PRESS, RIGHT): {
            COMMAND: COMMAND_PRESS,
            CLUSTER_ID: 5,
            ENDPOINT_ID: 1,
            ARGS: [256, 13, 0],
        },
        (LONG_PRESS, RIGHT): {
            COMMAND: COMMAND_HOLD,
            CLUSTER_ID: 5,
            ENDPOINT_ID: 1,
            ARGS: [3328, 0],
        },
    }
```