# coding: utf-8

# In[1]:


import requests
from bs4 import BeautifulSoup


# In[2]:


def fetch_fnc(url, cl):
    import re
    import io
    fn = re.sub('[^A-Za-z0-9-_]+', '', url.split("/")[-1]) + ".txt"
    fn
    encoding = 'utf-8'
    f = io.open(fn, "w", encoding='utf-8')
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


# In[3]:


def fetch_option(url):
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


# In[4]:

fetch_option("https://raovat.nguoi-viet.com/classified/dam-bop-thu-gian-massage-relax-browse-123.aspx")
