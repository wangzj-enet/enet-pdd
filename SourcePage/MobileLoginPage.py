# -*- coding: utf-8 -*-
'''
登录页面
'''
import time

from selenium import webdriver

from Config.Information import Information
from Config.Session import Session
from Page.BasePage import BasePage


class MobileLoginPage(BasePage):
    def __init__(self,driver):
        super(MobileLoginPage, self).__init__(driver)
        driver.get(Information.mobile_login_url)
        BasePage.printSymbol(self)
        time.sleep(2)

    def switchManualLogin(self):
        self.click(self.findEelement('//span[text()="手机登录"]'))
        time.sleep(2)

    def setLoginInfos(self,username,verticode):
        self.sendKeys('//input[@id="user-mobile"]',username)
        self.getVerticode()
        self.sendKeys('//input[@id="input-code"]', verticode)

    def getVerticode(self):
        self.click(self.findEelement('//button[@id="code-button"]'))
        time.sleep(2)

    def clickButton(self):
        self.click(self.findEelement('//button[@id="submit-button"]'))

    def login(self,username,verticode):
        self.switchManualLogin()
        self.setLoginInfos(username,verticode)
        self.clickButton()
        print('*'*32)

    def run(self):
        self.login(Information.mobile_username, '0000')
        time.sleep(3)
        Session.setCookiesToShelve(self.driver.get_cookies())





if __name__=='__main__':
    driver = webdriver.Firefox()
    mobileLoginPage = MobileLoginPage(driver)
    mobileLoginPage.run()







