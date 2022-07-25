
## Documentation

- ZBOSS: [Developing with ZBOSS : ZCL Occupancy Sensing cluster](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/zboss_api_doc/group___z_b___z_c_l___o_c_c_u_p_a_n_c_y___s_e_n_s_i_n_g.html)

- NXP docs for their API, seems to be useful regardless of MCU as a cross reference, especially since occupancy sensing isn't really implemented by Nordic/ZBOSS: [https://www.nxp.com/docs/en/user-guide/JN-UG-3076.pdf](https://www.nxp.com/docs/en/user-guide/JN-UG-3076.pdf)

  ![Occupancy sensing cluster in NXP guide](assets/images/2022-02-26-15-43-56.png)

  - Useful for checking the dependencies of clusters e.g.

    ![](assets/images/2022-02-26-15-45-35.png)

## Example Zigbee Traffic for Philips Hue

![](assets/images/2022-02-26-15-19-15.png)


## ZCL Specification

![[ee.zb.zcl.measurement-and-sensing.occupancy-sensing]]

## Adding Occupancy Sensing Implementation

![[ee.nrf-connect-sdk.zb.adding-custom-cluster]]

### Investigating Forum Post

[Zigbee Occupancy cluster attribute setting gives Invalid Value error - Nordic Q&amp;A - Nordic DevZone - Nordic DevZone](https://devzone.nordicsemi.com/f/nordic-q-a/60960/zigbee-occupancy-cluster-attribute-setting-gives-invalid-value-error)

Whenever a customer wants to use it, than he has to define:

- Sensor-specific attribute name, e.g.:

  ```c
  #define ZB_ZCL_CLUSTER_ID_OCCUPANCY_SENSING_PIR ZB_ZCL_CLUSTER_ID_OCCUPANCY_SENSING
  ```

- Sensor-specific attribute handlers, e.g.:

  ```c
  #defineZB_ZCL_CLUSTER_ID_OCCUPANCY_SENSING_PIR_SERVER_ROLE_INIT pir_sensor_init
  ```

- The init function has to pass the write attribute hook to the stack, e.g.:

  ```c
  zb_zcl_add_cluster_handlers(ZB_ZCL_CLUSTER_ID_OCCUPANCY_SENSING_PIR,
                                ZB_ZCL_CLUSTER_SERVER_ROLE,
                                check_value_pir_sensor_server,
                                write_attr_pir_sensor_server_hook,
                                (zb_zcl_cluster_handler_t)NULL);
  ```

  - Notice that in `zb_zcl_occupancy_sensing.h` these are not defined as null

    ```c
    #define ZB_ZCL_CLUSTER_ID_OCCUPANCY_SENSING_SERVER_ROLE_INIT (zb_zcl_cluster_init_t)NULL
    #define ZB_ZCL_CLUSTER_ID_OCCUPANCY_SENSING_CLIENT_ROLE_INIT (zb_zcl_cluster_init_t)NULL
    ```

  - Further to this point has the following comment `zb_zcl_comon.h` regarding the `ZB_ZCL_CLUSTER_ID_*_SERVER_ROLE_INIT` and  `ZB_ZCL_CLUSTER_ID_*_SERVER_CLIENT_INIT` `#defines`

  ```c
  /** @brief ZCL Cluster Init Handler. This handler is called on registering device context (@ref
      ZB_AF_REGISTER_DEVICE_CTX). Initialization of the cluster should include @ref
      zb_zcl_add_cluster_handlers call, if any of the cluster handlers are implemented.

      Cluster Init handler is bound to the cluster declaration via ZB_ZCL_CLUSTER_DESC macro. Every
      cluster should implement "<cluster_id>_<cluster_role>_INIT" macro, for example:
      @code
      #define ZB_ZCL_CLUSTER_ID_ON_OFF_SERVER_ROLE_INIT zb_zcl_on_off_init_server
      #define ZB_ZCL_CLUSTER_ID_ON_OFF_CLIENT_ROLE_INIT zb_zcl_on_off_init_client
      @endcode

      If cluster does not have any initialization steps and does not need any cluster handlers,
      Cluster Init handler may be NULL, for example:
      @code
      #define ZB_ZCL_CLUSTER_ID_OCCUPANCY_SENSING_SERVER_ROLE_INIT (zb_zcl_cluster_init_t)NULL
      #define ZB_ZCL_CLUSTER_ID_OCCUPANCY_SENSING_CLIENT_ROLE_INIT (zb_zcl_cluster_init_t)NULL
      @endcode
  */
  ```

  - These are called in `ZB_ZCL_CLUSTER_DESC` for declaring the simple descriptor (`zboss_api_af.h`). See `cluster_id##_SERVER_ROLE_INIT` within the macro

    ```c
    #define ZB_ZCL_CLUSTER_DESC(cluster_id, attr_count, attr_desc_list, cluster_role_mask, manuf_code)         \c
    {                                                                                                          \c
      (cluster_id),                                                                                            \c
      (attr_count),                                                                                            \c
      (attr_desc_list),                                                                                        \c
      (cluster_role_mask),                                                                                     \c
      (manuf_code),                                                                                            \c
      (((cluster_role_mask) == ZB_ZCL_CLUSTER_SERVER_ROLE) ? cluster_id##_SERVER_ROLE_INIT : \c
       (((cluster_role_mask) == ZB_ZCL_CLUSTER_CLIENT_ROLE) ? cluster_id##_CLIENT_ROLE_INIT : NULL)) \c
    }
    ```

## SET_ATTR_DESCR_WITH macro

Use of `ZB_SET_ATTR_DESCR_WITH_xxx` `#define`s found...

- `zb_zcl_common.h`

  ```c
  #define ZB_ZCL_SET_ATTR_DESC(attr_id, data_ptr) ZB_SET_ATTR_DESCR_WITH_##attr_id(data_ptr),
  ```

## Home Assistant recognising previous devices appearing with different names

I would have thought this device record would have been deleted

> [0x6093](Dimable_Light_v0.2): completed configuration
> [0x6093](Dimable_Light_v0.2): stored in registry: ZhaDeviceEntry(name='Nordic Dimable_Light_v0.1', ieee='f4:ce:36:71:26:ac:67:47', last_seen=1645960862.7940586)

## Device Signature Comparison with Philips Device

[[Device Signature|proj.zb-home-automation.occupancy-sensing.device-signature]]

### Occupancy Attribute Reporting appears in Home Assistant!

Have confirmed that occupancy attribute reporting works on first connection

- Commit: [Report occupancy on initialization (just like level and on off) · Kamholtz/zb-lightbulb@0ce322e](https://github.com/Kamholtz/zb-lightbulb/commit/0ce322e55144da43b0584d4284d5edf9fedc2236)

| Test | Success Criteria | Success? |
| ---- | ------ | --- |
| Reboot via push button | Device reconnects | `true` |
| Reboot via removing power cable | Device reconnects | `true` |
