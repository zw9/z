import requests
from bs4 import BeautifulSoup
import re
import io

def fetch_p(url):

    # url = "https://www.nguoi-viet.com/sinh-hoat-cong-dong/sinh-hoat-cong-dong/"


    fn = re.sub('[^A-Za-z0-9-_]+', '', url.split("/")[-2]) + ".txt"
    encoding = 'utf-8'
    f = io.open(fn, "w", encoding='utf-8')
    f.write(fn + "\n")
    print(fn)
    page = requests.get(url)
    page.status_code
    soup = BeautifulSoup(page.content, 'html.parser')
    ctl01_PageHead = soup.title
    print("## " + ctl01_PageHead.get_text() + "  ")
    f.write("## " + ctl01_PageHead.get_text() + "\n")
    TBLRoll = soup.find_all('a')
    for each in TBLRoll:
        if each.get_text():
            #print(each.get_text() + "  ")
            f.write(each.get_text() + "\n")
    f.close()


# fetch_p("https://www.nguoi-viet.com/sinh-hoat-cong-dong/sinh-hoat-cong-dong/")

def fetch_menuitem(url):
    page = requests.get(url)
    page.status_code
    soup = BeautifulSoup(page.content, 'html.parser')
    ctl01_PageHead = soup.title
    print("## " + ctl01_PageHead.get_text() + "  ")
    TBLRoll = soup.findAll('a')
    cl = 'TBLRoll'
    for each in TBLRoll:
        if (each.get('href')):
            print(each.get('href'))
            #print("fetch_p(\"https://raovat.nguoi-viet.com" + each['value'] + "\")")
            #url_c = "https://raovat.nguoi-viet.com" + each['value']
            try:
                fetch_p(each.get('href'))
            except:
                print("url is bad: " + each.get('href'))
