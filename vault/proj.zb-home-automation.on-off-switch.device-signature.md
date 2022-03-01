---
id: NKSTum1hoqIPue2kQRMKx
title: Device Signature
desc: ''
updated: 1646049786689
created: 1646049395623
---

Ikea on off switch device signature

```json
{
  "node_descriptor": "NodeDescriptor(logical_type=<LogicalType.EndDevice: 2>, complex_descriptor_available=0, user_descriptor_available=0, reserved=0, aps_flags=0, frequency_band=<FrequencyBand.Freq2400MHz: 8>, mac_capability_flags=<MACCapabilityFlags.AllocateAddress: 128>, manufacturer_code=4476, maximum_buffer_size=82, maximum_incoming_transfer_size=82, server_mask=11264, maximum_outgoing_transfer_size=82, descriptor_capability_field=<DescriptorCapability.NONE: 0>, *allocate_address=True, *is_alternate_pan_coordinator=False, *is_coordinator=False, *is_end_device=True, *is_full_function_device=False, *is_mains_powered=False, *is_receiver_on_when_idle=False, *is_router=False, *is_security_capable=False)",
  "endpoints": {
    "1": {
      "profile_id": 260,
      "device_type": "0x0820",
      "in_clusters": [
        "0x0000", // Basic
        "0x0001", // Power config
        "0x0003", // Identify
        "0x0009", // Alarms
        "0x0020", // Poll Control
        "0x1000", // Shade Config
        "0xfc7c"
      ],
      "out_clusters": [
        "0x0003", // Identify
        "0x0004", // Groups
        "0x0006", // On off
        "0x0008", // Level control
        "0x0019", // OTA
        "0x0102", // Window covering
        "0x1000" // Touchlink
      ]
    }
  },
  "manufacturer": "IKEA of Sweden",
  "model": "TRADFRI on/off switch",
  "class": "zhaquirks.ikea.twobtnremote.IkeaTradfriRemote2Btn"
}
```