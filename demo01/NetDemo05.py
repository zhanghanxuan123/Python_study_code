'''
Created on 2016年11月24日

@author: lenovo
'''
import requests
from bs4 import BeautifulSoup

def getHTML(url):
    r = requests.get(url)
    return r.content

def parseHTML(html):
    soup = BeautifulSoup(html,'html.parser')

    body = soup.body
    company_middle = body.find('div',attrs={'class':'middle'})
    company_list_ct = company_middle.find('div',attrs={'class':'list-ct'})

    for company_ul in company_list_ct.find_all('ul',attrs={'class':'company-list'}):
        for company_li in company_ul.find_all('li'):
            company_url = company_li.a['href']
            company_info = company_li.get_text()
            print (company_info,company_url)

URL = 'http://www.cninfo.com.cn/cninfo-new/information/companylist'
html = getHTML(URL)
parseHTML(html)