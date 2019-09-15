import requests
from bs4 import BeautifulSoup
def fetch_fnc(url,cl):
    import re
    import io
    fn= re.sub('[^A-Za-z0-9-_]+', '', url.split("/")[-1]) + ".txt"
    fn
    encoding = 'utf-8'
    f = io.open(fn, "w+",encoding='utf-8')
    page = requests.get(url)
    page.status_code
    soup = BeautifulSoup(page.content, 'html.parser')
    f.write(unicode(url))
    TBLRoll=soup.find_all(class_=cl)
    for each in TBLRoll:
        if each.get_text():
            f.write( '' +  each.get_text().rstrip().replace('\n\n', ' '))
    f.close()

