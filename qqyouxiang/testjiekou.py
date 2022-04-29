import  requests
import  unittest
#导入打印自动化测试报告方法
import  HTMLTestRunnerCN
#构建一个类，固定格式
class inter01(unittest.TestCase):
    #实时易买网接口登陆
    def test(self):
        url="http://localhost:8080/EasyBuy/Login"
        data='loginName=admin&password=123456&action=login'
        response=requests.request('POST',url,params=data)
        print(response.json())
#接口自动化单元测试里面不需要加 setup()初始函数和teardown() 关闭资源函数，
#也是需要与unittest结合使用，打印报告的操作与ui自动化测试一样，
#接口自动化测试与ui自动化测试的区别在于：
# ui自动化测试需要写在不同的脚本里面去读取需要写的用例所在的路径，
#而接口自动化测试可以在当前页面脚本进行读取打印报告，也可以在不同的包里面读取打印
Testcase_dir='C:\\课程资料\\code\\untitled\\qqyouxiang'
#覆盖该文件路径下的文件,这是文件的名字
dis=unittest.defaultTestLoader.discover(Testcase_dir,'testjiekou.py')
#这是打出的报告需要放到的位置
filename='C:\\课程资料\\code\\untitled\\report\\jiekouceshireport.html'
fp=open(filename,'wb')
runner=HTMLTestRunnerCN.HTMLTestRunner(stream=fp,title='接口测试报告',description='用例执行情况:')
runner.run(dis)
fp.close()
