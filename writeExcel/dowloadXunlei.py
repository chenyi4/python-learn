import os
import time
import common

save_path = "D:/迅雷下载" 

def download(url, name, i):
    downloadFile(url, i)

def get_filename(url):
    return os.path.split(url)[1]

def check_start(filename):
    cache_file = filename+".xltd"
    return os.path.exists(os.path.join(save_path,cache_file))

def check_end(fiename):
    return os.path.exists(os.path.join(save_path,fiename))

def downloadFile(downUrl, i):
    fileNames = get_filename(downUrl)
    isFinish = not check_end(fileNames)
    isExist = not check_start(fileNames)
    
    if(not isFinish): 
        print('==已经完成==')
        common.WriteTime(i, "已经完成", 'D')
    else:
        if(isExist):
            #如果这个任务不存在
            print('开始')
            #迅雷exe的目录地址
            os.system("\"D:\\C\\Thunder\\Program\\Thunder.exe\" -StartType:DesktopIcon %s"%downUrl)
        else:
            if(isFinish):
                print('继续')