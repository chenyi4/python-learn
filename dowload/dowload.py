import urllib.request

if __name__ == '__main__':
    print("downloading with urllib")
    # url = 'http://www.wzsky.net/img2013/uploadimg/20130906/1216294.jpg'
    url = 'http://music.163.com/song/media/outer/url?id=436514312.mp3'
    f = urllib.request.urlopen(url)
    data = f.read()
    # 存储位置可自定义
    with open("F:/E/python/test/dowload/file/tes.mp3", 'wb') as code:
        code.write(data)