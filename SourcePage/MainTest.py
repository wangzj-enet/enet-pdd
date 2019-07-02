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
from SourcePage.MobileGoodPage import MobileGoodPage

driver = webdriver.Firefox()
driver.maximize_window()

mobileGoodPage = MobileGoodPage(driver,'5218019897')






























