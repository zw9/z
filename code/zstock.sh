#
cd ~/Public/z/rpt/
mkdir -p stock
cd stock


# cd /run/user/1000/gvfs/ftp:host=192.168.1.1/shares/USB_Storage/Unix
# https://finance.yahoo.com/quote/UNH?p=UNH&.tsrc=fin-srch
#curl  -s -L https://finance.google.com/finance?q={unh,amzn,msft,voo,fb,spy,qqq,fxi,vwo,wdc,rht,Gild,aapl,goog,dis}>googlefinance.htm
curl  -s -L https://finance.yahoo.com/quote/{$1}>"$1 yahoo.htm"

# )>$fn.txt

#cd ../../Unix

 #. zrsync.sh
# . /Users/atang148/Dropbox/z/code/zstock.sh unh
