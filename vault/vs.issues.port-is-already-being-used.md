---
id: BOr9xvtqdRfYgFFB
title: Port Is Already Being Used
desc: ''
updated: 1627859304257
created: 1627859162634
---

## Problem


![](/assets/images/2021-08-02-09-06-06.png)

## Solution

[IIS Express Web Server Port Is In Use](https://stackoverflow.com/questions/34898901/iis-express-web-server-port-is-in-use)

Run in powershell as **admin**:

```ps1
netsh http add iplisten ipaddress=::
```