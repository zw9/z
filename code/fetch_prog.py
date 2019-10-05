
import requests
from bs4 import BeautifulSoup
import re
import io
import os
import time
from urllib3.exceptions import InsecureRequestWarning


def fetch_p(url):
    # url = "https://www.nguoi-viet.com/sinh-hoat-cong-dong/sinh-hoat-cong-dong/"
    url1=url
    if url1[-1]=="/":
        url1=url1[:-1]
    try:
        pathn = re.sub('[^A-Za-z0-9-_]+', '', url1.split("/")[-2])
        os.makedirs(pathn, exist_ok=True)
        fn = re.sub('[^A-Za-z0-9-_]+', '', url1.split("/")[-1]) + ".txt"
        encoding = 'utf-8'
        f = io.open(pathn + "/" + fn, "w", encoding='utf-8')
    except:
        print("something wrong with: " + pathn + "/" + fn)
        fn = pathn + ".txt"
        encoding = 'utf-8'
        f = io.open(pathn + "/" + fn, "w", encoding='utf-8')

    f.write(url + "\n")
    f.write(fn + "\n")

    print(url + "\n")
    print(fn)
    requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)

    page = requests.get(url, verify=False)
    page.status_code
    soup = BeautifulSoup(page.content, 'html.parser')
    ctl01_PageHead = soup.title
    print("## " + ctl01_PageHead.get_text() + "  ")
    f.write("## " + ctl01_PageHead.get_text() + "\n")
    TBLRoll = soup.find_all(['p', 'h3', 'br', 'h1', 'h2', 'h4','h5'])
    AllTags = soup.find_all(True)
    # for e in AllTags:
    # f.write(str(e))

    for each in TBLRoll:
        if each.get_text():
            # print(each.get_text() + "  ")
            #f.write(each.get_text() + "\n\n")
            f.write("\n" + each.get_text().lstrip().rstrip().replace('\n', ' ') + "  ")

    f.close()


print("fetch_p()")


def fetch_m(rptpath,url):
    print("rptpath="+ rptpath)
    print("url="+ url)
    print(os.getcwd())

    fnlog = os.environ['HOME'] + rptpath + "/fetch_log.md"
    encoding = 'utf-8'
    fflog= io.open(fnlog, "a", encoding='utf-8')
    fflog.write("fetch_m(\"" + rptpath+ "\",\"" + url + "\")\n")
    fflog.close()


    os.chdir(os.environ['HOME'] + rptpath)

    pathsvr = re.sub('[^A-Za-z0-9-_]+', '', url.split("/")[2])
    print("pathsvr=" + pathsvr)
    try:
        os.makedirs(pathsvr,exist_ok=True)
    except:
        print("something wrong with: " + pathsvr)

    os.chdir(os.environ['HOME'] + rptpath + "/" + pathsvr)

    page = requests.get(url, verify=False)
    page.status_code
    soup = BeautifulSoup(page.content, 'html.parser')

    try:
        ctl01_PageHead = soup.title
        print("## " + ctl01_PageHead.get_text() + "  ")
    except:
        print("something wrong with: " )
    TBLRoll = soup.findAll('a')
    cl = 'TBLRoll'
    fnlog = re.sub('[^A-Za-z0-9-_]+', '', url.split("/")[2]) + "_log.html"
    encoding = 'utf-8'
    ff = io.open(fnlog, "w", encoding='utf-8')
    for each in TBLRoll[:100]:
        if (each.get('href')):
            url1=each.get('href')
            print("url1="+url1)
            if '//' not in url1:
                url1=url.split("/")[0] + "//" + url.split("/")[2] + url1
            # print("fetch_p(\"https://raovat.nguoi-viet.com" + each['value'] + "\")")
            # url_c = "https://raovat.nguoi-viet.com" + each['value']
            try:
                ff.write("<li><a href=" + url1 + ">" + url1 + "</a>\n")
                #fetch_p(\'" + url1+ "\')\n")
                fetch_p(url1)

            except:
                print("url is bad: " + url1)

            time.sleep(2) # delays for 1 seconds


print("fetch_m()")
def fetch_all():
    fetch_m("/Public/z/rpt","https://nahq.org")
    fetch_m("/Public/z/rpt","https://health.gov")

    fetch_m("/Public/z/rpt","http://www.ncqa.org")
    fetch_m("/Public/z/rpt","http://www.medicare.gov")
    fetch_m("/Public/z/rpt","https://www.webmd.com")
    #fetch_m("/Public/z/rpt","https://www.linkedin.com/company/ncqa")




    fetch_m("/Public/z/rptvi","http://www.nguoi-viet.com")
    fetch_m("/Public/z/rptvi","http://www.vietfun.com")

    fetch_m("/Public/z/rptvi","https://english.thesaigontimes.vn")
    fetch_m("/Public/z/rptvi","https://vietnamnews.vn")
    fetch_m("/Public/z/rptvi","https://tuoitrenews.vn")
    fetch_m("/Public/z/rptvi","https://www.bbc.com/vietnamese")
    fetch_m("/Public/z/rptvi","https://thanhnien.vn")
    fetch_m("/Public/z/rptvi","https://vietbao.com")
    fetch_m("/Public/z/rptvi","http://www.vietnamdaily.com")
    fetch_m("/Public/z/rptvi","https://vnexpress.net")
    fetch_m("/Public/z/rptvi","https://baomoi.com")
    fetch_m("/Public/z/rptvi","https://baodautu.vn")
    fetch_m("/Public/z/rptvi","http://www.sggp.org.vn")
    fetch_m("/Public/z/rptvi","https://www.nhandan.com.vn")
    fetch_m("/Public/z/rptvi","https://tuoitre.vn")
    fetch_m("/Public/z/rptvi","https://www.tienphong.vn")

print("fetch_all()")

# %run ~/Dropbox/z/code/fetch_prog.py
# %run ~/Dropbox/z/code/fetch_prog.py
