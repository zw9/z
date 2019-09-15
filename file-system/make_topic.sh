#!/bin/bash
(echo \# $0 $1 $2
grep -i -h "$1" $rptfn/*fn.txt)>$rpt/$1_topic.txt
tail $rpt/$1_topic.txt

#find /data /home /media /var /etc -name "*.$1"|awk '{print "\"" $0 "\"" }'


: '
for ext in python vba sql sas verscend coviti 
#cms ncqa omw bcs mrp cdc 
#hedis medicare 
do 
bash topic_make.sh $ext
done

'