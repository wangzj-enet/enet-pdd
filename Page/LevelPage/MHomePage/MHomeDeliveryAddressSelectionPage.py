# -*- coding: utf-8 -*-
'''
后台首页面-选取发货地址
'''
import time

from Config.Information import Information


class MHomeDeliveryAddressSelectionPage(object):
    def __init__(self,driver):
        self.driver = driver
        print('*'*32)

    def clickRadio(self):
        ele = self.driver.find_element_by_xpath(Information.m_homePage_DeliveryAddressSelection_radio)
        ele.click()
        time.sleep(2)

    def chooseSelect(self):
        print('')
        ele = self.driver.find_element_by_xpath(Information.m_homePage_DeliveryAddressSelection_select)
        ele.click()
        time.sleep(1)
        ele = self.driver.find_element_by_xpath(Information.m_homePage_DeliveryAddressSelection_province)
        ele.click()
        time.sleep(1)
        ele = self.driver.find_element_by_xpath(Information.m_homePage_DeliveryAddressSelection_city)
        ele.click()
        time.sleep(1)
        ele = self.driver.find_element_by_xpath(Information.m_homePage_DeliveryAddressSelection_area)
        ele.click()
        time.sleep(1)

    def clickButton(self):
        ele = self.driver.find_element_by_xpath(Information.m_homePage_DeliveryAddressSelection_button)
        ele.click()
        time.sleep(2)