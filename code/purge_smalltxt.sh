# . /Users/atang148/Dropbox/z/code/purge_smalltxt.sh

find ~/Dropbox/z/ -name "**.txt" -size -2 -delete
find ~/Dropbox/z/ -name "**.txt" -size -2 -delete
find ~/Dropbox/z -empty -type d -delete
mkdir -p ~/Dropbox/z/rpt/ipynb/
cd ~/Dropbox/z/rpt && jupyter nbconvert ~/Dropbox/z/code/*.ipynb
mv ~/Dropbox/z/code/*.html ~/Dropbox/z/rpt/ipynb/
