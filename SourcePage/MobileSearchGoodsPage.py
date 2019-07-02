# -*- coding: utf-8 -*-
'''
MobileSearchGoods
2019-07-01 16:02 
PyCharm
页面
'''
import time

from Config.Information import Information
from Config.Session import Session
from Page.BasePage import BasePage
import operator as op
from selenium import webdriver


class MobileSearchGoodsPage(BasePage):
    def __init__(self, driver):
        super(MobileSearchGoodsPage, self).__init__(driver)
        driver.get(Information.mobile_index_url)
        for cookie in Session.getCookiesFromShelveFileter(Information.cookie_mobile_filterDict):
            driver.add_cookie(cookie)
        driver.get(Information.mobile_index_url)
        BasePage.printSymbol(self)
        time.sleep(2)

    def run(self):
        BasePage.printSymbol(self)

    def search(self,name):
        if(not op.eq(Information.mobile_index_url,self.driver.current_url)):
            self.driver.get(Information.mobile_index_url)

        search_div = self.driver.find_element_by_xpath('//div[@class = "footer-items"]/div[3]')
        search_div.click()

        search_input = self.driver.find_element_by_xpath('//div[@class = "Rj3w8_4n"]')
        search_input.click()
        search_input.send_keys(name)

        search_button = self.driver.find_element_by_xpath('//div[@class = "_1fALnEid"]')
        search_button.click()
        time.sleep(2)
        BasePage.printSymbol(self)

if __name__ == '__main__':
    driver = webdriver.Firefox()
    driver.maximize_window()
    mobileSearchGoods = MobileSearchGoodsPage(driver)
    mobileSearchGoods.search('猫包宠物包外出猫狗便携宠物包全景透明太空包透气便携猫包猫咪包')
