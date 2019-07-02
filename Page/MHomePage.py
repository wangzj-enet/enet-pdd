# -*- coding: utf-8 -*-
'''
后台管理主页页面
'''
import time

from Config.Information import Information
from Config.Session import Session
from Page.BasePage import BasePage
from Page.LevelPage.MHomePage.MHomeActivityModalPage import MHomeActivityModalPage
from Page.LevelPage.MHomePage.MHomeDeliveryAddressSelectionPage import MHomeDeliveryAddressSelectionPage
from Page.LevelPage.MHomePage.MHomeNewMsgsPage import MHomeNewMsgsPage
from Page.LevelPage.MHomePage.MHomeNoticeCheckinPage import MHomeNoticeCheckinPage


class MHomePage(BasePage):
    def __init__(self,driver):
        super(MHomePage, self).__init__(driver)
        driver.get(Information.login_url)
        for cookie in Session.getCookiesFileter(Information.filterDict):
            driver.add_cookie(cookie)
        driver.get(Information.m_homePage_url)
        BasePage.printSymbol(self)
        time.sleep(2)
        driver.save_screenshot(Information.mHomePage_img_path)
        time.sleep(2)
    def runDeliveryAddressSelection(self):
        #先判断自身的存在性,元素是否可以找到
        if(self.isElementExits(Information.m_homePage_DeliveryAddressSelection_title)):
            mHomeDeliveryAddressSelectionPage = MHomeDeliveryAddressSelectionPage(self.driver)
            mHomeDeliveryAddressSelectionPage.clickRadio()
            mHomeDeliveryAddressSelectionPage.chooseSelect()
            mHomeDeliveryAddressSelectionPage.clickButton()
        #处理自身的业务逻辑

    def runNoticeCheckin(self):
        #先判断自身的存在性,元素是否可以找到
        if(self.isElementExits(Information.m_homePage_NoticeCheckin_title)):
            mHomeNoticeCheckinPage = MHomeNoticeCheckinPage(self.driver)
            mHomeNoticeCheckinPage.clickButton()


    def runActivityModal(self):
        #先判断自身的存在性,元素是否可以找到
        if(self.isElementExits(Information.m_homePage_ActivityModal_title)):
            mHomeActivityModalPage = MHomeActivityModalPage(self.driver)
            mHomeActivityModalPage.clickClose()

    def runNewMsgs(self):
        #先判断自身的存在性,元素是否可以找到
        if(self.isElementExits(Information.m_homePage_NewMsgs_title)):
            mHomeNewMsgsPage = MHomeNewMsgsPage(self.driver)
            mHomeNewMsgsPage.clickClose()
            #mHomeNewMsgsPage.clickGoto()

    def runShade(self):
        self.runDeliveryAddressSelection()
        self.runNoticeCheckin()
        self.runActivityModal()
        self.runNewMsgs()


