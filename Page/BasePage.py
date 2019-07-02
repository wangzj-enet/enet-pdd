# -*- coding: utf-8 -*-
'''
作为页面类的基类，封装了其他的方法，其他页面必须为该类的子类
'''
import pickle

from selenium import webdriver

from Config.Information import Information


class BasePage(object):
    def __init__(self,driver):
        self.driver = driver
        print('BasePage dirver __init__')

    def setDriver(self,driver):
        self.driver = driver

    def printSymbol(self):
        print('%s[%s]' % (self.driver.title, self.driver.current_url))

    def findEelement(self,findstr):

        element = self.driver.find_element_by_xpath(findstr)
        return element

    def click(self,element):
        element.click()

    def sendKeys(self,findstr,text):
        element = self.driver.find_element_by_xpath(findstr)
        element.clear()
        element.send_keys(text)

    def isElementExits2(self,findstr):
        try:
            element = self.driver.find_element_by_xpath(findstr)
            if len(element) == 0:
                return False
            elif len(element) == 1:
                return True

            else:
                print('%s====%s' %(findstr,len(element)))
                return  False
        except:
            return False

    def isElementExits(self,findstr):
        try:
            element = self.driver.find_element_by_xpath(findstr)
            if len(element.id) > 0:
                return True
            elif len(element.id) == 0:
                return False

            else:
                print('%s====%s' %(findstr,element.id))
                return  False
        except:
            return False



    



