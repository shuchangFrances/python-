# python-
爬取百度歌单


#**思路**：首先爬取标签（如热门，风格等）以及标签下歌单的链接，然后据此爬取所有歌单下的歌曲信息


#**所需模块**：requests、BeautifulSoup、os等模块  
 ##requests模块用于请求网页；BeautifulSoup用于解析网页、os模块用于创建文件夹

#**步骤**：1.爬取标签及歌单链接 CrawlSongTag.py
     2.歌曲爬取 CrawlSongTag.py

#**文件说明**：1.CrawlSongTag.py&CrawlSongTag.py为爬取文件 2.风格、热门、心情分别为爬取到的歌单列表  3.SongTag.txt为爬取到的标签

#**图片展示**  
##![爬取的标签](https://github.com/shuchangFrances/python-/blob/master/%E6%88%AA%E5%9B%BE%E5%B1%95%E7%A4%BA/%E6%A0%87%E7%AD%BE.png)
