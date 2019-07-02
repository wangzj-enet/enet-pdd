# -*- coding: utf-8 -*-
'''
后台首页面-情景模拟广告弹出框
'''
import time

from Config.Information import Information


class MHomeActivityModalPage(object):
    def __init__(self,driver):
        self.driver = driver
        print('*'*32)


    def clickClose(self):
        ele = self.driver.find_element_by_xpath(Information.m_homePage_ActivityModal_close)
        ele.click()
        time.sleep(2)