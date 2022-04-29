from  selenium import  webdriver
from  time import  sleep
from  selenium.webdriver.common.by import  By
#使用谷歌浏览器
driver=webdriver.Chrome()
#进入QQ邮箱网址
driver.get('https://mail.qq.com//')
#使屏幕最大化
driver.maximize_window()
#获取外面的框架
driver.switch_to_frame('login_frame')
#
