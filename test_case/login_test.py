import time

from selenium.webdriver.common.by import By

from test_case.base_test_case import BaseTestCase


# 登录的测试用例
class LonginTest(BaseTestCase):
    def test_login(self):
        self.driver.get("http://192.168.52.128/index.php?m=user&c=public&a=login")
        self.driver.find_element("id", "username").send_keys("chenkaijie")
        self.driver.find_element("id", "password").send_keys("12345678")
        self.driver.find_element(By.CSS_SELECTOR, ".login_btn.fl").click()
        # 存在一个过渡页面需要等待3s
        time.sleep(3)
        # 查询欢迎语句是一个变量所以要跟着登录账号走
        welcome = self.driver.find_element(By.CSS_SELECTOR, ".site-nav-right.fr > a:nth-child(1)").text
        self.assertEqual("我的会员中心 - 道e坊商城 - Powered by Haidao", self.driver.title)
        self.assertEqual("http://192.168.52.128/index.php?m=user&c=index&a=index", self.driver.current_url)
        self.assertEqual("你好 陈凯杰", welcome)
