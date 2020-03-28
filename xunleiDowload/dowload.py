import os
import time

#下载的目录
save_path = "D:/迅雷下载" 
downUrl1='ftp://dygod1:dygod1@d215.dygod.org:8005/哈利·波特与死亡圣器(上)/[电影天堂www.dy2018.net]哈利·波特与死亡圣器(上)BD中英双字.rmvb'
downUrl2='ftp://ygdy8:ygdy8@yg45.dydytt.net:4235/阳光电影www.ygdy8.com.82年生的金智英.HD.1080p.韩语中字.mkv'
downUrl3='ftp://ygdy8:ygdy8@yg76.dydytt.net:5935/[阳光电影-www.ygdy8.com]梨泰院Class-01.mp4'
downUrl4='ftp://ygdy8:ygdy8@yg76.dydytt.net:5935/[阳光电影-www.ygdy8.com]梨泰院Class-02.mp4'
downUrl5='ftp://ygdy8:ygdy8@yg76.dydytt.net:5941/[阳光电影-www.ygdy8.com]梨泰院Class-03.mp4'
#ftp://ygdy8:ygdy8@yg76.dydytt.net:5942/[阳光电影-www.ygdy8.com]梨泰院Class-04.mp4
#ftp://ygdy8:ygdy8@yg76.dydytt.net:5947/[阳光电影-www.ygdy8.com]梨泰院Class-05.mp4
#ftp://ygdy8:ygdy8@yg76.dydytt.net:5947/[阳光电影-www.ygdy8.com]梨泰院Class-06.mp4
#ftp://ygdy8:ygdy8@yg76.dydytt.net:5954/[阳光电影-www.ygdy8.com]梨泰院Class-07.mp4
#ftp://ygdy8:ygdy8@yg76.dydytt.net:5954/[阳光电影-www.ygdy8.com]梨泰院Class-08.mp4
#ftp://ygdy8:ygdy8@yg76.dydytt.net:5961/[阳光电影-www.ygdy8.com]梨泰院Class-09.mp4
#ftp://ygdy8:ygdy8@yg76.dydytt.net:5961/[阳光电影-www.ygdy8.com]梨泰院Class-10.mp4
#ftp://ygdy8:ygdy8@yg76.dydytt.net:5968/[阳光电影-www.ygdy8.com]梨泰院Class-11.mp4
#ftp://ygdy8:ygdy8@yg76.dydytt.net:5968/[阳光电影-www.ygdy8.com]梨泰院Class-12.mp4
#ftp://ygdy8:ygdy8@yg76.dydytt.net:5974/[阳光电影-www.ygdy8.com]梨泰院Class-13.mp4
#ftp://ygdy8:ygdy8@yg76.dydytt.net:5974/[阳光电影-www.ygdy8.com]梨泰院Class-14.mp4
#ftp://ygdy8:ygdy8@yg76.dydytt.net:5980/[阳光电影-www.ygdy8.com]梨泰院Class-15.mp4
#ftp://ygdy8:ygdy8@yg76.dydytt.net:5980/[阳光电影-www.ygdy8.com]梨泰院Class-16.mp4

def get_filename(url):
    return os.path.split(url)[1]

def check_start(filename):
    cache_file = filename+".xltd"
    return os.path.exists(os.path.join(save_path,cache_file))

def check_end(fiename):
    return os.path.exists(os.path.join(save_path,fiename))


time.sleep(500)

def downloadFile(downUrl): 
    fileNames = get_filename(downUrl)
    isFinish = not check_end(fileNames)
    isExist = not check_start(fileNames)
    
    if(isExist):
        #如果这个任务不存在
        print('开始')
        #迅雷exe的目录地址
        os.system("\"D:\\C\\Thunder\\Program\\Thunder.exe\" -StartType:DesktopIcon %s"%downUrl)
    else:
        if(isFinish):
            print('继续')
        #没有继续开启任务的命令，没找到，开机自动继续

downloadFile(downUrl1)
downloadFile(downUrl2)
downloadFile(downUrl3)
downloadFile(downUrl4)
downloadFile(downUrl5)
