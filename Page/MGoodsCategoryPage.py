# -*- coding: utf-8 -*-
'''
添加商品页面
'''
import time

from Config.Information import Information
from Config.Session import Session
from Page.BasePage import BasePage
from Page.LevelPage.MGoodsCategory.MGoodsCategoryNoticePage import MGoodsCategoryNoticePage


class MGoodsCategoryPage(BasePage):
    def __init__(self,driver):
        super(MGoodsCategoryPage, self).__init__(driver)
        driver.get(Information.m_homePage_url)
        for cookie in Session.getCookiesFileter(Information.filterDict):
            driver.add_cookie(cookie)
        driver.get(Information.m_goodsCategory_url)
        BasePage.printSymbol(self)
        time.sleep(2)
        #driver.save_screenshot(Information.mHomePage_img_path)
    def run(self):
        print('')
        self.chooseOneLevel()
        self.chooseTwoLevel()
        self.chooseThreeLevel()
        self.validChoose()
        self.clickButton()

    def runShade(self):
        self.runNotice()

    def runNotice(self):
        #先判断自身的存在性,元素是否可以找到
        if(self.isElementExits(Information.m_goodsCategory_notice_title)):
            mGoodsCategoryNoticePage = MGoodsCategoryNoticePage(self.driver)
            mGoodsCategoryNoticePage.clickButton()

    def chooseOneLevel(self):
        ele = self.findEelement('//div[text()="家居生活"]')
        # 判断是否包含active属性
        # 如果包含，下一步
        # 如果不包含，点击
        if ele.get_attribute("class").find("active") > -1:
            print('')
        else:
            ele.click()
            time.sleep(1)

        # 判断是否被点击，如果没有被点击，点击，如果已经被点击，下一步
        ele1_1 = self.findEelement('//div[text()="宠物/宠物食品及用品"]')
        time.sleep(1)
        ele1_1.click()
        time.sleep(1)

    def chooseTwoLevel(self):
        # ele2 = driver.find_element_by_xpath('//div[text()="猫/狗日用品"]')
        time.sleep(2)
        # print('*'*32)
        # print(self.driver.page_source)
        # print('*' * 32)
        ele2 = self.findEelement('// *[ @ id = "selectedCate16399"] / a ')
        # ele2 = self.findEelement('// *[ @ id = "selectedCate16399"] / a / div[1]')

        #ele2 = self.findEelement('//li[@id="selectedCate16399"')

        ele2.click()
        time.sleep(1)

    def chooseThreeLevel(self):
        ele3 = self.findEelement('//div[text()="背包/箱包"]')
        ele3.click()
        time.sleep(1)

    def validChoose(self):
        show = self.findEelement('//div[@class="new-category-show"]')
        print(show)

    def clickButton(self):
        self.click(self.findEelement('//button/span[text()="我已阅读以下须知，确认创建该类商品"]'))
        time.sleep(1)




