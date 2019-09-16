#
fn=$(basename $1|cut -d_ -f1)_
fn=$(basename $0|cut -d. -f1)_$(uname -n)
fn=${fn//[^a-z A-Z 0-9]/_}
fn=${fn//\:/}
fn=${fn//\ /_}
echo $fn
# )>$rpt/$fn.txt

(
# cd /run/user/1000/gvfs/ftp:host=192.168.1.1/shares/USB_Storage/Unix
mkdir -p ../html
mkdir -p ../html/dl
cd ../html/dl



#curl  -s -L https://finance.google.com/finance?q={unh,amzn,msft,voo,fb,spy,qqq,fxi,vwo,wdc,rht,Gild,aapl,goog,dis}>googlefinance.htm

 )>$fn.txt

#cd ../../Unix

 #. zrsync.sh
