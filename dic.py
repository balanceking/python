# -*- coding:utf-8 -*-
#字典
dict={'name':'laowang','age':'22','class':'first'}
print("dict['name']:",dict['name'])
print("dict['age']:",dict['age'])
#访问不存在的值
#print(dict['shabi'])

#修改值
print("修改前",dict['age'])
dict['age']=23
print("修改后：",dict['age'])

#删除
del dict['age']# 删除键是'Name'的条目
#print("dict['age']: ", dict['age'])#引发异常
dict.clear()    # 清空词典所有条目
print(dict)
del dict      # 删除词典