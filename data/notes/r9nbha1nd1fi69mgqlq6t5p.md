
Fresh installs of windows come with [[powershell.versions.5.1]] but this does not include `pwsh`. The latest version of powershell is [[powershell.versions.7.1]] which does not come preinstalled on windows. PS5.1 cannot be upgraded to 7.x, it must be installed alongside it

[Powershell: What is pwsh.exe](https://powershellexplained.com/2017-12-29-Powershell-what-is-pwsh/)

The powershell version can be checked with

```pwsh
Get-Host | Select-Object Version
```