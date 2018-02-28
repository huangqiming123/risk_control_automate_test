import csv
import unittest
from time import sleep
from automate_driver.automate_driver import AutomateDriver
from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage
from pages.login.log_in_page_read_csv import LogInPageReadCsv
from pages.login.login_page import LoginPage
from pages.organize_management.organize_management import OrganizeManagement
from pages.organize_management.organize_management_read_csv import OrganizeManagementReadCsv
from pages.user_center.user_center import UserCenter
from pages.user_center.user_center_read_csv import UserCenterReadCsv
from pages.user_management.user_management import UserManagement
from pages.user_management.user_management_read_csv import UserManagementReadCsv


class TestCase06UserManageDeleteUser(unittest.TestCase):
    # 测试用户管理删除用户
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.user_center = UserCenter(self.driver, self.base_url)
        self.user_management = UserManagement(self.driver, self.base_url)
        self.log_in_page_read_csv = LogInPageReadCsv()
        self.user_center_read_csv = UserCenterReadCsv()
        self.user_management_read_csv = UserManagementReadCsv()
        self.driver.set_window_max()
        self.connect_sql = ConnectSql()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)



    def tearDown(self):
        self.driver.quit_browser()

    def test_delete_user(self):
        # 通过csv测试删除用户功能


        csv_file = self.user_management_read_csv.read_csv('delete_user.csv')
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            delete_user = {
                "account": row[0],
                "passwd": row[1],
                "delete_user_name": row[2],
            }

            # 打开风控首页-登录页
            self.base_page.open_page()
            sleep(1)
            # 登录账号
            self.login_page.user_login(delete_user['account'], delete_user['passwd'])

            # 点击进入角色管理
            self.user_management.click_user_manage()

            # 按名称查找角色
            self.user_management.search_user(delete_user['delete_user_name'])

            # 点击删除
            self.user_management.click_delete_user()
            # 跳出frame
            self.user_management.switch_to_default_content()
            # 点击取消
            self.user_management.delete_user_dismiss()

            # 切入frame
            self.user_management.switch_to_1_frame()
            # 点击删除
            self.user_management.click_delete_user()
            # 跳出frame
            self.user_management.switch_to_default_content()
            # 点击关闭
            self.user_management.delete_user_close()

            # 切入frame
            self.user_management.switch_to_1_frame()
            # 点击删除
            self.user_management.click_delete_user()
            # 跳出frame
            self.user_management.switch_to_default_content()
            # 点击确认
            self.user_management.delete_user_accept()

            # 数据库查找验证部门是否删除成功

            # 数据库查找角色
            user_name_after_delete = self.user_management.get_search_result_username_by_sql(delete_user['account'], '')

            self.assertNotIn(delete_user['delete_user_name'], user_name_after_delete)

            # 退出登录
            self.user_center.logout()

        csv_file.close()
