
import unittest

from automate_driver.automate_driver import AutomateDriver
from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage
from pages.login.log_in_page_read_csv import LogInPageReadCsv
from pages.login.login_page import LoginPage

class TestCase02LoginException(unittest.TestCase):
    # 测试登录异常情况
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.log_in_page_read_csv = LogInPageReadCsv()
        self.driver.set_window_max()
        self.connect_sql = ConnectSql()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_user_login_exception(self):
        '''测试用户账户登录异常'''

        # 打开风控首页-登录页
        self.base_page.open_page()

        # 第一种，密码和账号都为空
        self.login_page.account_input('')
        self.login_page.password_input('')
        self.login_page.login_button_click()
        self.driver.wait()
        self.assertEqual('登录账号不能为空', self.login_page.get_exception_text())

        # 第二种，密码和账号其中一个不为空
        self.login_page.account_input('syntest')
        self.login_page.password_input('')
        self.login_page.login_button_click()
        self.driver.wait()
        self.assertEqual('登陆密码不能为空', self.login_page.get_exception_text())

        self.login_page.account_input('')
        self.login_page.password_input('jimi123')
        self.login_page.login_button_click()
        self.driver.wait()
        self.assertEqual('登录账号不能为空', self.login_page.get_exception_text())


        # 第三种，账号不存在
        self.login_page.account_input('abdwerewf')
        self.login_page.password_input('123')
        self.login_page.login_button_click()
        self.driver.wait()
        self.assertEqual('账号不存在或者已经停用', self.login_page.get_exception_text())


        # 第四种，密码错误
        self.login_page.account_input('syntest')
        self.login_page.password_input('jimi')
        self.login_page.login_button_click()
        self.driver.wait()
        self.assertEqual('登录密码验证错误', self.login_page.get_exception_text())