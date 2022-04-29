from  selenium import  webdriver
import  unittest
import  time
from  selenium.webdriver.common.by import  By
class Test(unittest.TestCase):
    #访问网址,初始化参数
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get('http://localhost:8080/EasyBuy/Home?action=index')
        self.driver.maximize_window()
        time.sleep(2)
    #执行用例
    def test_login(self):
        #点击登陆按钮
        self.driver.find_element_by_xpath('/html/body/div[1]/div/span[2]/span/a[1]').click()
        time.sleep(2)
        #输入账号
        self.driver.find_element_by_id('loginName').send_keys('admin')
        #输入密码
        self.driver.find_element_by_name('password').send_keys('123456')
        time.sleep(2)
        #点击登陆按钮
        self.driver.find_element_by_class_name('log_btn').click()
    @unittest.skip('不执行此用例')
    def test_search(self):
        self.driver.find_element_by_xpath('/html/body/div[4]/div[2]/form/input[1]').send_keys('香水')
    def tearDown(self):
        time.sleep(5)
        self.driver.quit()


