# -*- coding: utf-8 -*-
'''
后台首页面-入住通知
'''
import time

from Config.Information import Information


class MHomeNoticeCheckinPage(object):
    def __init__(self,driver):
        self.driver = driver
        print('*'*32)


    def clickButton(self):
        ele = self.driver.find_element_by_xpath(Information.m_homePage_NoticeCheckin_button)
        ele.click()
        time.sleep(2)