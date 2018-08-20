# -*- coding:utf-8 -*-
"""
@Project:watchmen
@Language:Python3.6.4
@Author:Hans
@File:WeChatFrends.py
@Ide:PyCharm
@Time:2018/7/19 15:10
@Remark:
"""

import itchat
import os,math,random
import PIL.Image as Image
from pandas import DataFrame

itchat.login()
friends = itchat.get_friends(update=True)[0:]
# with open('friends.json','w') as fw:
#     fw.write('%s' % '\n'.join('%s' %id for id in friends))
# 男女比例 key=sex,male=1,female=2

male = female = other = 0
for i in friends[1:]:
    sex = i["Sex"]
    if sex == 1:
        male += 1
    elif sex == 2:
        female += 1
    else:
        other += 1
total = len(friends[1:])

# print("男性好友: %.2f%%" % (float(male) / total * 100) + "\n" +
#       "女性好友:%.2f%%" % (float(female) / total * 100) + "\n" +
#       "不满性别好友:%.2f%%" % (float(other) / total * 100))

# 自己微信好友的城市分布
# def get_var(var):
#     variable = []
#     for i in friends:
#         value = i[var]
#         variable.append(value)
#     return variable
#
# NickName = get_var("NickName")
# RemarkName=get_var("RemarkName")
# Sex = get_var("Sex")
# Province = get_var("Province")
# City = get_var("City")
# Signature = get_var("Signature")

# data = {'昵称': NickName, '备注': RemarkName, '性别': Sex, '省份': Province, '城市': City, '签名': Signature}
# frame = DataFrame(data)
# frame.to_excel('friends.xlsx', index=True)

#微信好友头像拼接图
# def headImg():
#     itchat.login()
#     friends = itchat.get_friends(update=True)
#     # itchat.get_head_img() 获取到头像二进制，并写入文件，保存每张头像
#     for count, f in enumerate(friends):
#         # 根据userName获取头像
#         img = itchat.get_head_img(userName=f["UserName"])
#         imgFile = open("img/" + str(count) + ".jpg", "wb")
#         imgFile.write(img)
#         imgFile.close()
# def createImg():
#     x = 0
#     y = 0
#     imgs = os.listdir("img")
#     random.shuffle(imgs)
#     # 创建640*640的图片用于填充各小图片
#     newImg = Image.new('RGBA', (640, 640))
#     # 以640*640来拼接图片，math.sqrt()开平方根计算每张小图片的宽高，
#     width = int(math.sqrt(640 * 640 / len(imgs)))
#     # 每行图片数
#     numLine = int(640 / width)
#
#     for i in imgs:
#         img = Image.open("img/" + i)
#         # 缩小图片
#         img = img.resize((width, width), Image.ANTIALIAS)
#         # 拼接图片，一行排满，换行拼接
#         newImg.paste(img, (x * width, y * width))
#         x += 1
#         if x >= numLine:
#             x = 0
#             y += 1
#
#     newImg.save("all.png")

# 自己微信好友个性签名的自定义词云图
# import re
#
# siglist = []
# for i in friends:
#     signature = i["Signature"].strip().replace("span", "").replace("class", "").replace("emoji", "")
#     rep = re.compile("1f\d+\w*|[<>/=]")
#     signature = rep.sub("", signature)
#     siglist.append(signature)
# text = "".join(siglist)
#
# import jieba
#
# wordlist = jieba.cut(text, cut_all=True)
# word_space_split = "".join(wordlist)
#
# import matplotlib.pyplot as plt
# from wordcloud import WordCloud, ImageColorGenerator
# import numpy as np
# import PIL.Image as image
#
# coloring = np.array(image.open("/Users/Desktop/wechat.jpg"))
# my_wordcloud = WordCloud(background_color="white", max_words=2000, mask=coloring,
#                          max_font_size=60, random_state=42, scale=2,
#                          font_path="Library/Fonts/Microsoft/SimHei.ttf").generate(word_space_split)
# image_colors = ImageColorGenerator(coloring)
# plt.imshow(my_wordcloud.recolor(color_func=image_colors))
# plt.imshow(my_wordcloud)
# plt.axis("off")
# plt.show()

#公众号的获取
# itchat.auto_login(hotReload=True)
# mpsList=itchat.get_mps(update=True)[1:]
# total=0
# for it in mpsList:
#     # mps_data = {it['NickName']+':'+it['Signature']}
#     # frame = DataFrame(mps_data)
#     # frame.to_excel('Public_number.xlsx', index=True)
#     print(it['NickName']+':'+it['Signature'])
#     total=total+1
#
# print('公众号的数目是%d'%total)

#获取微信群用户信息
name = '《商服会场》'
roomslist = []

# itchat.auto_login(enableCmdQR = False)

# def getroom_message(n):
#     #获取群的username，对群成员进行分析需要用到
#     itchat.dump_login_status() # 显示所有的群聊信息，默认是返回保存到通讯录中的群聊
#     RoomList =  itchat.search_chatrooms(name=n)
#     if RoomList is None:
#         print("%s group is not found!" % (name))
#     else:
#         return RoomList[0]['UserName']
#
# def getchatrooms():
#     #获取群聊列表
#     roomslist = itchat.get_chatrooms()
#     # print(roomslist)
#     return roomslist
#
# for i in getchatrooms():
#     #print(i['NickName'])
#     roomslist.append(i['NickName'])
#
# with open('群用户名.txt', 'a', encoding='utf-8')as f:
#     for n in roomslist:
#         ChatRoom = itchat.update_chatroom(getroom_message(n='《商服会场》'), detailedMember=True)
#         for i in ChatRoom['MemberList']:
#             f.write( i['NickName']+ " " +i['RemarkName']+ " " +str(i['Sex'])+ " " +i['Province']+ " " +i['City']+ " " +i['Signature'] + '\n')
#             print('正在写入           '+i['Province']+":",i['NickName'])
#     f.close()

#群聊列表
# itchat.auto_login(hotReload=True)
# #itchat.run()
# mpsList=itchat.get_chatrooms(update=True)[1:]
# total=0
# for it in mpsList:
#     print(it['NickName'])
#     total=total+1
#
# print('群聊的数目是%d'%total)
# itchat.dump_login_status()