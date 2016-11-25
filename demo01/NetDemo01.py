#encoding:UTF-8

import urllib.request
url = "http://www.baidu.com"
data = urllib.request.urlopen(url).read()
data = data.decode('UTF-8')
#print(data)
print (urllib.request.urlopen(url).getheader("'Content-Type'"))

#===============================================================================
# import urllib
# import urllib.request
#===============================================================================
""" 
data={}
data['word']='Jecvay Notes'
 
url_values=urllib.parse.urlencode(data)
url="http://www.baidu.com/s?"
full_url=url+url_values
 
data=urllib.request.urlopen(full_url).read()
data=data.decode('UTF-8')
print(data)

s = 'ABC\\-001'
print (s)
"""
'''
import re
re.match(r'^\d{3}\-\d{3,8}$', '010-12345')
'''
'''
import re
test = '用户输入的字符串'
if re.match(r'正则表达式', test):
    print('ok')
else:
    print('failed')
'''
'''
from collections import deque
queue=deque(["peace","rong","sisi"])
queue.append("nick")
queue.append("pishi")
print(queue.popleft())
print(queue.popleft())
print(queue)
'''










