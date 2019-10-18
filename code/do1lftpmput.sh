#!/bin/bash -xv
# publish to ftp site
#set -x

# bash  ~/Dropbox/z/code/do1lftpmput.sh &

# test;

#!/bin/bash
cd ~/Dropbox/wlog

logfile="output_"$(basename $0|cut -d. -f1)"_"$(uname -n)".txt"
echo $logfile

grep x10 ~/Dropbox/z_lock/uidpass.txt>.tmp
 read uid pass site <.tmp
#echo $uid $pass $site
lftp -u $uid,$pass $site << EOF1  &> ~/Dropbox/wlog/$logfile

set net:timeout 5;
set net:max-retries 3;
set net:reconnect-interval-multiplier 1;
set net:reconnect-interval-base 5;
# mkdir  /public_html/z/rpt
cd /public_html/z/rpt
#rm -rf  /public_html/z/rpt/.git
#rm -rf  /public_html/z/rptvi/.git
rm -rf  /public_html/z/rptvi

dir
#mirror -nrR /Volumes/ThuDuc/z/rptvi  /public_html/z/rptvi
mirror -R /Volumes/ThuDuc/z/rpt/notebook  /public_html/z/rpt/notebook
mirror -R /Volumes/ThuDuc/z/rpt  /public_html/z/rpt
du -h
#help
bye

EOF1

cat ~/Dropbox/wlog/$logfile

#$(cat ~/z/code/listurl_$(uname -n).txt|awk '{print "mirror -nrR ~/doneurl  /public_html/txt -i " $1}')

#mrm  /public_html/txt/*grepext*
