#

find /Volumes/ThuDuc/z/ -name "**.txt" -size -2 -delete
find /Volumes/ThuDuc/z -empty  -delete
find /Volumes/ThuDuc/z -empty -type d -delete
rm /Volumes/ThuDuc/z/rpt/*.html
rm /Volumes/ThuDuc/z/rptvi/*.html
python3 ~/Dropbox/z/code/filelist_mk.py
python3 ~/Dropbox/z/code/filelistbyext.py
