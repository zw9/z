#!/bin/bash

# populate admin report
set -x

#!/bin/bash -v 

logfile=$(basename $0|cut -d. -f1)"_output_"$(uname -n)".txt"
echo $logfile 

# export PS1='\u@\h:\w \d \@\$'
( 
    date 
/sbin/ifconfig |grep 'inet'|awk '{gsub("addr:","",$0);print "lynx " $2}'

#lsof |egrep 'home'|awk '{print $1,$7,$9}'|sort -u

#lsof -i
w
df -h
last|head
ps auxc|egrep -v ' 0.0 '
du -d 1 ../ 
) &>  $logfile

#if [ -f   ~/wlog/$logfile ] ; then head -n 500  ~/wlog/$logfile >> ~/wlog/$logfile.tmp ; fi && mv  ~/wlog/$logfile.tmp  ~/wlog/$logfile

#head ~/wlog/$logfile