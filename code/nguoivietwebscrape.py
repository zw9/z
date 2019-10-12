
# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup
import re
import io
import os
import time

# In[2]:


def fetch_fnc(url, cl):

    pathn = re.sub('[^A-Za-z0-9-_]+', '', url.split("/")[-2])
    print(pathn)
    try:
        os.makedirs(pathn,exist_ok=True)
    except:
        print("pwd=: " + pwd)
        print("something wrong with: " + pathn)

    fn = re.sub('[^A-Za-z0-9-_]+', '', url.split("/")[-1]) + "_" + cl + ".txt"
    encoding = 'utf-8'
    try:
        f = io.open(pathn + "/" + fn, "w", encoding='utf-8')
        print(f)
        f.write(url + "\n")
        f.write(fn + "\n")
        f.write(cl + "\n")
        encoding = 'utf-8'
        page = requests.get(url)
        page.status_code
        soup = BeautifulSoup(page.content, 'html.parser')
        ctl01_PageHead = soup.title
        print("## " + ctl01_PageHead.get_text() + "  ")
        f.write("## " + ctl01_PageHead.get_text() + "  ")
        finditems = soup.find_all(class_=cl)
        print(finditems)
        #
        for each in finditems:
            print(each)
            for a in each.find_all('a', href=True):
                print(a.get('href'))
                url1=a.get('href')
                print("url1="+url1)
                f.write("\n\n" + url1 + "  ")
            if each.get_text():
                print("\n\n" + each.get_text().lstrip().rstrip().replace('\n', ' ') +"  ")
                f.write("\n\n" + each.get_text().lstrip().rstrip().replace('\n', ' ') + "  ")
        f.close()
    except:
        #print("something wrong: " + each.get('href'))
        print("something wrong: " + str(each.get_text()) )

# In[3]:


def fetch_option(url):

    print(os.getcwd())
    os.chdir("/Volumes/ThuDuc/z/rptvi")
    pathsvr = re.sub('[^A-Za-z0-9-_]+', '', url.split("/")[2])
    print(pathsvr)
    try:
        os.makedirs(pathsvr,exist_ok=True)
    except:
        print("something wrong with: " + pathn)
    os.chdir("/Volumes/ThuDuc/z/rptvi/" + pathsvr)

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
            fetch_fnc(url_c, 'TBLRoll')
            time.sleep(2) # delays for 1 seconds


# In[4]:
# %run ~/Dropbox/z/code/nguoivietwebscrape.py
# fetch_fnc("https://raovat.nguoi-viet.com/classified/dam-bop-thu-gian-massage-relax-browse-123.aspx",'TBLRoll')
# fetch_option("https://raovat.nguoi-viet.com/classified/dam-bop-thu-gian-massage-relax-browse-123.aspx")
