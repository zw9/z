#cd /run/user/1000/gvfs/ftp:host=192.168.1.1/shares/USB_Storage/Unix

mkdir -p ../html

mkdir -p ../html/dl
cd ../html/dl

curl -s http://localhost  > index_php_`hostname`.htm
curl -s http://localhost/sysinfo.php > sysinfo_`hostname`.htm

curl -s http://192.168.1.{12}  > index_php.htm
svr=("6" ) #"12" "16")

for a in ${svr[@]}
do
curl  -s http://192.168.1.$a/sysinfo.php > sysinfo_$a.htm
done

#curl -L jancox.com > jancox.htm

# curl -u ftpuser:password -O ftp://ftp_pub/public_html/index.html

# curl is a command line tool used to transfer data  to/from a server. The tool supports various protocols such as : DICT, FILE, FTP, FTPS, GOPHER, HTTP,  HTTPS,  IMAP,  IMAPS,  LDAP,  LDAPS,  POP3, POP3S,  RTMP, RTSP, SCP, SFTP, SMB, SMBS, SMTP, SMTPS, TELNET and TFTP.

# curl -o dictionary.txt dict://dict.org/show:db

# curl -o Vietnam.txt dict://dict.org/d:Vietnam:*
# curl -o Saigon.txt dict://dict.org/d:Saigon:*
# curl -o awk.txt dict://dict.org/d:awk:*

#svr=("Nguyen" "Tran" "Huynh" "Tang" "Zhang")
#for a in ${svr[@]}
#do
# curl -o $a.txt dict://dict.org/d:$a:*
#done

# curl -o California.txt dict://dict.org/d:California:*
# curl dict://dict.org/d:[word-to-be-searched]:[dictionary-name]

# curl -L -o UNH_flashratings.htm https://www.flashratings.com/stocks/5823-UNH

# curl -s -L -o UNH_thestreet_summary.htm https://www.thestreet.com/quote/UNH.html

# curl -s -L  https://www.thestreet.com/quote/UNH/details/{profile,news,financials,events,ownership,options}.html > UNH_thestreet.htm

curl -s -L https://www.zacks.com/stock/quote/UNH >UNH_zacks.htm

# curl -L  "http://www.google.com/finance?q=NSE:UNH"

curl  -s -o UNH_googlefinance.htm  -L https://finance.google.com/finance?q=UNH

#curl -o optumsearch.htm -L "https://www.google.com/search?q=optum+reports"

curl -s -L  https://www.marketwatch.com/investing/stock/unh/{profile,news,charts,financials,historical,analystestimates,options,secfilings,insideractions} > UNH_marketwatch.htm

curl -s -L -o UNH_marketwatch_summary.htm https://www.marketwatch.com/investing/stock/unh

curl -s -L -o sinh-hoat-cong-dong.htm https://www.nguoi-viet.com/sinh-hoat-cong-dong/sinh-hoat-cong-dong/

curl -s -L -o dam-bop-thu-gian-massage-relax.htm https://raovat.nguoi-viet.com/classified/dam-bop-thu-gian-massage-relax-browse-123.aspx

curl -s -L -o sang-nhuong-co-so-business-opportunities.htm https://raovat.nguoi-viet.com/classified/sang-nhuong-co-so-business-opportunities-browse-92.aspx

curl -s -L -o viec-van-phong-office-clerical-jobs.htm https://raovat.nguoi-viet.com/classified/viec-van-phong-office-clerical-jobs-browse-97.aspx
cd ../../Unix

 . zrsync.sh
