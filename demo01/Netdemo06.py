# -*- coding: utf-8 -*-
import codecs
import csv
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
    
    company_list = []    #修改
    for company_ul in company_list_ct.find_all('ul',attrs={'class':'company-list'}):
        for company_li in company_ul.find_all('li'):
            company_url = company_li.a['href']
            company_info = company_li.get_text()
            company_list.append([company_info,company_url])    #修改
    
    return company_list    #修改


def writeCSV(file_name,data_list):
    with open(file_name,'w') as f:
        writer = csv.writer(f)
        for data in data_list:
            writer.writerow(data)
            


URL = 'http://www.cninfo.com.cn/cninfo-new/information/companylist'
html = getHTML(URL)
data_list = parseHTML(html)    #修改
writeCSV('F://test.csv',data_list)
