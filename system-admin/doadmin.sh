#!/bin/bash -xv 
# populate admin report
set -x

#!/bin/bash -v 

logfile="output_"$(basename $0|cut -d. -f1)"_"$(uname -n)".txt"
echo $logfile 

# export PS1='\u@\h:\w \d \@\$'
(date 
/sbin/ifconfig |grep 'inet'|awk '{gsub("addr:","",$0);print "lynx " $2}'

lsof |egrep 'home'|awk '{print $1,$7,$9}'|sort -u

lsof -i
w
df -h
du ~/doneurl -d 1 |sort -n
du ~ -d 1 -h |sort -n

last|head

ps auxc|egrep -v ' 0.0 '|grep admin
) &>  ~/wlog/$logfile.tmp
if [ -f   ~/wlog/$logfile ] ; then head -n 500  ~/wlog/$logfile >> ~/wlog/$logfile.tmp ; fi && mv  ~/wlog/$logfile.tmp  ~/wlog/$logfile

head ~/wlog/$logfile