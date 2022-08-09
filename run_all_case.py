import unittest

from lib.HTMLTestRunner import HTMLTestRunner

if __name__ == '__main__':
    #先找到需要执行的测试用例
    suite = unittest.defaultTestLoader.discover("./test_case", "*test.py")
    #指的测试报告的位置
    path = "report/TestReport.html"
    #准备写入测试报告
    file = open(path, "wb")
    #通过第三方的库编写测试报告
    HTMLTestRunner(stream=file,verbosity=1,title="自动化测试报告",description="Chrome", tester ="陈凯杰").run(suite)
