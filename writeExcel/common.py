import openpyxl
import urllib.request
import datetime
import time
import os
import re

filePath = "F:/E/git/python-learn/writeExcel/download/" 
#换成自己的下载目录地址
wb = openpyxl.load_workbook('file/allhref.xlsx')
#换成自己的exal目录

sheets = wb.sheetnames

def WriteTime(i, Val, row):       
    sheetFile = wb['Sheet1']
    sheetFile[row+'%d'%i] = Val
    wb.save('file/allhref.xlsx')

def getCurrentTime():
    now_time = (datetime.datetime.now()).strftime("%Y-%m-%d %H:%M:%S")
    return now_time