# -*- coding: utf-8 -*-
'''
MAddGoodPage
2019-07-01 14:28 
PyCharm
页面
'''
import time

from Config.Information import Information
from Config.Session import Session
from Page.BasePage import BasePage


class MAddGoodPage(BasePage):
    def __init__(self, driver):
        super(MAddGoodPage, self).__init__(driver)
        # driver.get(Information.m_homePage_url)
        # for cookie in Session.getCookiesFileter(Information.filterDict):
        #     driver.add_cookie(cookie)
        #driver.get(Information.m_goodsCategory_url)
        BasePage.printSymbol(self)
        time.sleep(2)

    def run(self):
        BasePage.printSymbol(self)

    def oneLevelGoodBasic(self):
        BasePage.printSymbol(self)

    def oneLevelGoodBasicCategory(self):
        BasePage.printSymbol(self)

    def oneLevelGoodBasicTitle(self):
        BasePage.printSymbol(self)

    def oneLevelGoodBasicProperty(self):
        BasePage.printSymbol(self)

    def oneLevelGoodBasicGallery(self):
        BasePage.printSymbol(self)

    def twoLevelGoodSpecSku(self):
        BasePage.printSymbol(self)

    def twoLevelGoodSpecSkuSpec(self):
        BasePage.printSymbol(self)

    def twoLevelGoodSpecSkuSku(self):
        BasePage.printSymbol(self)

    def twoLevelGoodSpecSkuSkuMask(self):
        BasePage.printSymbol(self)

    def threeLevelGoodService(self):
        BasePage.printSymbol(self)

    def threeLevelGoodServiceCostTemplate(self):
        BasePage.printSymbol(self)

    def threeLevelGoodServicePromise(self):
        BasePage.printSymbol(self)

    def clickButton(self):
        BasePage.printSymbol(self)

    def clickGrayButton(self):
        BasePage.printSymbol(self)











