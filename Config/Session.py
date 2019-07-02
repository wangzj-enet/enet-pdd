# -*- coding: utf-8 -*-
'''
Session工具
'''
import pickle
import operator as op
from Config.Information import Information
import dbm
import shelve

class Session(object):
    def __init__(self):
        print('Session......')

    def setCookiesToFile(cookies):
        print(cookies)
        cookiesFile = Information.cookiesFile
        with open(cookiesFile, 'wb') as f:
            pickle.dump(cookies, f)
            print('*' * 32)

    def getCookiesFromFile():
        cookiesFile = Information.cookiesFile
        with open(cookiesFile, 'rb') as f:
            cookies = pickle.load(f)
            print(cookies)
            print('*' * 32)
            return cookies

    def setCookiesToShelve(cookies):
        print(cookies)
        cookie_db = shelve.open(Information.cookies_db_name)
        cookie_db[Information.cookies_db_mobile] = cookies
        cookie_db.close()

    def getCookiesFromShelve():
        cookie_db = shelve.open(Information.cookies_db_name)
        cookies = cookie_db[Information.cookies_db_mobile]
        cookie_db.close()
        print(cookies)
        return  cookies



    def getCookiesFileter(filterDict):
        if len(filterDict) == 0:
            return Session.getCookiesFromFile()

        temp_cookie_dict = []
        for cookie_dict in Session.getCookiesFromFile():
            flag = True
            for filterkey in filterDict.keys():
                if filterkey in cookie_dict:
                    if(op.eq(cookie_dict[filterkey],filterDict[filterkey])):
                        flag = False
                        break
            if(flag):
                temp_cookie_dict.append(cookie_dict)

        return temp_cookie_dict

    def getCookiesFromShelveFileter(filterDict):
        cookie_db = shelve.open(Information.cookies_db_name)
        cookies = cookie_db[Information.cookies_db_mobile]
        cookie_db.close()

        if len(filterDict) == 0:
            return cookies

        print(cookies)
        temp_cookie_dict = []
        for cookie_dict in cookies:
            flag = True
            for filterkey in filterDict.keys():
                if filterkey in cookie_dict:
                    if(op.eq(cookie_dict[filterkey],filterDict[filterkey])):
                        flag = False
                        break
            if(flag):
                temp_cookie_dict.append(cookie_dict)

        return temp_cookie_dict










