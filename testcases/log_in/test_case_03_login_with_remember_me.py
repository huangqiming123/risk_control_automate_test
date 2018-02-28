import csv
import unittest
from time import sleep

from automate_driver.automate_driver import AutomateDriver
from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage
from pages.login.log_in_page_read_csv import LogInPageReadCsv
from pages.login.login_page import LoginPage
from pages.user_center.user_center import UserCenter

class TestCase03LoginWithRememberMe(unittest.TestCase):
    # 测试登录时记住密码
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
        '''测试登录时记住密码'''

        # 打开风控首页-登录页
        self.base_page.open_page()

        # 登录时勾选“记住我”复选框
        self.login_page.account_input('syntest')
        self.login_page.password_input('jimi123')
        self.login_page.remember_me()
        self.login_page.login_button_click()
        self.driver.wait()

        # 判断登录成功后招呼栏的用户名是否正确
        username = self.user_center.get_username()

        # 从数据库获取登录账号的用户名
        account_info = self.user_center.get_account_info_by_sql('syntest')
        print(account_info)
        account_name = account_info[1]

        self.assertEqual(account_name, username, '登录成功后招呼栏的用户名错误')


        # 成功退出系统
        sleep(2)
        self.user_center.logout()

        # 输入用户名
        self.login_page.account_input('syntest')
        # 点击密码输入框
        self.login_page.click_password()
        self.driver.wait()
        # 验证退出系统后“记住我”复选框是否是已勾选状态
        box_status = self.login_page.check_remember_me()
        self.assertEqual(True, box_status, '记住密码失败')

        self.driver.wait()

        # 输入用户名，不输入密码直接点击登录
        self.login_page.login_button_click()
        self.driver.wait()

        # 判断登录成功后招呼栏的用户名是否正确
        username = self.user_center.get_username()

        # 从数据库获取登录账号的用户名
        account_info = self.user_center.get_account_info_by_sql('syntest')
        print(account_info)
        account_name = account_info[1]

        self.assertEqual(account_name, username, '登录成功后招呼栏的用户名错误')


        # 成功退出系统
        sleep(2)
        self.user_center.logout()

        # 输入用户名
        self.login_page.account_input('syntest')
        # 点击密码输入框
        self.login_page.click_password()
        # 验证退出系统后“记住我”复选框是否是已勾选状态
        box_status = self.login_page.check_remember_me()
        self.assertEqual(True, box_status, '记住密码失败')

        self.driver.wait()

        # 输入用户名，取消勾选“记住我”复选框,输入密码再次登录
        self.login_page.account_input('syntest')
        # 点击密码输入框
        self.login_page.click_password()
        self.driver.wait(2)
        # 取消勾选“记住我”复选框
        self.login_page.remember_me()

        # 验证“记住我”复选框是否是未勾选状态
        box_status = self.login_page.check_remember_me()
        self.assertEqual(False, box_status, '取消记住密码失败')

        # 点击登录
        self.login_page.login_button_click()
        self.driver.wait()

        # 判断登录成功后招呼栏的用户名是否正确
        username = self.user_center.get_username()

        # 从数据库获取登录账号的用户名
        account_info = self.user_center.get_account_info_by_sql('syntest')
        print(account_info)
        account_name = account_info[1]

        self.assertEqual(account_name, username, '登录成功后招呼栏的用户名错误')

        # 成功退出系统
        sleep(2)
        self.user_center.logout()

        # 输入用户名
        self.login_page.account_input('syntest')
        # 点击密码输入框
        self.login_page.click_password()
        # 验证退出系统后“记住我”复选框是否是未勾选状态
        box_status = self.login_page.check_remember_me()
        self.assertEqual(False, box_status, '取消记住密码失败')




