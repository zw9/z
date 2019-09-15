#!/bin/bash
(grep -i -h "[.]$1$" -v "zlock" $rptfn/*fn.txt)>$rptext/$1_$(basename $0|cut -d. -f1).txt
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