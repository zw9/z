# . ~/Dropbox/z/code/purge_smalltxt.sh

cd /Volumes/ThuDuc/z && jupyter lab

jupyter notebook list|grep http|cut -f1 -d" "

# python3 ~/Dropbox/z/code/nguoivietwebscrape.py
#mkdir -p /Volumes/ThuDuc/z/rpt/ipynb/
jupyter nbconvert /Volumes/ThuDuc/z/rpt/notebook/*.ipynb
jupyter nbconvert /Volumes/ThuDuc/z/rptvi/notebook/*.ipynb
mkdir -p /Volumes/ThuDuc/z/rptvi/notebook_html/
mkdir -p /Volumes/ThuDuc/z/rpt/notebook_html/

mv  /Volumes/ThuDuc/z/rptvi/notebook/*.html /Volumes/ThuDuc/z/rptvi/notebook_html/
mv  /Volumes/ThuDuc/z/rpt/notebook/*.html /Volumes/ThuDuc/z/rpt/notebook_html/

find /Volumes/ThuDuc/z/ -name "**.txt" -size -2 -delete
find /Volumes/ThuDuc/z -empty -type d -delete
python3 ~/Dropbox/z/code/filelist_mk.py
python3 ~/Dropbox/z/code/filelistbyext.py

#find /Volumes/ThuDuc/z/rpt  -name "**.txt" -mtime +3  -delete

awk -F "//" '{print 2}' /Volumes/ThuDuc/z/*log.html
