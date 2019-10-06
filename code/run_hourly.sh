# . ~/Dropbox/z/code/run_hourly.sh

find ~/Public/z/ -name "**.txt" -size -2 -delete
find ~/Public/z -empty -type d -delete
python3 ~/Dropbox/z/code/filelist_mk.py
python3 ~/Dropbox/z/code/filelistbyext.py
