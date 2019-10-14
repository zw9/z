
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import re
import io
import os
import time

# In[2]:
rptpath="/Volumes/ThuDuc/z/rptvi/"

def fetch_fnc(url, cl):
    if url[-1]=="/":
        url=url[:-1]
    print(url)
    print(cl)
    print(os.getcwd())
    os.chdir(rptpath)
    pathsvr = re.sub('[^A-Za-z0-9-_]+', '', url.split("/")[2])
    print("pathsvr=" + pathsvr)
    try:
        os.makedirs(rptpath + "/" + pathsvr,exist_ok=True)
    except:
        print("something wrong with: " + pathsvr)
    os.chdir(rptpath + pathsvr)

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

    fn = re.sub('[^A-Za-z0-9-_]+', '', url.split("/")[-1]) + "_" + cl + ".txt"
    encoding = 'utf-8'
    try:
        f = io.open(folderpathnew + "/" + fn, "w", encoding='utf-8')
        f.write(  os.getcwd() + "/")
        f.write(folderpathnew + "/" + fn + "\n")
        #f.write(str(f) )
        f.write(url + "\n")
        #f.write(fn + "\n")
        f.write(cl + "\n")
        encoding = 'utf-8'
        page = requests.get(url)
        page.status_code
        soup = BeautifulSoup(page.content, 'html.parser')
        ctl01_PageHead = soup.title
        print("## " + ctl01_PageHead.get_text() + "\n")
        f.write("## " + ctl01_PageHead.get_text() + "\n")
        finditems = soup.find_all(class_=cl)
        #print(finditems)
        #
        for each in finditems:
            #print(each)
            if each.get_text():
                print( each.get_text()+"\n" +"  ")
                #.lstrip().rstrip().replace('\n', '')
                f.write(each.get_text()+ "\n" + "  ")
            for b in each.find_all('a', href=True):
                #print("url=" + '/'.join(url.split("/")[:-1]))
                #f.write("\n" + '/'.join(url.split("/")[:-1]) + "  " )
                url1=b.get('href')
                if '//' not in url1:
                    url1='/'.join(url.split("/")[:-1])  + ("/" + url1).replace("//","/")

                print( url1+ "\n\n")
                #f.write(  url1 + "  "+ "\n\n")

        print(os.getcwd()  + "/" + fn + "\n")
        f.write( os.getcwd()  + "/" + fn + "\n")
        f.close()
    except:
        #print("something wrong: " + each.get('href'))
        print("something wrong: "  )

# In[3]:


def fetch_option(url):

    print(os.getcwd())
    os.chdir(rptpath)
    pathsvr = re.sub('[^A-Za-z0-9-_]+', '', url.split("/")[2])
    print(pathsvr)
    try:
        os.makedirs(rptpath + "/" + pathsvr,exist_ok=True)
    except:
        print("something wrong with: " + pathn)
    os.chdir(rptpath + pathsvr)

    page = requests.get(url)
    page.status_code
    soup = BeautifulSoup(page.content, 'html.parser')
    ctl01_PageHead = soup.title
    print("## " + ctl01_PageHead.get_text() + "  ")
    optionlist = soup.find(class_='col2Div').find_all('option')
    for each in optionlist:
        if (each.text):
            print("fetch_fnc(\"https://raovat.nguoi-viet.com" + each['value'] + "\")")
            url_c = "https://raovat.nguoi-viet.com" + each['value']
            print("url_c="+url_c)
            fetch_fnc(url_c, 'TBLRoll')
            time.sleep(2) # delays for 1 seconds

def fetch_searchresult(url,cl):
    print(os.getcwd())
    os.chdir(rptpath)
    pathsvr = re.sub('[^A-Za-z0-9-_]+', '', url.split("/")[2])
    print(pathsvr)
    try:
        os.makedirs(rptpath + "/" + pathsvr,exist_ok=True)
    except:
        print("something wrong with: " + pathn)
    os.chdir(rptpath + pathsvr)

    page = requests.get(url)
    page.status_code
    soup = BeautifulSoup(page.content, 'html.parser')
    ctl01_PageHead = soup.title
    print("## " + ctl01_PageHead.get_text() + "  ")
    linklist = soup.find(class_=cl)
    print("linklist=" )
    print(linklist)
    for each in linklist.find_all('a', href=True):
        print(each.get('href'))
        print("url=" + '/'.join(url.split("/")[:-1]))
        #f.write("\n" + '/'.join(url.split("/")[:-1]) + "  " )
        url1=each.get('href')
        if '//' not in url1:
            url1='/'.join(url.split("/")[:-1])  + ("/" + url1).replace("//","/")

        print( url1+ "\n\n")
        fetch_fnc(url1, 'td-post-content')
        time.sleep(2) # delays for 1 seconds


# In[4]:
# %run ~/Dropbox/z/code/nguoivietwebscrape.py
# fetch_fnc("https://raovat.nguoi-viet.com/classified/dam-bop-thu-gian-massage-relax-browse-123.aspx",'TBLRoll')
# fetch_option("https://raovat.nguoi-viet.com/classified/dam-bop-thu-gian-massage-relax-browse-123.aspx")
