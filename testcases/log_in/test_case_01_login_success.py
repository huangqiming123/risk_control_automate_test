import csv
import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage
from pages.login.log_in_page_read_csv import LogInPageReadCsv
from pages.login.login_page import LoginPage
from pages.user_center.user_center import UserCenter

class TestCase01LoginSuccess(unittest.TestCase):
    # 测试用户账号登录成功
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.user_center = UserCenter(self.driver, self.base_url)
        self.log_in_page_read_csv = LogInPageReadCsv()
        self.driver.set_window_max()
        self.connect_sql = ConnectSql()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_user_login_by_csv(self):
        '''通过csv测试用户账户成功登录和成功退出功能'''
        data = ["部门管理", "设备", "贷款客户", "车辆监控中心", "统计报表", "设置"]

        csv_file = self.log_in_page_read_csv.read_csv('login_account.csv')
        csv_data = csv.reader(csv_file)

        for row in csv_data:
            user_to_login = {
                "account": row[0],
                "passwd": row[1],
            }

            # 打开风控首页-登录页
            self.base_page.open_page()
            # 输入用户信息进行登录
            self.login_page.user_login(user_to_login["account"], user_to_login["passwd"])
            self.driver.wait(1)

            # 判断登录成功后招呼栏的用户名是否正确
            username = self.user_center.get_username()

            # 从数据库获取登录账号的用户名
            account_info = self.user_center.get_account_info_by_sql(user_to_login['account'])
            print(account_info)
            account_name = account_info[1]

            self.assertEqual(account_name, username, '登录成功后招呼栏的用户名错误')

            # 验证模块
            module = self.user_center.get_module_name()
            print(module)
            self.assertEqual(data, module, "用户账号登录，模块显示错误")


            # 取消退出系统
            sleep(2)
            self.user_center.logout_dismiss()

            # 关闭退出系统弹框
            sleep(2)
            self.user_center.logout_close()

            # 成功退出系统
            sleep(2)
            self.user_center.logout()

            # 再次登录判断是否成功退出到登录页并登录成功
            self.login_page.user_login(user_to_login["account"], user_to_login["passwd"])

            # # 成功退出系统
            sleep(2)
            self.user_center.logout()

        csv_file.close()
