import csv
import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage
from pages.login.log_in_page_read_csv import LogInPageReadCsv
from pages.login.login_page import LoginPage
from pages.user_center.user_center import UserCenter

class TestCase04LoginWithTester(unittest.TestCase):
    # 测试体验账号登录
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

    def test_user_login_exception(self):
        '''测试体验账号登录'''

        # 打开风控首页-登录页
        self.base_page.open_page()

        # 点击“我要体验”
        self.login_page.taste()

        # 判断登录成功后招呼栏的用户名是否正确
        username = self.user_center.get_username()

        self.assertEqual('小明', username, '登录成功后招呼栏的用户名错误')


        # 成功退出系统
        sleep(2)
        self.user_center.logout()


