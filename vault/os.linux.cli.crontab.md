---
id: f3ee3132-6e64-4f42-b39c-90ec4fa18ebf
title: Crontab
desc: ''
updated: 1620458806637
created: 1620452489266
---


## Viewing logs

`grep CRON /var/log/syslog`

[Where is the cron / crontab log?](https://askubuntu.com/questions/56683/where-is-the-cron-crontab-log)


## Starting an node project on boot

[How to start node.js app on machine boot by creating a boot service](https://unix.stackexchange.com/questions/441624/how-to-start-node-js-app-on-machine-boot-by-creating-a-boot-service)


> Edit crontab run the following replacing the "USER" with your desired runtime user for the node process. If you choose a different user other than yourself, you will have to run this with sudo.
>
> $ crontab -u USER -e
>
> Once in the editor add the following line:
>
> @reboot /usr/local/bin/forever start /your/path/to/your/index.js else
>
> @reboot sh /your/path/to/your/startApp.sh
>
> Save & confirm file is saved by check command of #1 again
>
> Note: In my opinion, you should use the full path in crontab file to prevent issues


## Troubleshooting

### Reboot job runs but nothing happens



It seems that if the output is not redirected somewhere then cronjob does not run. However this may have also been fixed by installing [[os.linux.cli.postfix]]




```sh
@reboot /home/pi/repos/presence-detector-cljs-deploy/start.sh 1> /home/pi/repos/presence-detector-cljs-deploy/cron-out 2> /home/pi/repos/presence-detector-cljs-deploy/cron-err
```

#### Redirecting stdout and stderr within cron


- `1>` is stdout
- `2>` is stderr

In the context of `@reboot` within crontab, the first part indicating time intervals can be ignored.

`33 3 * * * /path/to/some_job.sh 1> /dev/null 2> /other/path/to/some_job.err`

[How can I view results of my cron jobs?](https://superuser.com/questions/122246/how-can-i-view-results-of-my-cron-jobs)



#### Installing postfix

`sudo apt-get install postfix`

Notice the comment:

> It is worth pointing out that for use with cron (that is if you don't want to actually send email outwards) during the installation procedure you should answer to configure for local use only. ??? steffen Oct 27 '17 at 10:16

[&quot;(CRON) info (No MTA installed, discarding output)&quot; error in the syslog](https://askubuntu.com/questions/222512/cron-info-no-mta-installed-discarding-output-error-in-the-syslog)
