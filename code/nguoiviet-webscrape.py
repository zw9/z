# %run ~/Dropbox/z/code/nguoiviet-webscrape.py

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
        print("something wrong with: " + pathn)

    fn = re.sub('[^A-Za-z0-9-_]+', '', url.split("/")[-1]) + ".txt"
    encoding = 'utf-8'
    try:
        f = io.open(pathn + "/" + fn, "w", encoding='utf-8')
        f.write(url + "\n")
        f.write(fn + "\n")
        encoding = 'utf-8'
        page = requests.get(url)
        page.status_code
        soup = BeautifulSoup(page.content, 'html.parser')
        ctl01_PageHead = soup.title
        print("## " + ctl01_PageHead.get_text() + "  ")
        f.write("## " + ctl01_PageHead.get_text() + "  ")
        TBLRoll = soup.find_all(class_=cl)
        for each in TBLRoll:
            if each.get_text():
                # print("\n\n" + each.get_text().lstrip().rstrip().replace('\n', ' ') +"  ")
                f.write("\n\n" + each.get_text().lstrip().rstrip().replace('\n', ' ') + "  ")
        f.close()
    except:
        print("something wrong: " + pathn)

# In[3]:


def fetch_option(url):

    print(os.getcwd())
    os.chdir(os.environ['HOME'] + "/Public/z/rptvi")
    pathsvr = re.sub('[^A-Za-z0-9-_]+', '', url.split("/")[2])
    print(pathsvr)
    try:
        os.makedirs(pathsvr,exist_ok=True)
    except:
        print("something wrong with: " + pathn)
    os.chdir(os.environ['HOME'] + "/Public/z/rptvi/" + pathsvr)

    page = requests.get(url)
    page.status_code
    soup = BeautifulSoup(page.content, 'html.parser')
    ctl01_PageHead = soup.title
    print("## " + ctl01_PageHead.get_text() + "  ")
    TBLRoll = soup.find(class_='col2Div').find_all('option')
    cl = 'TBLRoll'
    for each in TBLRoll:
        if (each.text):
            print("fetch_fnc(\"https://raovat.nguoi-viet.com" + each['value'] + "\")")
            url_c = "https://raovat.nguoi-viet.com" + each['value']
            fetch_fnc(url_c, cl)
            time.sleep(2) # delays for 1 seconds


# In[4]:

fetch_option("https://raovat.nguoi-viet.com/classified/dam-bop-thu-gian-massage-relax-browse-123.aspx")
