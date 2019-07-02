# -*- coding: utf-8 -*-
'''
主要用来存放一些配置信息
'''


class Information:

    # 登录页面
    login_url = 'https://mms.pinduoduo.com'
    username = '15514553803'
    password = 'Wangzhijia1012'
    cookiesFile = "cookies.json"
    login_img_path = 'img/LoginPage_img.png'


    #微信扫描页面
    bindWechat_url = 'https://mms.pinduoduo.com/mallcenter/bindWechat'
    bindWechat_img_path = 'img/bindWechat_img.png'
    bindWechat_button = ''

    filterDict = {'domain': '.pinduoduo.com'}
    filterDictNone = {}

    #后台管理主页面
    m_homePage_url= 'https://mms.pinduoduo.com/home/'
    mHomePage_img_path = 'img/m_homePage_img.png'


    m_homePage_DeliveryAddressSelection_title = '//span[text()="请选择您的主要发货地"]'
    m_homePage_DeliveryAddressSelection_radio = '//span[text()="大陆地区商家"]'
    m_homePage_DeliveryAddressSelection_select='//input[@class="ant-input ant-cascader-input "]'
    m_homePage_DeliveryAddressSelection_province = '//li[@title="河南省"]'
    m_homePage_DeliveryAddressSelection_city = '//li[@title="郑州市"]'
    m_homePage_DeliveryAddressSelection_area=  '//li[@title="新郑市"]'
    m_homePage_DeliveryAddressSelection_button = '//span[text()="确认"]'

    m_homePage_NoticeCheckin_title = '//h3[text()="市场主体登记信息公示通知"]'
    m_homePage_NoticeCheckin_button = '//a[text()="我不用上传"]'

    m_homePage_ActivityModal_title = '//div[@class="pdd-modal-body"]'
    m_homePage_ActivityModal_close = '//div[@class="activity-hide"]'

    m_homePage_NewMsgs_title = '//div[@class="message-box-NewMsgBox-ImportantList--msgbox-3hcji"]'
    m_homePage_NewMsgs_close = '//i[contains(@class, "message-box-NewMsgBox-ImportantList--close-29h7A")]'
    m_homePage_NewMsgs_goto = '//a[@id="goto"]'

    #后台管理-添加新商品页面
    m_goodsCategory_url= 'https://mms.pinduoduo.com/goods/category'
    m_goodsCategory_notice_title = '//div[@class="mui-modal-content"]'
    m_goodsCategory_notice_button = '//button[@data-e2e-action="close-1"]'




    #手机端登录拼多多
    mobile_index_url = 'http://mobile.yangkeduo.com/index.html'
    mobile_login_url = 'http://mobile.yangkeduo.com/login.html'
    mobile_good_id_ = 'http://mobile.yangkeduo.com/goods.html?goods_id='
    mobile_username = '13311503035'

    #cookies
    cookies_db_name = 'cookies'
    cookies_db_pc = ''
    cookies_db_mobile = 'mobile_cookies'

    cookie_mobile_filterDict = {'domain': '.yangkeduo.com'}



if __name__ == '__main__':
    print('*'*32)
