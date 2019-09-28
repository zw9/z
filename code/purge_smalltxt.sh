# . /Users/atang148/Dropbox/z/purge_smalltxt.sh

find ~/Dropbox/z/ -name "**.txt" -size -2 -delete
find ~/Dropbox/z/ -name "**.txt" -size -2 -delete
find ~/Dropbox/z -empty -type d -delete

cd ~/Dropbox/z/rpt && jupyter nbconvert ~/Dropbox/z/*.ipynb
mv ~/Dropbox/z/*.html ~/Dropbox/z/rpt/
