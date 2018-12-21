# -*- coding:utf-8 -*-
list1=[0,1,2,3,4,5,6,7,8,9]
print("正序list1：",list1)
print("逆序list1：",list1[::-1])

#百度笔记
#>>> lst = [1,2,3,4,5,6]                #创建测试列表

#方法1： 
#>>> lst.reverse()                      #reverse()反转
#>>> lst
#[6, 5, 4, 3, 2, 1]

#方法2：
#>>> lst1 = [i for i in reversed(lst)]  #reversed只适用于与序列(列表、元组、字符串)
#>>> lst1
#[6, 5, 4, 3, 2, 1]

#方法3:
#>>> lst2 = sorted(lst,reverse=True)    #sorted+reverse适用于序列(列表、元组、字符串)、集合、字典
#>>> lst2
#[6, 5, 4, 3, 2, 1]

#方法4:
#>>> lst3 = lst[::-1]                    #切片用法：创建一个与原字符串顺序相反的字符串
#>>> lst3
#[6, 5, 4, 3, 2, 1]