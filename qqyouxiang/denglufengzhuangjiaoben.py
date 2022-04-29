from selenium import webdriver
from time import  sleep
from test_auto.passwd import  kkk
a=kkk()
class Login(object):
    def aaa (self):
        self.driver=webdriver.Chrome()
        self.driver.get('https://mail.qq.com//')
        self.driver.maximize_window()
        sleep(2)
    # def __init__(self,driver):
    #     # self.driver=driver
    def login(self):
        self.aaa()
        #账号密码参数化
        self.driver.switch_to.frame('login_frame')
        #点击账号密码
        self.driver.find_element_by_id('switcher_plogin').click()
        self.driver.find_element_by_xpath('//*[@id="u"]').send_keys(a.fff())
        self.driver.find_element_by_xpath('//*[@id="p"]').send_keys(a.ttt())
        #点击登陆按钮
        self.driver.find_element_by_xpath('//*[@id="login_button"]').click()

d=Login()
d.login()