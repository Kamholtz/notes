
A Zigbee stack


[Developing with ZBOSS for Zigbee : Zigbee stack API overview](https://developer.nordicsemi.com/nRF_Connect_SDK/doc/zboss/3.11.1.0/using_zigbee__z_c_l.html#zigbee_device_imp)

> Zigbee devices are characterized by a set of clusters that have mandatory and optional attributes. To save memory, make sure that only the required attributes and clusters are declared.
>
> Application can either use predefined device declaration (for example, IAS Zone device) or define its own set of clusters and endpoints.
>
> At the highest level, the Zigbee end product implementation consists of the following parts:
>
> Declaration of Zigbee device data structures:
> - Declaring attributes for each cluster (attribute lists),
> - Declaring cluster (or Declaring custom cluster),
> - Declaring cluster list for a device,
> - Declaring endpoint (including runtime context).
>
> Zigbee device executable code:
> - Registering device context (including optional implementation of a handler function for custom ZCL packets),
> - Configuring default ZCL command handler override,
> - Implementing Zigbee device callback (optional),
> - Sending ZCL commands and Parsing ZCL commands according to the application logic.
>