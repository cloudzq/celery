# -*- coding:utf-8 -*-
"""
@Project:watchmen
@Language:Python3.6.4
@Author:Hans
@File:allxima.py
@Ide:PyCharm
@Time:2018/7/21 10:43
@Remark:获取排行榜前50哥专辑的音频
"""
import re
import requests
from lxml import etree

from onexima import Xima


def get_id():
    """获取排行榜每个专辑的id和名字"""
    main_url = "https://www.ximalaya.com/shangye/top/"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    r = requests.get(main_url, headers=headers)  # r是状态码
    html = etree.HTML(r.content.decode())
    div_list = html.xpath('//div[contains(@class,"e-2997888007 rrc-album-item")]')
    all_list = [] # dict
    for div in div_list:
        author={} # {'name':'吴晓波频道','id':'3385980'}
        r = div.xpath('./a/@href')[0]
        re.search(r'')
    return all_list

all_list = get_id()
for li in all_list:
    Xima(name,id)