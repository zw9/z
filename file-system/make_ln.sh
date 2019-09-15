#!/bin/bash
set -xv

cd ~
for fn in $(ls /data );
do
ln -s "/data/$fn" "$fn"
done
exit

: '

'
rm $rptext/*.txt
(
set +e
awk -F "." '!/\/\./ && !/zlock/ && /\./ && !/\.[0-9]/ {fnnew= $(NF);gsub("/","", fnnew); print "echo \"" $0 "\" >> \"$rptext/"fnnew"_make_ext.txt\""}' $rptfn/*fn.txt 
awk -F "/" '!/\./ {fnnew= $(NF);gsub("/","", fnnew);print "echo \"" $0 "\" >> \"$rptext/" fnnew "_make_ext.txt\""}' $rptfn/*fn.txt )>doit.sh
cat doit.sh
bash doit.sh

for fnn in $(find $rptext -name "*ext.txt" -type f -size -2k); 
do 
cat "$fnn"  >> $rptext/misc_misc.txt
rm $fnn
done

exit
bash $fn/make_ext_awk.sh

(grep -i -h "[.]$1$" $rptfn/*fn.txt)>$rptext/$1_$(basename $0|cut -d. -f1).txt
#tail $r/$1_ext.txt
tail $rptext/$1_$(basename $0|cut -d. -f1).txt

#find /data /home /media /var /etc -name "*.$1"|awk '{print "\"" $0 "\"" }'



: '
echo \# $0 $1 $2
rm $rptext/*
for ext in $(echo log xml Readme pxi pxd rst txt INSTALLER METADATA RECORD WHEEL ps1 js pl rb c cpp cs csv pdf doc json sas sql py R zip ppt xls xlsx xlsm dat mov jpg jpeg png bas bat exe msi bash mp3 mpg mpeg gif conf c cs h js json R py csv txt ini pdf mp3 jpg png mov sql sas awk sed xls xlsx doc docx psv cmd sh jpeg pl rb bas vbs mp4 |tr " " "\n"|sort -u);
do 
bash $task/fn/make_ext.sh $ext
done

find $rptext -name "*.txt" -size -1k -delete


for ext in $(echo xml txt mdb accdb tar h tar z ps1 js pl rb c cpp cs csv pdf doc json sas sql py R zip ppt xls xlsx xlsm dat mov jpg jpeg png bas bat exe msi bash mp3 mpg mpeg gif conf c cs h js json R py csv txt ini pdf mp3 jpg png mov sql sas awk sed xls xlsx doc docx psv cmd sh jpeg pl rb bas vbs mp4 |tr " " "\n"|sort -u);
do 
bash $task/fn/make_ext.sh $ext
done

'