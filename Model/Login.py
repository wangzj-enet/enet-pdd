#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
记录login（登录）界面的元素，调用的时候采用Login.username表示Login页面的用户名
'''

class login:
    username = ('id', 'username11')
    password = ('id', 'password11')
    captcha = ('id', 'captcha')
    submit_button = ('xpath', '//*[@id="loginForm"]/div[5]/div/button')

