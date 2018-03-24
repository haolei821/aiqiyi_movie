# coding: utf-8


import requests
from lxml import etree
import pandas as pd


headers = {
    'Referer':'http://www.iqiyi.com/dianying/',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
}
response = requests.get('http://www.iqiyi.com/dianying_new/i_list_paihangbang.html',headers=headers).text
html = etree.HTML(response)
lis = html.xpath('//*[@id="widget-tab-0"]/div[2]/div/div[1]/ul/li[1]')
# print(lis)

title = li.xpath('//div[@class="title"]/p/a/text()')
link = li.xpath('//div[@class="title"]/p/a/@href')
score_front = li.xpath('//span[@class="score"]/strong/text()')
score_back = li.xpath('//span[@class="score"]/text()')
score = [str(i)+str(j) for i, j in zip(score_front,score_back)]
describe = li.xpath('//p[@class="site-piclist_info_describe"]/text()')
data = {
    'title':title,
    'link':link,
    'score':score,
    'describe':describe,
}

for i in field():
#     print(i)
    df = pd.DataFrame(i)
df.to_csv("d:\\desktop\\data.csv")

