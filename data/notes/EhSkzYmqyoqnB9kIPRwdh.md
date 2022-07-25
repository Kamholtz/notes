
![](assets/images/2021-08-10-10-57-12.png)

## Issue

[Cannot start the website because administrative privileges are required to bind to the hostname or port](https://realmpkdotnet.wordpress.com/2015/11/16/cannot-start-the-website-because-administrative-privileges-are-required-to-bind-to-the-hostname-or-port/)

## Solution

-  Delete the following from  [[ams.files.AMS.csproj]]
  - DevelopmentServerPort
  - IISUrl

  ![](assets/images/2021-08-20-10-29-03.png)
