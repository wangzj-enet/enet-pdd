# -*- coding: utf-8 -*-
'''
登录页面
'''
import time

from selenium import webdriver

from Config.Information import Information
from Config.Session import Session
from Page.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self,driver):
        super(LoginPage, self).__init__(driver)
        driver.get(Information.login_url)
        BasePage.printSymbol(self)
        time.sleep(2)
        driver.save_screenshot(Information.login_img_path)

    def switchManualLogin(self):
        self.click(self.findEelement('//div[text()="账户登录"]'))
        time.sleep(2)

    def setLoginInfos(self,username,password,verticode):
        self.sendKeys('//input[@id="usernameId"]',username)
        self.sendKeys('//input[@id="passwordId"]', password)
        self.sendKeys('//input[@placeholder="请输入右侧验证码"]', verticode)

    def clickButton(self):
        self.click(self.findEelement('//span[text()="登录"]'))

    def login(self,username,password,verticode):
        self.switchManualLogin()
        self.setLoginInfos(username,password,verticode)
        self.clickButton()
        print('*'*32)

    def run(self):
        self.login(Information.username, Information.password, '0000')
        time.sleep(3)
        Session.setCookiesToFile(self.driver.get_cookies())





if __name__=='__main__':
    driver = webdriver.Firefox()
    login_page = LoginPage(driver)
    login_page.login(1,2,3)







