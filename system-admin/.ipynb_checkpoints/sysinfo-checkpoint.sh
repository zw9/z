#fn=$(basename $1|cut -d. -f1)_
fn=$(uname -a)_$(basename $0|cut -d. -f1)
fn=${fn//[^a-z A-Z 0-9]/_}
fn=${fn//\:/}
fn=${fn//\ /_}
echo $fn

(uname -a;
pwd;
ls -al;
netstat -r;
route -n;
ip route list;
fc -l 5;
groups;id;seq -s, 1 7 100;finger;hostname -I;tree /var/www/html;iwconfig;env;set;compgen -c -S d|sort |tail;lastlog|grep -v Never;netstat -ntpl;chkconfig –list;nmap -sP 192.168.1.0/24;w;who;alias;export;mount;df -h;cal;ifconfig;history|tail;uptime;users;whoami;crontab -l;free -h;lsof|grep -v denied|tail;last|tail;ps -f;grep -i error /var/log/messages|tail;grep -i error /var/log/*|grep -v denied|tail;dmesg|tail)> $rpt/$fn.txt

echo   "$0<pre>" > $rpt/html_header.txt

echo "</pre>" > $rpt/html_tail.txt

cat $rpt/html_header.txt $rpt/$fn.txt $rpt/html_tail.txt  > $rpt/$fn.htm

tail $rpt/$fn.txt

#. zrsync.sh
