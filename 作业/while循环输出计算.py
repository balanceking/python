# -*- coding:utf-8 -*-

i=2
sum=0
while i<=100:
    if i%2==0:
        sum=sum+i
    else:
        sum=sum-i
    i+=1
print('2-3+4-5+6.....+100的和为：',sum)