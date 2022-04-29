from  selenium import  webdriver
from  time  import  sleep
from  selenium.webdriver.common.by import  By
driver=webdriver.Chrome()
#进入qq网址
driver.get('https://mail.qq.com//')
#进入qq邮箱网址
# driver.find_element_by_id('kw').send_keys('qq邮箱')
# driver.find_element_by_id('su').click()
driver.maximize_window()
sleep(3)
#获取外面的框架
driver.switch_to_frame('login_frame')
#获取里面的框架
driver.find_element_by_id('switcher_plogin').click()
sleep(5)
#登陆用户
driver.find_element_by_id('u').send_keys('2186376644') #这里注意的点是查找的参数点是input里面的id值
driver.find_element_by_id('p').send_keys('lxy19991229')#这里也是参数值是input里面的id值
driver.find_element_by_id('login_button').click() #这里获取的是登陆按钮
sleep(4)
#循环次数
#进入写信页面
driver.find_element(By.XPATH,'//*[@id="composebtn"]').click()
sleep(2)
#进入写信的主框架
driver.switch_to_frame('mainFrame')
sleep(2)
i=0
while True:
    #进入收件人输入框
    driver.find_element_by_xpath('//*[@id="toAreaCtrl"]/div[2]/input').send_keys('2571382543@qq.com')
    sleep(2)
    #主题
    driver.find_element_by_xpath('//*[@id="subject"]').send_keys('华萍小姐姐')
    sleep(2)
    #添加附件
    driver.find_element_by_xpath('//*[@id="AttachFrame"]/span/input').send_keys('C:\华为mate40.jpg')
    #添加文件
    # driver.find_element_by_xpath('//*[@id="bigAttachLink"]').click()
    # sleep(2)
    #进入框架
    # driver.switch_to_frame('ftnupload_attach_QMDialog__dlgiframe_')
    #上传新文件按钮,只要不是input属性文件的需要
    # driver.find_element_by_xpath('//input[@name="UploadFile"]').click()
    #输入文件路径和名字
    # driver.find_element_by_xpath('//input[@name="UploadFile"]').send_keys('C:\课程资料\新建文本文档.txt')
    #动态获取id框架
    driver.switch_to_frame(driver.find_element_by_xpath('//iframe[@class="qmEditorIfrmEditArea"]'))#动态获取id
    sleep(2)
    #输入正文
    driver.find_element_by_xpath('/html/body').send_keys('小可爱，我来啦')
    sleep(2)
    #再次返回上一级框架
    # driver.switch_to_frame('mainFrame')  #返回上一级框架
    driver.switch_to.parent_frame()    #返回上一级框架
    #点击发送按钮
    driver.find_element_by_xpath('//*[@id="toolbar"]/div/a[1]').click()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="btnagainl"]').click()
    i+=1
    if i==5:
        break
#跳回最外层的页面
driver.switch_to_default_content()
#跳回上一层的页面
# driver.switch_to.parent_frame()
# driver.switch_to_frame('mainFrame')    #里面写的是获取的iframe的对应的结果