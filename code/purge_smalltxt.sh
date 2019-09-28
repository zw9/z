# . /Users/atang148/Dropbox/z/code/purge_smalltxt.sh

python3 /Users/atang148/Dropbox/z/code/nguoiviet-webscrape.py
mkdir -p ~/Dropbox/z/rpt/ipynb/
cd ~/Dropbox/z/rpt && jupyter nbconvert ~/Dropbox/z/code/*.ipynb
mv ~/Dropbox/z/code/*.html ~/Dropbox/z/rpt/ipynb/
find ~/Dropbox/z/ -name "**.txt" -size -2 -delete
find ~/Dropbox/z -empty -type d -delete
python3 /Users/atang148/Dropbox/z/code/weblist_inc_mk.py
