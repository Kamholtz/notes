
## Home Assistant Developer Docs - Implementation in Python

[Device Triggers | Home Assistant Developer Docs](https://developers.home-assistant.io/docs/device_automation_trigger/)

- Device triggers are automation triggers that are tied to a specific device and an event or state change. Examples are "light turned on" or "water detected".

- To add support for Device Triggers, an integration needs to have a `device_trigger.py` and:

  - Define a `TRIGGER_SCHEMA`: A dictionary that represents a trigger, such as a device and an event type
  - Create triggers: Create dictionaries containing the device or entity and supported events or state changes as defined by the schema.
  - Attach triggers: Associate a trigger config with an event or state change, e.g. a message fired on the event bus.
  - Add text and translations: Give each trigger a human readable name.
