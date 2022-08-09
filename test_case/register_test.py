import ddt

from func.csv_file_message import reader
from test_case.base_test_case import BaseTestCase


# 数据驱动类
@ddt.ddt
class RegisterTest(BaseTestCase):
    # 读取csv文件，注意要带后缀
    table_list = reader("register_test_cases.csv")

    # 数据驱动方法
    @ddt.data(*table_list)
    def test_register(self, row):
        # 循环每行数据
        self.driver.get("http://192.168.52.128/index.php?m=user&c=public&a=reg")
        self.driver.find_element("name", "username").send_keys(row[0])
        self.driver.find_element("name", "password").send_keys(row[1])
        self.driver.find_element("name", "userpassword2").send_keys(row[2])
        self.driver.find_element("name", "mobile_phone").send_keys(row[3])
        self.driver.find_element("name", "email").send_keys(row[4])
