import csv
import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage
from pages.login.log_in_page_read_csv import LogInPageReadCsv
from pages.login.login_page import LoginPage
from pages.user_center.user_center import UserCenter

class TestCase05UserCenterLogout(unittest.TestCase):
    # 测试用户中心退出登录
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

    def test_user_center_logout(self):
        '''测试用户中心退出登录功能'''
        self.base_page.open_page()
        self.login_page.test_user_login()

        # 取消退出登录
        self.user_center.logout_dismiss()

        # 关闭退出登录
        self.user_center.logout_close()

        # 确认退出登录
        self.user_center.logout()