from  selenium import  webdriver
from  time import  sleep
#定义账号密码
class Login():
    def __init__(self,driver):
        self.driver=driver
    def login(self,username,psw):
        #参数化账号密码
        self.driver.find_element_by_xpath('//*[@id="u"]').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="p"]').send_keys(psw)
        #点击登陆按钮
        self.driver.find_element_by_xpath('//*[@id="login_button"]').click()
        sleep(3)
class QQemail():
    def setup(self):
        self.driver=webdriver.Chrome()
        self.driver.get('https://mail.qq.com/')
    def test_sendmail(self):
        self.driver.switch_to.frame('login_frame')
        self.driver.implicitly_wait(30)
        #点击注册账号密码登陆按钮
        self.driver.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
        self.driver.implicitly_wait(30)
        #调用登陆的办法实现登陆
        Login(self.driver).login('345678888889','lxy19991229')
#实例化就可以直接输出
a=QQemail()
a.setup()
a.test_sendmail()


