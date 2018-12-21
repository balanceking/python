# -*- coding:utf-8 -*-

# 进制转换
print('进制转换：')
a = 0o101
print("a="+str(a))
b=64
print('b='+str(b))
c=-237
print('c='+str(c))
d=0x92
print('d='+str(d))
e=-0x92
print('e='+str(e))

longint = 9999 ** 8
print("longint="+str(longint))

# boo1基本测试
print('bool测试：')
print(bool(1))
print(bool(True))
print(bool('0'))
print(bool([]))
print(bool((1,)))
 
# 使用bool数
foo = 42
bar = foo<42
print('使用bool数：')
print(bar)
print(bar+10)
print('%s' %bar)
print('%d' %bar)

# 无_nozero_()
class C:pass
c=C()
print('nozero：')
print('无_nozero_():'+str(bool(c)))

# 双精度浮点
print('双精度浮点：')
print(0.0)
print(-777.)
print(-5.123456789)
print(96e3 * 1.0)
print(-1.609E-19)

#复数
print('复数：')
print(complex(2,4))
print(1.23e-045+6.7e+089j)

# 十进制浮点
from decimal import *
 
print("十进制浮点....")
dec=Decimal('.1')
print(dec)
print(Decimal(.1))
print(dec +Decimal(.1))

#转换工厂
print("转换工厂....")
print(int(4.2222222))
print(float(4))
print(complex(4))

#进制转换
print("进制转换....")
print(hex(255))
print(oct(255))
print(oct(0x111))

#ASCII转换
print("进制转换....")
print(chr(76))
print(ord('L'))