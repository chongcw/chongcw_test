import pymysql
import xlrd
import matplotlib
import requests
from PIL import Image

import matplotlib.pyplot as plt
# import cv2

'''EXCEL TEST'''
'''xlsx = xlrd.open_workbook('c:\\Users\\chong\\P38new\\LEDPD.xlsx')
xlsx = xlrd.open_workbook('c:/Users/chong/P38new/LEDPD.xlsx')
print('%s'% xlsx.sheet_names())
sheet = xlsx.sheets()[0]
print('row 4:%s' % sheet.row_values(4))'''

'''MYSQL TEST'''
'''config = {
    'host':'127.0.0.1',
    'user':'ChongWANG',
    'password':'127907',
    'port':3306,
    'database':'pythontestdb',
    'charset':'utf8'
}
cnn = pymysql.connect(**config)
cursor = cnn.cursor()

sql = "select * from tb_student"
# sql = "select * from tb_student where age < 18 and gender = 1;"
cursor.execute(sql)

data = cursor.fetchall()
for i in data:
    print(i)

cursor.close()
cnn.close()'''


'''API TEST'''
'''
add = '南京软件谷科创城'
ak = 'gCKvsiPj8xnltkaoHaZ0lEC9Z9GVookG'
url = 'http://api.map.baidu.com/geocoder/v2/?address=%s&output=json&ak=%s'
res = requests.get(url % (add, ak))
add_info = res.text
print(add_info)
'''

'''Requests TEST'''
'''url = 'http://www.dataivy.cn/blog/dbscan'
res = requests.get(url)
html = res.text
print(html)'''

'''Pillow'''
'''file = 'Method.png'
img = Image.open(file, mode="r")

print('format:', img.format)
print('size:', img.size)
print('mode:', img.mode)
img.show()

imgarr = img.convert('L')
imgarr.show()
'''


