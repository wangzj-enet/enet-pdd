# -*- coding: utf-8 -*-
'''
后台首页面-新消息通知
'''
import time

from Config.Information import Information


class MHomeNewMsgsPage(object):
    def __init__(self,driver):
        self.driver = driver
        print('*'*32)


    def clickGoto(self):
        ele = self.driver.find_element_by_xpath(Information.m_homePage_NewMsgs_goto)
        ele.click()
        time.sleep(2)

    def clickClose(self):
        ele = self.driver.find_element_by_xpath(Information.m_homePage_NewMsgs_close)
        ele.click()
        time.sleep(2)