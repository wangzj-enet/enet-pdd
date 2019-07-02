# -*- coding: utf-8 -*-
'''
测试
'''
import time

import pickle
from selenium import webdriver

from Config.Information import Information
from Config.Session import Session
from Page.BindWechatPage import BindWechatPage
from Page.LoginPage import LoginPage
import operator as op

from Page.MGoodsCategoryPage import MGoodsCategoryPage
from Page.MHomePage import MHomePage

#driver = webdriver.Firefox()
driver = webdriver.Chrome()
driver.maximize_window()
# login_page = LoginPage(driver)
# login_page.login(Information.username, Information.password, '0000')
# print('%s[%s]' %(driver.title,driver.current_url))

# bindWechatPage = BindWechatPage(driver)
# cookies = Session.getCookiesFromFile()
# print(type(cookies))
# print(len(cookies))
# print(driver.get_cookies())
# login_page = LoginPage(driver)
# login_page.run()
# driver.delete_all_cookies()

# bindWechatPage = BindWechatPage(driver)
# bindWechatPage.clickBindWechat()

# mHomePage = MHomePage(driver)
# mHomePage.runShade()
# mHomePage.printSymbol()
# mHomePage.runDeliveryAddressSelection()
# mHomePage.runNoticeCheckin()
# mHomePage.runActivityModal()
# mHomePage.runNewMsgs()
# 2145916555
# 2425342303
# 1562292721

mgoodsCategoryPage = MGoodsCategoryPage(driver)
mgoodsCategoryPage.runShade()
mgoodsCategoryPage.run()




























