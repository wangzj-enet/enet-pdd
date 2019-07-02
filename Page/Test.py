# -*- coding: utf-8 -*-
'''
测试
'''
import pickle
import time

from selenium import webdriver

from Config.Information import Information
from Config.Session import Session
from Page.BindWechatPage import BindWechatPage
from Page.LoginPage import LoginPage
import operator as op



driver = webdriver.Firefox()
# login_page = LoginPage(driver)
# login_page.login(Information.username, Information.password, '0000')
# print('%s[%s]' %(driver.title,driver.current_url))

# bindWechatPage = BindWechatPage(driver)
# cookies = Session.getCookiesFromFile()
# print(type(cookies))
# print(len(cookies))
print(driver.get_cookies())
login_page = LoginPage(driver)
login_page.login(Information.username, Information.password, '0000')
time.sleep(3)
Session.setCookiesToFile(driver.get_cookies())
driver.delete_all_cookies()
for cookie_dict in Session.getCookiesFromFile():
    if(not op.eq(cookie_dict['domain'],'.pinduoduo.com')):
        driver.add_cookie(cookie_dict)

bindWechatPage = BindWechatPage(driver)














