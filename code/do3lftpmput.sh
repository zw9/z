#!/bin/bash -xv
# publish to ftp site
## set -x

#echo $uid $pass $site

cd ~/Dropbox/wcode
logfile="output_"$(basename $0|cut -d. -f1)"_"$(uname -n)".txt"
echo $logfile
grep 000webhost ~/Dropbox/z_lock/uidpass.txt>.tmp
 read uid pass site <.tmp
lftp -u $uid,$pass $site << 'EOF' > ~/Dropbox/wlog/$logfile
#rm -rf  /public_html/z/rpt/.git
#rm -rf  /public_html/z/rptvi/.git

cd  /public_html/z/rptvi
#mrm rpt*.txt
cd /public_html/z/rptvi
dir
mirror -R /Volumes/ThuDuc/z/rptvi   /public_html/z/rptvi
dir
du -h /
#help
bye
EOF

cat  ~/Dropbox/wlog/$logfile


# bash  ~/Dropbox/wcode/do3lftpmput.sh &
