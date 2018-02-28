import csv
import unittest
from time import sleep
from automate_driver.automate_driver import AutomateDriver
from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage
from pages.login.log_in_page_read_csv import LogInPageReadCsv
from pages.login.login_page import LoginPage
from pages.user_center.user_center import UserCenter
from pages.user_center.user_center_read_csv import UserCenterReadCsv



class TestCase03UserCenterModifyPassword(unittest.TestCase):
    # 测试个人中心修改密码
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.user_center = UserCenter(self.driver, self.base_url)
        self.log_in_page_read_csv = LogInPageReadCsv()
        self.user_center_read_csv = UserCenterReadCsv()
        self.driver.set_window_max()
        self.connect_sql = ConnectSql()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)



    def tearDown(self):
        self.driver.quit_browser()

    def test_user_center_modify_password(self):
        # 通过csv测试修改密码功能

        csv_file = self.user_center_read_csv.read_csv('user_to_modify_password.csv')
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            user_to_modify_password = {
                "account": row[0],
                "old_passwd": row[1],
                "new_passwd": row[2],
            }

            # 打开途强在线首页-登录页
            self.base_page.open_page()
            sleep(1)
            # 登录账号
            self.login_page.user_login(user_to_modify_password['account'],user_to_modify_password['old_passwd'])

            # 修改密码
            self.user_center.click_edit_password()
            self.user_center.input_old_password(user_to_modify_password['old_passwd'])
            self.user_center.input_new_password(user_to_modify_password['new_passwd'])
            self.user_center.input_password_again(user_to_modify_password['new_passwd'])

            # 确认
            self.user_center.click_edit_password_confirm()
            self.driver.wait()



            # 用旧密码登录，验证提示
            self.login_page.user_login(user_to_modify_password['account'],user_to_modify_password['old_passwd'])
            exception_text = self.login_page.get_exception_text()
            self.assertEqual('登录密码验证错误',exception_text)

            self.driver.wait()

            # 用新密码登录，验证是否修改成功
            self.login_page.user_login(user_to_modify_password['account'], user_to_modify_password['new_passwd'])
            # 判断登录成功后招呼栏的用户名是否正确
            username = self.user_center.get_username()

            # 从数据库获取登录账号的用户名
            account_info = self.user_center.get_account_info_by_sql(user_to_modify_password['account'])
            print(account_info)
            account_name = account_info[1]

            self.assertEqual(account_name, username, '登录成功后招呼栏的用户名错误')

            # 退出登录
            self.user_center.logout()

        csv_file.close()


