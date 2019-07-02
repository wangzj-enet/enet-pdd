# -*- coding: utf-8 -*-
'''
扫描微信页面
'''
import time

from Config.Information import Information
from Config.Session import Session
from Page.BasePage import BasePage


class BindWechatPage(BasePage):
    def __init__(self, driver):
        super(BindWechatPage, self).__init__(driver)
        driver.get(Information.login_url)
        for cookie in Session.getCookiesFileter(Information.filterDict):
            driver.add_cookie(cookie)
        driver.get(Information.bindWechat_url)
        BasePage.printSymbol(self)
        time.sleep(2)
        driver.save_screenshot(Information.bindWechat_img_path)
        time.sleep(2)

    def run(self):
        print('*'*32)

    def clickBindWechat(self):
        #self.driver.find_element_by_xpath('//button[@class="mui-button goindex"]').click()
        self.click(self.findEelement('//span[text()="完成绑定，前往后台"]'))
        time.sleep(3)

