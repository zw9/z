
import requests
from bs4 import BeautifulSoup
import re
import io
import os
import time
from urllib3.exceptions import InsecureRequestWarning
# import HTMLSession from requests_html
from requests_html import HTMLSession

# create an HTML Session object


def fetch_p(rptpath,url):
    if url[-1]=="/":
        url=url[:-1]

    # url = "https://www.nguoi-viet.com/sinh-hoat-cong-dong/sinh-hoat-cong-dong/"
    url1=url
    #session = HTMLSession()

    pathsvr = re.sub('[^A-Za-z0-9-_]+', '', url.split("/")[2])
    print("pathsvr=" + pathsvr)
    try:
        os.makedirs(rptpath + "/" + pathsvr,exist_ok=True)
    except:
        print("something wrong with: " + rptpath + "/" + pathsvr)
    os.chdir(rptpath + "/" + pathsvr)

    pathn = re.sub('[^A-Za-z0-9-_]+', '', url.split("/")[-2])
    if pathsvr==pathn:
        folderpathnew=rptpath + "/" + pathsvr
    if pathsvr != pathn:
        folderpathnew=rptpath + "/" + pathsvr+"/" + pathn

    print("folderpathnew=" +folderpathnew)
    try:
        os.makedirs(folderpathnew,exist_ok=True)
    except:
        print( os.getcwd())
        print("something wrong with: " + folderpathnew)

    os.chdir(folderpathnew)

    if url1[-1]=="/":
        url1=url1[:-1]
    try:
        pathn = re.sub('[^A-Za-z0-9-_]+', '', url1.split("/")[-2])
        os.makedirs(folderpathnew, exist_ok=True)
        fn = re.sub('[^A-Za-z0-9-_]+', '', url1.split("/")[-1]) + ".txt"
        encoding = 'utf-8'
        f = io.open(folderpathnew  + "/" + fn, "w", encoding='utf-8')
    except:
        print("something wrong with: " + folderpathnew + "/" + fn)
        fn = pathn + ".txt"
        encoding = 'utf-8'
        f = io.open(rptpath + "/" + pathsvr + "/" + fn, "w", encoding='utf-8')

    f.write(url + "\n")
    f.write(fn + "\n")
    #f.write("<li><a href=" + url + ">" + url + "</a>\n")

    print(url + "\n")
    print(fn)
    requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
    # Use the object above to connect to needed webpage
    #resp = session.get(url)

    # Run JavaScript code on webpage
    #resp.html.render()

    page = requests.get(url, verify=False)
    page.status_code
    soup = BeautifulSoup(page.content, 'html.parser')
    #soup = BeautifulSoup(resp.html.html, "lxml")
    ctl01_PageHead = soup.title
    print("## " + ctl01_PageHead.get_text() + "  ")
    f.write("## " + ctl01_PageHead.get_text() + "\n")
    TBLRoll = soup.find_all(['td_data_time','td-module-meta-info', 'td-post-date', 'entry-date',  'p', 'h3', 'br', 'h1', 'h2', 'h4','h5'])
    AllTags = soup.find_all(True)
    # for e in AllTags:
    # f.write(str(e))

    for each in TBLRoll:
        if each.get_text():
            # print(each.get_text() + "  ")
            #f.write(each.get_text() + "\n\n")
            f.write(each.get_text() + "\n\n")
            #.lstrip().replace('\n', ' ') + "  ")
            #.rstrip()
    f.close()


print("fetch_p(rptpath,)")


