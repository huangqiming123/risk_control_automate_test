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



class TestCase04UserCenterModifyPassword(unittest.TestCase):
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

        # 打开途强在线首页-登录页
        self.base_page.open_page()
        sleep(1)
        # 登录账号
        self.login_page.test_user_login()

    def tearDown(self):
        self.driver.quit_browser()

    def test_user_center_modify_password(self):
        # 通过csv测试修改密码功能

        # 点击打开修改密码框
        self.user_center.click_edit_password()

        csv_file = self.user_center_read_csv.read_csv("modify_password_exception.csv")
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            data = {
                "old_password": row[0],
                "new_password": row[1],
                "new_password2": row[2],
                "pwd_prompt": row[3],
            }

            text = self.user_center.get_modify_pwd_exception_prompt(data['old_password'],
                                                                    data['new_password'],
                                                                    data['new_password2']
                                                                    )

            self.assertIn(data["pwd_prompt"], text, "修改密码，错误提示语显示不一致")


        csv_file.close()

        # 关闭修改密码框
        self.user_center.click_edit_password_close()

        # 退出登录
        self.user_center.logout()
