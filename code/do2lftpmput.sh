#!/bin/bash -xv
# publish to ftp site
#set -x

# bash ~/Dropbox/z/code/do2lftpmput.sh &

#!/bin/bash
logfile="output_"$(basename $0|cut -d. -f1)"_"$(uname -n)".txt"
echo $logfile
(

grep somee ~/Dropbox/z_lock/uidpass.txt>.tmp
 read uid pass site <.tmp
#echo $uid $pass $site
lftp -u $uid,$pass $site << EOF2

set net:timeout 5;
set net:max-retries 3;
set net:reconnect-interval-multiplier 1;
set net:reconnect-interval-base 5;
#rm -rf  /public_html/z/rpt/.git
#rm -rf  /public_html/z/rptvi/.git

rm -rf  /public_html/z/rptvi

cd /www.healthit.somee.com/z/rpt
dir

mirror -R /Volumes/ThuDuc/z/rpt/notebook  /www.healthit.somee.com/z/rpt/notebook
mirror -R /Volumes/ThuDuc/z/rpt  /www.healthit.somee.com/z/rpt


du -h
#help
bye
EOF2
) &> ~/Dropbox/wlog/$logfile
cat ~/Dropbox/wlog/$logfile
cd ~/Dropbox/z/code
