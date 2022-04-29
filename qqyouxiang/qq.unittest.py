from  selenium import  webdriver
from  time import  sleep
import  unittest
class Login(unittest.TestCase):
    def setUp(self):
        self.driver=webdriver.Chrome()
        self.driver.get('https://mail.qq.com//')
        self.driver.maximize_window()
        sleep(3)
    def test_login(self):
        #获取账号密码登陆主框架
        self.driver.switch_to.frame('login_frame')
        #点击获取账号密码的按钮
        self.driver.find_element_by_id('switcher_plogin').click()
        #输入账号
        self.driver.find_element_by_xpath('//*[@id="u"]').send_keys('2186376644')
        #输入密码
        self.driver.find_element_by_xpath('//*[@id="p"]').send_keys('lxy19991229')
        self.driver.find_element_by_xpath('//*[@id="login_button"]').click()
        sleep(2)
    # @unittest.skip('不执行这个条例')#单元测试装饰器，当启用时候不执行该用例，可以方便找bug
    def test_aaa(self):
        #点击账号密码登陆按钮主框架
        self.driver.switch_to.frame('login_frame')
        #点击获取账号密码的按钮
        self.driver.find_element_by_id('switcher_plogin').click()
        #输入账号
        self.driver.find_element_by_xpath('//*[@id="u"]').send_keys('2186376644')
        #输入密码
        self.driver.find_element_by_xpath('//*[@id="p"]').send_keys('lxy19991229')
        self.driver.find_element_by_xpath('//*[@id="login_button"]').click()
        sleep(2)
        #点击写信按钮
        self.driver.find_element_by_xpath('//*[@id="composebtn"]').click()
        sleep(2)
        #进入到写信主框架
        self.driver.switch_to.frame('mainFrame')
        #进入收件人输入框
        self.driver.find_element_by_xpath('//*[@id="toAreaCtrl"]/div[2]/input').send_keys('2571382543@qq.com')
        #进入主题输入框
        self.driver.find_element_by_xpath('//*[@id="subject"]').send_keys('华萍小姐姐')
        #进入正文页面框架
        self.driver.switch_to.frame(self.driver.find_element_by_xpath('//iframe[@class="qmEditorIfrmEditArea"]'))
        #进入正文编辑框
        self.driver.find_element_by_xpath('/html/body').send_keys('小可爱，我来啦')
        sleep(3)
        #返回上一层框架输入正文的框架
        self.driver.switch_to.parent_frame()
        #点击发送按钮
        self.driver.find_element_by_xpath('//*[@id="toolbar"]/div/a[1]').click()
        #返回最外层
        self.driver.switch_to_default_content()
    def tearDown(self):
        sleep(5)
        self.driver.quit()
    #添加主方法，可以不用加，不改变运行结果
    # if __name__ == '__main__':
    #     unittest.main()
#三大框架：1-setup()  2-def test_jik() 用例，这里必须是test开头才能运行，3-teardown()关闭资源










