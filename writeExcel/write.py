import openpyxl
import urllib.request
import time
import os

filePath = "F:/E/git/python-learn/writeExcel/download/" 
#换成自己的下载目录地址
wb = openpyxl.load_workbook('file/allhref.xlsx')
#换成自己的exal目录

sheets = wb.sheetnames
# print(sheets, type(sheets)) 

def getHref(ws):
    # print(ws['A']) A一竖列
    #循环B数列
    i = 0
    for href in  ws['B']: 
        name = (ws['A'][i].value)
        i = i + 1
        if href.value != 'href': 
             dowload(href.value, name)
        

         
def dowload(url, fileName):
        response = urllib.request.urlopen(url)
        data = response.read()
        t = int(time.time() * 1000)
        os.mkdir("download/"+fileName)
        name = filePath +fileName+"/"+ '%d'%t+".jpg"
        print(name)
        with open(name, 'wb') as code:
            code.write(data)
            print('finish')


for sheet in sheets:        # 循环表
   if(sheet == 'Sheet1'): getHref(wb[sheet])
        # wb[sheet]




