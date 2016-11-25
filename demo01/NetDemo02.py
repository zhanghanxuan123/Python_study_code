#爬取一个网站所有的url

import re
import urllib.request
import urllib
import queue
 
from collections import deque
import queue
 
queue = deque()
visited = set()
 
url = 'http://news.dbanotes.net'  # 入口页面, 可以换成别的
 
queue.append(url)
cnt = 0
 
while queue:
  url = queue.popleft()  # 队首元素出队
  visited |= {url}  # 标记为已访问
 
  print('已经抓取: ' + str(cnt) + '   正在抓取 <---  ' + url)
  cnt += 1
  urlop = urllib.request.urlopen(url,timeout=2)
  
  #所以会把那些.ico或者.jpg的链接都爬下来. 这样read()了之后碰上decode(‘utf-8′)就要抛出异常, 
  #因此我们用getheader()函数来获取抓取到的文件类型, 是html再继续分析其中的链接.
  if 'html' not in urlop.getheader('Content-Type'):
    continue
 
  # 避免程序异常中止, 用try..catch处理异常
  try:
    data = urlop.read().decode('utf-8')
  except:
    #urlop = urllib.request.urlopen(url,timeout=2) 
    continue
 
  # 正则表达式提取页面中所有队列, 并判断是否已经访问过, 然后加入待爬队列
  linkre = re.compile('href=\"(.+?)\"')
  str1 = linkre.findall(data)
  for x in linkre.findall(data):
    if 'http' in x and x not in visited:
      queue.append(x)
      print('加入队列 --->  ' + x)
