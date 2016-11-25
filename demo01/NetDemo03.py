#乐外教师信息，单页爬取
import requests
from bs4 import BeautifulSoup
from builtins import str
r = requests.get('http://web.lswgyxx.com/xxgk/jsfc/gzsx/index_2.html')
html = r.content
soup = BeautifulSoup(html,'html.parser')    #html.parser是解析器
div_people_list = soup.find_all('div', attrs={'photo'})
for a_s in div_people_list:
    a = a_s.find("a")
    url = a["href"]
    name = a["title"]
    img = a_s.find("img")
    pic_url = img["src"]
    print (name ,"||" ,url,"||",pic_url)
    