def fetch_m(rptpath,url):
    if url[-1]=="/":
        url=url[:-1]

    print("rptpath="+ rptpath)
    print("url="+ url)
    print(os.getcwd())

    fnlog = rptpath + "/fetch_log.md"
    encoding = 'utf-8'
    fflog= io.open(fnlog, "a", encoding='utf-8')
    fflog.write("fetch_m(\"" + rptpath+ "\",\"" + url + "\")\n")
    fflog.close()


    os.chdir(rptpath)

    pathsvr = re.sub('[^A-Za-z0-9-_]+', '', url.split("/")[2])
    print("pathsvr=" + pathsvr)
    try:
        os.makedirs(rptpath + "/" + pathsvr,exist_ok=True)
    except:
        print("something wrong with: " + pathsvr)

    os.chdir(rptpath + "/" + pathsvr)

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
            print("url="+url)
            print("url1="+url1)
            if '//' not in url1:
                url1=url.split("/")[0] + "//" + url.split("/")[2] + ("/" + url1).replace("//","/")
            # print("fetch_p(\"https://raovat.nguoi-viet.com" + each['value'] + "\")")
            # url_c = "https://raovat.nguoi-viet.com" + each['value']
            try:
                ff.write("<li><a href=" + url1 + ">" + url1 + "</a>\n")
                #fetch_p(\'" + url1+ "\')\n")
                fetch_p(rptpath,url1)

            except:
                print("url is bad: " + url1)

            time.sleep(2) # delays for 1 seconds


print("fetch_m()")
def fetch_all():
    fetch_m("/Volumes/ThuDuc/z/rpt","https://nahq.org")
    fetch_m("/Volumes/ThuDuc/z/rpt","https://health.gov")

    fetch_m("/Volumes/ThuDuc/z/rpt","http://www.ncqa.org")
    fetch_m("/Volumes/ThuDuc/z/rpt","http://www.medicare.gov")
    fetch_m("/Volumes/ThuDuc/z/rpt","https://www.webmd.com")
    fetch_m("/Volumes/ThuDuc/z/rpt","https://www.cms.gov/Medicare/Prescription-Drug-Coverage/PrescriptionDrugCovGenIn/index.html")

    #fetch_m("/Volumes/ThuDuc/z/rpt","https://www.linkedin.com/company/ncqa")




    fetch_m("/Volumes/ThuDuc/z/rptvi","http://www.nguoi-viet.com")
    fetch_m("/Volumes/ThuDuc/z/rptvi","http://www.vietfun.com")

    fetch_m("/Volumes/ThuDuc/z/rptvi","https://english.thesaigontimes.vn")
    fetch_m("/Volumes/ThuDuc/z/rptvi","https://vietnamnews.vn")
    fetch_m("/Volumes/ThuDuc/z/rptvi","https://tuoitrenews.vn")
    fetch_m("/Volumes/ThuDuc/z/rptvi","https://www.bbc.com/vietnamese")
    fetch_m("/Volumes/ThuDuc/z/rptvi","https://thanhnien.vn")
    fetch_m("/Volumes/ThuDuc/z/rptvi","https://vietbao.com")
    fetch_m("/Volumes/ThuDuc/z/rptvi","http://www.vietnamdaily.com")
    fetch_m("/Volumes/ThuDuc/z/rptvi","https://vnexpress.net")
    fetch_m("/Volumes/ThuDuc/z/rptvi","https://baomoi.com")
    fetch_m("/Volumes/ThuDuc/z/rptvi","https://baodautu.vn")
    fetch_m("/Volumes/ThuDuc/z/rptvi","http://www.sggp.org.vn")
    fetch_m("/Volumes/ThuDuc/z/rptvi","https://www.nhandan.com.vn")
    fetch_m("/Volumes/ThuDuc/z/rptvi","https://tuoitre.vn")
    fetch_m("/Volumes/ThuDuc/z/rptvi","https://www.tienphong.vn")

print("fetch_all()")

# %run ~/Dropbox/z/code/fetch_prog.py
# fetch_p("/Volumes/ThuDuc/z/rptvi","https://www.nguoi-viet.com/sinh-hoat-cong-dong/sinh-hoat-cong-dong/")

# %run ~/Dropbox/z/code/fetch_prog.py
# fetch_m("/Volumes/ThuDuc/z/rptvi","https://www.nguoi-viet.com/sinh-hoat-cong-dong/sinh-hoat-cong-dong/")
