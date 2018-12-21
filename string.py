# -*- coding:utf-8 -*-

#声明字符串
str1 ='hello world!'
str2 ="hello 老王"
print('声明字符串。。。')
print(str1)
print(str2)

#访问字符内容
print('访问字符内容。。。')
print("str1[0]:",str1[0])
print("str2[1:8]:",str2[1:8])

#字符串操作符
print('字符串操作符。。。')
a ="hello"
b ="python"

print("a + b 输出结果：", a + b)
print("a * b 输出结果：", a * 2)
print("a[1] 输出结果：", a[1])
print("a[1:6] 输出结果：", a[1:4])

if("h" in a):
    print("h在变量a中")
else:
    print("h不在变量a中")

if ("m" not in b):
    print("m不在变量B中")
else:
    print("m在变量B中")

print(r'\n')
print(R'\n')

#字符串格式化
print('my name is %s and higth is %d cm!'%('lw',170))
print("formart method call:my name is {name} and higth is {hight} cm".format(name='lw',hight='170'))

#三引号
print('三引号。。。')
hi='''hello
    i
        am
            lw'''
print(hi)