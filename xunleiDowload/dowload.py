import os

#下载的目录
save_path = "D:/迅雷下载" 
downUrl='ftp://ygdy8:ygdy8@yg18.dydytt.net:7012/阳光电影www.ygdy8.com.饥饿站台.BD.1080p.中英双字幕.mkv'
def get_filename(url):
    return os.path.split(url)[1]

fileNames = get_filename(downUrl)

print(fileNames)

def check_start(filename):
    cache_file = filename+".xltd"
    return os.path.exists(os.path.join(save_path,cache_file))

def check_end(fiename):
    return os.path.exists(os.path.join(save_path,fiename))

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


