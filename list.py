# -*- coding:utf-8 -*-

#创建list
print('创建list。。。')
list1 =['math','chinses','english',1996,2018]
list2 =[1,2,3,4,5]
list3 =["a","b","c","d"]

print('list1[0]:',list1[0])
print('list2[1:5]:',list2[1:5])
print('list3:',list3)

#更新

print("更新list。。。")
print("索引 2 的值: ")
print(list1[2])
list1[2]=2008
print("索引2更新后的值为 : ")
print(list1[2])

#删除

print("删除list...")
print("删除索引2处的值之前: ")
print(list1)
del(list1[2])
print("删除索引2处的值之后: \n",list1)

#操作符

print('操作符。。。')
print('list1:',list1)
print('list2:',list2)
list4=list1+list2
print('list1+list2:',list4)
list5=['hi']*5
print('[\'hi\']*5:',list5)

#截取
print('列表截取。。。')
L=['老','王','老王！']
print(L[2])
print(L[-2])
print(L[1:])

