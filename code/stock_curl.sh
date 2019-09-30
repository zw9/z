!export pick="{unh,amzn,msft,voo,fb,spy,qqq,fxi,vwo,wdc,rht,Gild,aapl,goog,dis}"
!curl -s -L https://www.zacks.com/stock/quote/UNH >../stock-market/UNH_zacks.htm
!curl -s -L https://www.marketwatch.com/investing/stock/unh/{profile,news,charts,financials,historical,analystestimates,options,secfilings,insideractions} > ../stock-market/UNH_marketwatch.htm
!curl -s -L https://finance.yahoo.com/quote/$pick>../stock-market/yahoofinance.htm
!curl -s -L http://thestockmarketwatch.com/stock/?stock={unh,amzn,msft,voo,fb,spy,qqq,fxi,vwo,wdc,rht,Gild,aapl,goog,dis}>../stock-market/thestockmarketwatch.htm
!curl -s -L http://mobile.reuters.com/search/news?blob={unh,amzn,msft,voo,fb,spy,qqq,fxi,vwo,wdc,rht,Gild,aapl,goog,dis} >../stock-market/reuters.htm
!curl -s -L https://www.zacks.com/stock/quote/$pick>../stock-market/zacks.htm
!curl -s -L https://www.marketwatch.com/investing/stock/$pick/{profile,news,charts,financials,historical,analystestimates,options,secfilings,insideractions} > ../stock-market/marketwatch.htm
!curl -s -L https://www.marketwatch.com/investing/stock/$pick>../stock-market/marketwatch_summary.htm
!curl -s -L -o ../stock-market/UNH_marketwatch_summary.htm https://www.marketwatch.com/investing/stock/unh
