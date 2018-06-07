# 首先爬取标签以及标签下歌单的链接；然后据此爬取所有歌单下的歌曲信息
import requests
from bs4 import BeautifulSoup


# 获取网页信息
def get_html(url):
    html = requests.get(url)
    html.encoding = 'utf-8'
    return html


def get_info(html):
    f = open('songTag.txt', 'w', encoding='utf-8')
    soup = BeautifulSoup(html.text, 'lxml')
    tagOne = soup.find_all('dl', attrs={'class': 'tag-mod'})
    for tag_items in tagOne:
        tag = tag_items.find('dt').get_text()  # 获取标签名
        f.write(tag + ':\n')
        tag_list = tag_items.find_all('span', attrs={'class': ['tag-list', 'clearfix']})
        for tag_item in tag_list:
            info = tag_item.find('a')
            title = info.get_text()  # 获取分类名称
            href = info['href']  # 获取分类的链接
            f.write('\t' + title + ';' + href + '\n')
    f.close()


def main():
    url = 'http://music.baidu.com/tag'
    soup = get_html(url)
    get_info(soup)
    print('Over!')


if __name__ == '__main__':
    main()