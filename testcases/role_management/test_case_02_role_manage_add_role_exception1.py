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
from pages.role_management.role_management import RoleManagement
from pages.role_management.role_management_read_csv import RoleManagementReadCsv
from pages.user_center.user_center import UserCenter
from pages.user_center.user_center_read_csv import UserCenterReadCsv



class TestCase02RoleManageAddRoleException1(unittest.TestCase):
    # 测试角色管理新增角色功能异常情况
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.user_center = UserCenter(self.driver, self.base_url)
        self.role_management = RoleManagement(self.driver, self.base_url)
        self.log_in_page_read_csv = LogInPageReadCsv()
        self.user_center_read_csv = UserCenterReadCsv()
        self.role_management_read_csv = RoleManagementReadCsv()
        self.driver.set_window_max()
        self.connect_sql = ConnectSql()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

        # 打开风控首页-登录页
        self.base_page.open_page()
        sleep(1)
        # 登录账号
        self.login_page.test_user_login()



    def tearDown(self):
        self.driver.quit_browser()

    def test_add_role_exception1(self):
        # 通过csv测试新增角色功能异常情况


        # 获取当前登录账户
        log_in_account = self.user_center.get_login_account()
        print(log_in_account)


        csv_file = self.role_management_read_csv.read_csv('add_role_exception1.csv')
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            add_role_exception = {
                "add_role_name": row[0],
                "add_role_description": row[1],
                "add_role_limit": row[2],
                "exception_text": row[3],
            }

            # 点击进入角色管理
            self.role_management.click_role_manage()
            # 点击创建角色
            self.role_management.click_add_role()
            # 切入内层frame
            self.role_management.switch_to_2_frame()
            # 输入角色名称
            self.role_management.input_add_role_name(add_role_exception['add_role_name'])
            # 输入角色描述
            self.role_management.input_add_role_description(add_role_exception['add_role_description'])
            # 选择角色权限
            self.role_management.choose_add_role_limit(add_role_exception['add_role_limit'])
            # 点击保存按钮
            self.role_management.click_add_role_save()

            # 获取异常提示
            text = self.role_management.get_add_role_exception1()

            self.assertEqual(add_role_exception['exception_text'], text)


            # 关闭创建角色框
            self.role_management.click_add_role_close()

            # 跳出最外层frame
            self.role_management.switch_to_default_content()

            # 从数据库查询验证新增失败
            new_role_name = self.role_management.get_add_role_by_sql(log_in_account)
            self.assertNotEqual(new_role_name, add_role_exception['add_role_name'])
            self.driver.wait(1)


        csv_file.close()

        # 退出登录
        self.user_center.logout()
