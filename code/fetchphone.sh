# bash ~/Dropbox/z/code/fetchphone.sh

fn="/Users/atang148/Dropbox/zz/classified.vcf"
#fn="/Users/atang148/Dropbox/zz/work-sinh-hoat-cong-dong.vcf"

echo "BEGIN:VCARD
VERSION:3.0
PRODID:-//Apple Inc.//Mac OS X 10.15//EN
N:classified;random;;;
FN:test nv
ORG:zz;
" >"$fn"

cd /Volumes/ThuDuc/z/rptvi/raovatnguoi-vietcom/classified/
#cd /Volumes/ThuDuc/z/rptvi/wwwnguoi-vietcom/sinh-hoat-cong-dong
(
grep -Eo '[-()0-9]+' *.txt

) |grep '-' |sort -u |awk '{print "TEL;type=IPHONE;type=CELL;type=VOICE:"$0}'>>"$fn"
echo "END:VCARD">>"$fn"

atom  "$fn"

# tr -dc '0-9' < /Volumes/ThuDuc/z/rptvi/raovatnguoi-vietcom/classified/dam-bop-thu-gian-massage-relax-browse-123aspx.txt
