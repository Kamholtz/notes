---
id: 17rny6i5f96msb6qu26913c
title: Csharp Ls
desc: ''
updated: 1647053266488
created: 1647052711698
---

> LSP[csharp_ls][Log] csharp-ls: msbuildWorkspace.Diagnostics: [Failure] Msbuild failed when processing the file 'C:\Users\carlk\source\repos\xxx\xxx.csproj' with message: The imported project "C:\Program Files\dotnet\sdk\6.0.201\Microsoft\VisualStudio\v17.0\WebApplications\Microsoft.WebApplication.targets" was not found. Confirm that the expression in the Import declaration "C:\Program Files\dotnet\sdk\6.0.201\Microsoft\VisualStudio\v17.0\WebApplications\Microsoft.WebApplication.targets" is correct, and that the file exists on disk.  C:\Users\carlk\source\repos\xxx\xxx.csproj

BuildTools is missing `WebApplications\Microsoft.WebApplication.targets` it seems
  -[Microsoft.WebApplication.targets was not found, on the build server. What&#x27;s your solution?](https://stackoverflow.com/questions/3980909/microsoft-webapplication-targets-was-not-found-on-the-build-server-whats-your)


