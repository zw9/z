#!/bin/bash
PS1="\t $ "

while IFS= read -r file;
do
fn=$(basename -z "$file").R;echo $fn
[ -f "$file" ] && (echo "# Rscript ${src}R/$fn;
fn <- \"$fn\";
fin <- \"$file\";
# $0 $1
source(\"~/Dropbox/z/code/one.R\")
" )>"${src}R/$fn"
cat "${src}R/$fn" ;
 Rscript "${src}R/$fn" ;
 sleep 5s;
done <${rpt}ext/csv_make_ext.txt
