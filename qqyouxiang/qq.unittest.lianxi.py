from  selenium import  webdriver
import  unittest
from  time import  sleep
class Login(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get('https://mail.qq.com')
        self.driver.maximize_window()
        sleep(3)
    def test_login(self):
        #点击获取登陆密码主框架
        self.driver.switch_to.frame('login_frame')
        #点击获取登陆密码按钮
        self.driver.find_element_by_id('switcher_plogin').click()
        #输入账号
        self.driver.find_element_by_id('u').send_keys('2186376644@qq.com')
        #输入密码
        self.driver.find_element_by_id('p').send_keys('lxy19991229')
        #点击登陆按钮
        self.driver.find_element_by_xpath('//*[@id="login_button"]').click()
        sleep(2)
if __name__ == '__main__':
    Login()
#导入ActionChains类封装起来用,鼠标操作



