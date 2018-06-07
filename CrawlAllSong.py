import os
import requests
from bs4 import BeautifulSoup

FILE = 'D://spyder//'


# 创建新的文件夹
def creatFile(element):
    path = FILE
    title = element
    new_path = os.path.join(path, title)
    if not os.path.isdir(new_path):
        os.makedirs(new_path)
    return new_path


# 获取网页信息
def downLoad(url):
    html = requests.get(url)
    html.encoding = 'utf-8'
    return html


# 爬取网页中的指定信息
def get_info(html, flag, fOut):
    f = open(fOut, 'a', encoding='utf-8')
    soup = BeautifulSoup(html.text, 'lxml')
    li = soup.find_all('li', attrs={'class': ['bb-dotimg', 'clearfix', 'song-item-hook', 'csong-item-hook']})
    for i in li:
        song_item = i.find('div', attrs={'class': ['song-item', 'clearfix']})
        # time.sleep(0.1)
        try:
            singerRaw = song_item.find('span', attrs={'class': 'singer'})
            singer = singerRaw.find('span', attrs={'class': 'author_list'})['title']  # 歌手
            ul = song_item.find('span', attrs={'class': 'song-title'})
            info = ul.find('a', attrs={'target': '_blank'})
            title = info.get_text()  # 获取歌曲标题
            songUrl = info['href']  # 获取歌曲链接
            f.write(str(flag) + ';' + singer + ';' + title + ';' + 'http://music.baidu.com' + songUrl + '\n')
            flag += 1
        except:
            print('歌曲已经下架，爬取有误！')
    pageurl = soup.find('a', attrs={'class': 'page-navigator-next'})

    f.close()
    if pageurl:
        #         print(pageurl['href'])
        return flag, pageurl['href'].strip()
    return flag, None


def main():
    fInput = open('songTag.txt', 'r', encoding='utf-8')
    print("-----")
    line = fInput.readline()
    while line:
        print('开始下一个主题音乐爬取')
        lin = line.strip()
        if len(lin) < 7:
            b = list(lin)[0:-1]
            b = str(b[0] + b[1])
            path = creatFile(b)
            line = fInput.readline()
        else:
            store = lin.split(';')
            tag = store[0]
            fOutput = path + '//' + tag + '.txt'
            href = store[1]
            url = href.strip()
            i = 1
            print(tag + '--' + url)
            while url:  # 用于歌曲页码下一页的跳转
                urls = 'http://music.baidu.com' + url
                html = downLoad(urls)
                i, url = get_info(html, i, fOutput)  # i是歌单下歌曲序号，url为下一页的网址链接。
            line = fInput.readline()
    fInput.close()
    print("over")


if __name__ == '__main__':
    main()