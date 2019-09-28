
import requests
from bs4 import BeautifulSoup
import re
import io
import os
import time


def fetch_p(url):
    # url = "https://www.nguoi-viet.com/sinh-hoat-cong-dong/sinh-hoat-cong-dong/"

    try:
        pathn = re.sub('[^A-Za-z0-9-_]+', '', url.split("/")[-3])
        os.makedirs(pathn, exist_ok=True)
        fn = re.sub('[^A-Za-z0-9-_]+', '', url.split("/")[-2]) + ".txt"
        encoding = 'utf-8'
        f = io.open(pathn + "/" + fn, "w", encoding='utf-8')
    except:
        print("something wrong with: " + pathn)
        pathn = re.sub('[^A-Za-z0-9-_]+', '', url.split("/")[-2])
        os.makedirs(pathn, exist_ok=True)
        fn = re.sub('[^A-Za-z0-9-_]+', '', url.split("/")[-1]) + ".txt"
        encoding = 'utf-8'
        f = io.open(pathn + "/" + fn, "w", encoding='utf-8')

    f.write(url + "\n")
    f.write(fn + "\n")

    print(fn)
    page = requests.get(url, verify=False)
    page.status_code
    soup = BeautifulSoup(page.content, 'html.parser')
    ctl01_PageHead = soup.title
    print("## " + ctl01_PageHead.get_text() + "  ")
    f.write("## " + ctl01_PageHead.get_text() + "\n")
    TBLRoll = soup.find_all(['p', 'h3', 'li', 'br', 'h1', 'h2', 'h'])
    AllTags = soup.find_all(True)
    # for e in AllTags:
    # f.write(str(e))

    for each in TBLRoll:
        if each.get_text():
            # print(each.get_text() + "  ")
            f.write(each.get_text() + "\n\n")
    f.close()


print("fetch_p()")


def fetch_m(url):
    print(os.getcwd())
    os.chdir("/Users/atang148/Dropbox/z/rpt")
    pathsvr = re.sub('[^A-Za-z0-9-_]+', '', url.split("/")[2])
    print(pathsvr)
    try:
        os.makedirs(pathsvr,exist_ok=True)
    except:
        print("something wrong with: " + pathn)
    os.chdir("/Users/atang148/Dropbox/z/rpt/" + pathsvr)

    page = requests.get(url, verify=False)
    page.status_code
    soup = BeautifulSoup(page.content, 'html.parser')
    ctl01_PageHead = soup.title
    print("## " + ctl01_PageHead.get_text() + "  ")
    TBLRoll = soup.findAll('a')
    cl = 'TBLRoll'
    fnlog = re.sub('[^A-Za-z0-9-_]+', '', url.split("/")[-2]) + "_log.txt"
    encoding = 'utf-8'
    ff = io.open(fnlog, "w", encoding='utf-8')
    for each in TBLRoll:
        if (each.get('href')):
            print(each.get('href'))
            # print("fetch_p(\"https://raovat.nguoi-viet.com" + each['value'] + "\")")
            # url_c = "https://raovat.nguoi-viet.com" + each['value']
            try:
                ff.write("fetch_p(\'" + each.get('href') + "\')\n")
                fetch_p(each.get('href'))

            except:
                print("url is bad: " + each.get('href'))

            time.sleep(2) # delays for 1 seconds


print("fetch_m()")
def fetch_all():
    fetch_m("http://www.vietfun.com")
    fetch_m("http://www.ncqa.org")
    fetch_m("http://www.medicare.gov")
    fetch_m("http://www.nguoi-viet.com")
    fetch_m("https://www.webmd.com/health-insurance/terms/ncqa")
    fetch_m("https://www.linkedin.com/company/ncqa")

# %run /Users/atang148/Dropbox/z/daily/fetch_prog.py
