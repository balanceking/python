# -*- coding: UTF-8 -*-

#函数声明
def sayhello():
    print('hello laowang!')

sayhello() #函数调用

#参数

def printmax(a,b):
    if a>b:
        print(a,'is maximum')
    else:
        print(b,'is maximum')
printmax(3,4)

x=5
y=7
print('参数传递')
printmax(x,y)

#局部变量
def func(x):
    print('x is',x)
    x=2
    print('changed local x to',x)
print('局部变量')
x=50
func(x)
print('x is still',x)

#访问外部变量
def func2():
    global x
 
    print('x is', x)
    x = 2
    print('Changed local x to', x)
print('访问外部变量')
x = 50
func2()
print('Value of x is', x)

#默认参数
def say(message,times=1):
    print(message*times)

print('默认参数。。。')
say('hello')
say('world',5)

#关键字传参
def func3(a, b=5, c=10):
    print('a is', a, 'and b is', b, 'and c is', c)
 
func3(3, 7)
func3(25, c=24)
func3(c=50, a=100)

#return
def maximum(x, y):
    if x > y:
        return x
    else:
        return y
print('return。。。。。')
print(maximum(2, 3))

def someFunction():
    pass
print(someFunction())

#docstrings
def printMax2(x, y):
    '''Prints the maximum of two numbers.
 
    The two values must be integers.'''
    x = int(x) # convert to integers, if possible
    y = int(y)
 
    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')
 
printMax2(3, 5)
print(printMax2.__doc__)