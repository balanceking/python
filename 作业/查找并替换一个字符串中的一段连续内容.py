# -*- coding:utf-8 -*-
#查找
str1='a,b,c,d,e,f'
tofind='c'
if(str1.find(tofind)>0):
    print(str1.find(tofind)+1)
else:
    print('不存在')

#替换
print('替换前：',str1)
replace='qqq'
str2=str1.replace('c',replace)
print('替换后：',str2)