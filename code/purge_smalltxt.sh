# . /Users/atang148/Dropbox/z/code/purge_smalltxt.sh

python3 /Users/atang148/Dropbox/z/code/nguoiviet-webscrape.py
#mkdir -p ~/Public/z/rpt/ipynb/
jupyter nbconvert ~/Public/z/rpt/notebook/*.ipynb
jupyter nbconvert ~/Public/z/rptvi/notebook/*.ipynb

find ~/Public/z/ -name "**.txt" -size -2 -delete
find ~/Public/z -empty -type d -delete
python3 /Users/atang148/Dropbox/z/code/weblist_inc_mk.py
