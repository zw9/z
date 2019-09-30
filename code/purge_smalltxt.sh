# . /Users/atang148/Dropbox/z/code/purge_smalltxt.sh

cd ~/Public/z && jupyter lab

jupyter notebook list|grep http|cut -f1

python3 /Users/atang148/Dropbox/z/code/nguoiviet-webscrape.py
#mkdir -p ~/Public/z/rpt/ipynb/
jupyter nbconvert ~/Public/z/rpt/notebook/*.ipynb
jupyter nbconvert ~/Public/z/rptvi/notebook/*.ipynb
mkdir -p ~/Public/z/rptvi/notebook_html/
mkdir -p ~/Public/z/rpt/notebook_html/

mv  ~/Public/z/rptvi/notebook/*.html ~/Public/z/rptvi/notebook_html/
mv  ~/Public/z/rpt/notebook/*.html ~/Public/z/rpt/notebook_html/

find ~/Public/z/ -name "**.txt" -size -2 -delete
find ~/Public/z -empty -type d -delete
python3 /Users/atang148/Dropbox/z/code/weblist_inc_mk.py
