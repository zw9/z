# bash  ~/Dropbox/z/code/purge_smalltxt.sh

#cd /Volumes/ThuDuc/z && jupyter lab

#jupyter notebook list|grep http|cut -f1 -d" "

# python3 ~/Dropbox/z/code/nguoivietwebscrape.py
#mkdir -p /Volumes/ThuDuc/z/rpt/ipynb/

jupyter nbconvert /Volumes/ThuDuc/z/rpt/notebook/*.ipynb
jupyter nbconvert /Volumes/ThuDuc/z/rptvi/notebook/*.ipynb
mkdir -p /Volumes/ThuDuc/z/rptvi/notebook_html/
mkdir -p /Volumes/ThuDuc/z/rpt/notebook_html/

mv  /Volumes/ThuDuc/z/rptvi/notebook/*.htm* /Volumes/ThuDuc/z/rptvi/notebook_html/
mv  /Volumes/ThuDuc/z/rpt/notebook/*.htm* /Volumes/ThuDuc/z/rpt/notebook_html/

python3 /Users/atang148/Dropbox/z/code/run_weekly.py
python3 /Users/atang148/Dropbox/z/code/run_daily.py

bash ~/Dropbox/z/code/run_hourly.sh

#R -e "rmarkdown::render('/Volumes/ThuDuc/z/rpt/notebook/Genesis-Hospital-Price-List.R',output_file='Genesis-Hospital-Price-List.html')"
#R -e "rmarkdown::render('script.Rmd',output_file='output.html')"

bash  ~/Dropbox/z/code/do1lftpmput.sh &
bash ~/Dropbox/z/code/do2lftpmput.sh &
bash  ~/Dropbox/z/code/do3lftpmput.sh &

#find /Volumes/ThuDuc/z/rpt  -name "**.txt" -mtime +3  -delete

#awk -F "//" '{print 2}' /Volumes/ThuDuc/z/*log.html
