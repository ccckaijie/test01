import time
import unittest
from selenium import webdriver


# 创建一个重复代码的类，
class BaseTestCase(unittest.TestCase):
    # 先进行实例化，打开浏览器窗口全屏，再隐式等待5s
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(5)

    # 最后关闭浏览器
    @classmethod
    def tearDownClass(cls):
        time.sleep(3)
        cls.driver.quit()
