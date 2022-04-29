from selenium import webdriver
import time
#定义账号密码
class Login():
    def __init__(self,driver):
        self.driver=driver
    def login(self,username,psw):
        #账号密码参数化
        self.driver.find_element_by_xpath('//*[@id="u"]').send_keys(username)
        self.driver.find_element_by_xpath('//*[@id="p"]').send_keys(psw)
        #点击登录按钮
        self.driver.find_element_by_xpath('//*[@id="login_button"]').click()
        time.sleep(3)
class QQemail():
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get('https://mail.qq.com/')
    def test_sendmail(self):
        self.driver.switch_to.frame("login_frame")
        self.driver.implicitly_wait(30)
        #点击账号密码登录按钮
        self.driver.find_element_by_xpath('//*[@id="switcher_plogin"]').click()
        self.driver.implicitly_wait(30)
        #调用登录方法实现登录
        Login(self.driver).login("2186376644","234568798")
        time.sleep(3)
#添加一个主方法
if __name__ == '__main__':
    go=QQemail()
    go.setUp()
    go.test_sendmail()