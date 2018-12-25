# -*- coding:utf-8 -*-
print('登陆吧！')
def login(id,psw):
    if id=="seven" and psw=="123456":
        print('登陆成功！')
    else:
        print('登录失败！')
id=input('请输入用户名：')
psw=input('请输入密码：')
print(login(id,psw))