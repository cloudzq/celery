# -*- coding:utf-8 -*-
"""
@Project:watchmen
@Language:Python3.6.4
@Author:Hans
@File:onexima.py
@Ide:PyCharm
@Time:2018/7/20 20:46
@Remark:爬取一个专辑前7页的音频
"""

import requests
import json
import re


# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
# ret = requests.get("", header=headers)
# result = ret.content.decode()
# print(result)


class Xima(object):
    def __init__(self, book_name,id):
        self.book_name = book_name
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
        }
        self.start_url = "https://www.ximalaya.com/revision/play/album?albumId=%s&pageNum={}&sort=-1&pageSize=30"%id
        self.book_url=[] #所有页面的url
        for i in range(8):
            url=self.start_url.format(i+1)
            self.book_url.append(url)


    def get_book_msg(self):
        all_list = []
        for url in self.book_url:
            r = requests.get(url, headers=self.headers)
            python_dict = json.load(r.content.decode())
            book_list = python_dict['data']['tracksAudioPlay']
            for i in book_list:
                list = {}
                list['name'] = i['trackName']
                list['src'] = i['src']
                all_list.append(list)  # ctrl+d
                print(list)
        return list

    def save(self, all_list):
        """"保存音频信息到本地"""
        for i in all_list:
            i['name']=re.sub('"|\|','',i['name'])
            with open('xiam/{}.m4a'.format(self.book_name + i['name'], 'ab')) as f:
                print('正在保存第%d条音频' % (all_list.index(i) + 1))
                r = requests.get(i['src'], headers=self.headers)
                f.write(r.content)

    def run(self):
        all_list = self.get_book_msg()
        self.save(all_list)


if __name__ == '__main__':
    xima = Xima(name,id)
    xima.run()
