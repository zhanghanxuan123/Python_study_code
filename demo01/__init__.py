#!/usr/bin/python3
#encoding:UTF-8
'''
 import pickle
 
 # ʹ��pickleģ�齫���ݶ��󱣴浽�ļ�
 data1 = {'a': [1, 2.0, 3, 4+6j],
          'b': ('string', u'Unicode string'),
          'c': None}
 
 selfref_list = [1, 2, 3]
 selfref_list.append(selfref_list)
 
 output = open('data.pkl', 'wb')
 
 # Pickle dictionary using protocol 0.
 pickle.dump(data1, output)
 
 # Pickle the list using the highest protocol available.
 pickle.dump(selfref_list, output, -1)
 
 output.close()
 class JustCounter:
     __secretCount = 0  # ˽�б���
     publicCount = 0    # ��������
 
     def count(self):
         self.__secretCount += 1
         self.publicCount += 1
         print (self.__secretCount)
 
 counter = JustCounter()
 counter.count()
 counter.count()
 print (counter.publicCount)
 print (counter.__secretCount)  # ����ʵ�����ܷ���˽�б���
 import sys
 
 print(sys.argv)
 from urllib.request import urlopen
 for line in urlopen('http://tycho.usno.navy.mil/cgi-bin/timer.pl'):
     line = line.decode('utf-8')  # Decoding the binary data to text.
     if 'EST' in line or 'EDT' in line:  # look for Eastern Time
         print(line)

 д�ļ�
 with open("F://abc.txt", "wt") as out_file:
     out_file.write("���ı���д�뵽�ļ���\n�������˰ɣ�")
  
 # Read a file
 with open("F://abc.txt", "rt") as in_file:
     text = in_file.read()
  
 print(text)
'''
'''
import urllib.request
from builtins import str
url = "http://www.baidu.com"
data = urllib.request.urlopen(url).read()
data = data.decode('UTF-8')
newdata = str(data)
print(data)
'''




























