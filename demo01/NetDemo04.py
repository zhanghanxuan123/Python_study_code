'''
Created on 2016年11月24日

@author: lenovo
'''
import requests

r1 = requests.get('http://cn.bing.com/search?q=requests')  #get方法
#状态码，正常是200
str1 = r1.status_code    
#文件编码，比如'utf-8'
str2 = r1.encoding  
#文件全文  
str3 = r1.content    
#把请求回来的json数据转成Python字典并返回
#str4 = r1.json()    
#print (str3)

post_data={
'stock':'000001',
'searchkey':'',
'category':'category_ndbg_szsh;',
'pageNum':'1',
'pageSize':'',
'column':'szse_main',
'tabName':'fulltext',
'sortName':'',
'sortType':'',
'limit':'',
'seDate':''
}

r2 = requests.post('http://www.cninfo.com.cn/cninfo-new/announcement/query',data=post_data)    #
#print (r2.content)

r3 = requests.get('http://www.cninfo.com.cn/finalpage/2015-03-13/1200694563.PDF',stream = True)    #请求

r3.raw.read()   #读取文件（最好在括号里面加一下个数，只读前面几个，不然……可以试试看哈哈哈哈）
