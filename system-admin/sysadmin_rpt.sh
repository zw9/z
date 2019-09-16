
logfile=$(basename $0|cut -d. -f1)"_output_"$(uname -n)".txt"
echo $logfile 

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

) &>  $logfile

xed $logfile  &
xed sysadmin_rpt.sh &
