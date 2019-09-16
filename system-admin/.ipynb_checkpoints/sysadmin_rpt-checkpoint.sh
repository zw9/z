(
ps -all
top -b -n 1 |grep -v '0.0  0.'
uptime
w
who
ls
printenv
users
crontab -l
service
free
lsof|head -n 10

)>sysadmin_rpt.txt

#gedit ~/Dropbox/txt/sysadmin_rpt.txt &
#gedit ~/Dropbox/bash/sysadmin_rpt.sh &

xed sysadmin_rpt.txt &
xed sysadmin_rpt.sh &
