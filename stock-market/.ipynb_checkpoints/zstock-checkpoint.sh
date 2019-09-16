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
mkdir -p $html
mkdir -p $html/dl
cd $html/dl

export pick="{unh,amzn,msft,voo,fb,spy,qqq,fxi,vwo,wdc,rht,Gild,aapl,goog,dis}"

curl  -s -L https://finance.yahoo.com/quote/$pick>yahoofinance.htm

curl  -s -L http://thestockmarketwatch.com/stock/?stock={unh,amzn,msft,voo,fb,spy,qqq,fxi,vwo,wdc,rht,Gild,aapl,goog,dis}>thestockmarketwatch.htm

curl  -s -L http://mobile.reuters.com/search/news?blob={unh,amzn,msft,voo,fb,spy,qqq,fxi,vwo,wdc,rht,Gild,aapl,goog,dis} >reuters.htm

curl -s -L  https://www.zacks.com/stock/quote/$pick>zacks.htm

curl  -s -L https://finance.google.com/finance?q={unh,amzn,msft,voo,fb,spy,qqq,fxi,vwo,wdc,rht,Gild,aapl,goog,dis}>googlefinance.htm

curl -s -L  https://www.marketwatch.com/investing/stock/$pick/{profile,news,charts,financials,historical,analystestimates,options,secfilings,insideractions} > marketwatch.htm

curl -s -L  https://www.marketwatch.com/investing/stock/$pick>marketwatch_summary.htm
 )>$fn.txt

#cd ../../Unix

 #. zrsync.sh
