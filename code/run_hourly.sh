# . ~/Dropbox/z/code/run_hourly.sh

find /Volumes/ThuDuc/z -name "**.txt" -size -2 -delete
find /Volumes/ThuDuc/z -empty -type d -delete
python3 ~/Dropbox/z/code/filelist_mk.py
python3 ~/Dropbox/z/code/filelistbyext.py
