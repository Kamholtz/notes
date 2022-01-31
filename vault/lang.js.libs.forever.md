---
id: c273c482-8138-4e6d-92ad-cfc86158afd8
title: Forever
desc: ''
updated: 1620452942184
created: 1620452392637
---

[forever](https://www.npmjs.com/package/forever)

## CLI

### Starting a Daemon

Using `start` as an argument for the CLI will start a daemon

### Viewing all running 'forever' processes

`forever list`

### Stopping Daemons

`forever stop all`
`forver stop MY_UID`

### Configuration file

Example

> .
> ├── forever
> │   └── development.json
> └── index.js
>
> // forever/development.json
> {
> // Comments are supported
> "uid": "app",
> "append": true,
> "watch": true,
> "script": "index.js",
> "sourceDir": "/home/myuser/app",
> "logFile": "/home/myuser/logs/forever.log",
> "outFile": "/home/myuser/logs/out.log",
> "errFile": "/home/myuser/logs/error.log"
> }

Which can be used like so:

```bash
forever start ./forever/development.json
```

#### Parameters

##### uid

This will be the name of the process. It can be used in commands such as...

`forever stop MY_UID`
