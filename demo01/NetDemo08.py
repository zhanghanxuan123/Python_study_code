'''
Created on 2016年11月25日

@author: lenovo
'''
#导入所需的库  
import urllib.request,socket,re,sys,os 
import requests
from bs4 import BeautifulSoup
from builtins import str
from collections import deque
import queue

#定义文件保存路径  
targetPath = "D:\picture"


def saveFile(path,name):  
    #检测当前路径的有效性  
    dir = str("gzsx")
    newfile = targetPath
    #print (path)
    if not os.path.isdir(newfile):  
        os.mkdir(newfile)
  
    #设置每个图片的路径  
    #"/"最后出现的位置
    pos = path.rindex('/')
    path01 = path[pos+1:]
    newpos = path01.rindex(".")
    newname = name+path01[newpos:]
    print (newname)
    name += path[pos+1:]
    t = os.path.join(newfile,newname) 
    return t

r = requests.get('http://web.lswgyxx.com/xxgk/jsfc/index.html')
html = r.content
soup = BeautifulSoup(html,'html.parser')    #html.parser是解析器
div_subject_list = soup.find("div",attrs={"id":"sideBarContent"})
subject_list = div_subject_list.find_all("a",attrs={'target': '_self'})
for subjecet_kind in subject_list:
    subjecet_kind_url = subjecet_kind["href"]
    subjecet_kind_name = subjecet_kind.get_text()
    #print (subjecet_kind_url)
    r1 = requests.get(subjecet_kind_url)
    html01 = r1.content
    soup = BeautifulSoup(html01,'html.parser')
    div_people_list = soup.find_all('div', attrs={'photo'})
    for a_s in div_people_list:
        a = a_s.find("a")
        url = a["href"]
        name = a["title"]
        img = a_s.find("img")
        pic_url = img["src"]
        print (name)
        urllib.request.urlretrieve(pic_url,saveFile(pic_url,name))
    queue = deque()
    visited = set()
    span_page_list = soup.find("span",attrs={"currentPagination"})
    index_list = span_page_list.find_all("a")
    for index_url in index_list:
        a = index_url["href"]
        #index_url = list(set(index_url))
        #new_list.set(a)
        queue.append(a)
        #print (queue)
        while queue:
            url_last = queue.popleft()  # 队首元素出队
            pos01 = url.rindex("/")
            url_head = url[0:48]
            pos02 = url_head.rindex("/")
            url_new_head = url_head[0:38]
            url_new_head += url_last
            #print (url_new_head)
            if url_last not in visited:
                #print (url_last)
                visited |= {url_last}  # 标记为已访问
                r2 = requests.get(url_new_head)
                html02 = r2.content
                soup = BeautifulSoup(html02,'html.parser')
                div_people_list01 = soup.find_all('div', attrs={'photo'})
                #print (div_people_list01)
                for a_s1 in div_people_list01:
                    a1 = a_s1.find("a")
                    url1 = a1["href"]
                    name1 = a1["title"]
                    img1 = a1.find("img")
                    pic_url1 = img1["src"]
                    print (name1)
                    urllib.request.urlretrieve(pic_url1,saveFile(pic_url1,name1))
                    #print (html02)
            
            
    
    #print (index_list)

  #http://web.lswgyxx.com/xxgk/jsfc/gzyw/2014-02-25/1393290752d5709.html

#s = saveFile("http://web.lswgyxx.com/xxgk/jsfc/kyt/h000/h22/img201402260922150.jpg")
#print (s)


