# -*- coding: utf-8 -*-
'''
后台发布新商品-通知
'''
import time

from Config.Information import Information


class MGoodsCategoryNoticePage(object):
    def __init__(self,driver):
        self.driver = driver
        print('*'*32)


    def clickButton(self):
        ele = self.driver.find_element_by_xpath(Information.m_goodsCategory_notice_button)
        ele.click()
        time.sleep(2)