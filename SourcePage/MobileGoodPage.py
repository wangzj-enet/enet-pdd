# -*- coding: utf-8 -*-
'''
MobileGood
2019-07-01 16:33 
PyCharm
页面
'''
import time

from Config.Information import Information
from Config.Session import Session
from Page.BasePage import BasePage


class MobileGoodPage(BasePage):
    def __init__(self, driver,good_id):
        super(MobileGoodPage, self).__init__(driver)
        driver.get(Information.mobile_index_url)
        for cookie in Session.getCookiesFromShelveFileter(Information.cookie_mobile_filterDict):
            driver.add_cookie(cookie)
        driver.get(Information.mobile_good_id_+ good_id)
        BasePage.printSymbol(self)
        time.sleep(2)

    def run(self):
        BasePage.printSymbol(self)