#run_daily.py
# %run ~/Dropbox/z/code/run_daily.py
# %run ~/Dropbox/z/code/run_weekly.py

import os
os.chdir(os.environ['HOME'] + "/Dropbox/z/code")

import nguoivietwebscrape as nv

os.chdir("/Volumes/ThuDuc/z/rptvi")

nv.fetch_fnc("https://raovat.nguoi-viet.com/classified/dam-bop-thu-gian-massage-relax-browse-123.aspx",'TBLRoll')

nv.fetch_fnc("https://www.nguoi-viet.com/?s=Cuối+tuần+xem+gì",'item-details')

nv.fetch_option("https://raovat.nguoi-viet.com/classified/dam-bop-thu-gian-massage-relax-browse-123.aspx")


%run ~/Dropbox/z/code/nguoivietwebscrape.py
fetch_fnc("https://www.nguoi-viet.com/?s=Cuối+tuần+xem+gì","entry-title td-module-title")

%run ~/Dropbox/z/code/nguoivietwebscrape.py
fetch_fnc("https://www.nguoi-viet.com/?s=Cuối+tuần+xem+gì",'item-details')

# fetch_fnc("https://raovat.nguoi-viet.com/classified/dam-bop-thu-gian-massage-relax-browse-123.aspx",'TBLRoll')
# fetch_option("https://raovat.nguoi-viet.com/classified/dam-bop-thu-gian-massage-relax-browse-123.aspx")

#
