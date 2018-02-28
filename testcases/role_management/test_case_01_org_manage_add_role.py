import csv
import unittest
from time import sleep
from automate_driver.automate_driver import AutomateDriver
from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage
from pages.login.log_in_page_read_csv import LogInPageReadCsv
from pages.login.login_page import LoginPage
from pages.role_management.role_management import RoleManagement
from pages.role_management.role_management_read_csv import RoleManagementReadCsv
from pages.user_center.user_center import UserCenter
from pages.user_center.user_center_read_csv import UserCenterReadCsv



class TestCase01OrgManageAddRole(unittest.TestCase):
    # 测试角色管理新增角色
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



    def tearDown(self):
        self.driver.quit_browser()

    def test_add_role(self):
        # 通过csv测试新增角色功能

        csv_file = self.role_management_read_csv.read_csv('add_role.csv')
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            add_role = {
                "account": row[0],
                "password": row[1],
                "add_role_name": row[2],
                "add_role_description": row[3],
                "add_role_limit": row[4],
            }

            # 打开风控首页-登录页
            self.base_page.open_page()
            sleep(1)
            # 登录账号
            self.login_page.user_login(add_role['account'],add_role['password'])


            # 判断登录成功后招呼栏的用户名是否正确
            username = self.user_center.get_username()

            # 从数据库获取登录账号的用户名
            account_info = self.user_center.get_account_info_by_sql(add_role['account'])
            print(account_info)
            account_name = account_info[1]

            self.assertEqual(account_name, username, '登录成功后招呼栏的用户名错误')


            # 点击进入角色管理
            self.role_management.click_role_manage()
            # 点击创建角色
            self.role_management.click_add_role()
            # 切入内层frame
            self.role_management.switch_to_2_frame()
            # 输入角色名称
            self.role_management.input_add_role_name(add_role['add_role_name'])
            # 输入角色描述
            self.role_management.input_add_role_description(add_role['add_role_description'])
            # 选择角色权限
            self.role_management.choose_add_role_limit(add_role['add_role_limit'])
            # 点击取消
            self.role_management.click_add_role_dismiss()
            # 从数据库查询验证角色未创建成功
            new_role_name_01 = self.role_management.get_add_role_by_sql(add_role['account'])
            self.assertNotEqual(new_role_name_01,add_role['add_role_name'])
            self.driver.wait(1)


            # 点击创建角色
            self.role_management.click_add_role()
            # 切入内层frame
            self.role_management.switch_to_2_frame()
            # 输入角色名称
            self.role_management.input_add_role_name(add_role['add_role_name'])
            # 输入角色描述
            self.role_management.input_add_role_description(add_role['add_role_description'])
            # 选择角色权限
            self.role_management.choose_add_role_limit(add_role['add_role_limit'])
            # 点击关闭按钮
            self.role_management.click_add_role_close()

            # 从数据库查询验证角色未创建成功
            new_role_name_02 = self.role_management.get_add_role_by_sql(add_role['account'])
            self.assertNotEqual(new_role_name_02, add_role['add_role_name'])
            self.driver.wait(1)


            # 点击创建角色
            self.role_management.click_add_role()
            # 切入内层frame
            self.role_management.switch_to_2_frame()
            # 输入角色名称
            self.role_management.input_add_role_name(add_role['add_role_name'])
            # 输入角色描述
            self.role_management.input_add_role_description(add_role['add_role_description'])
            # 选择角色权限
            self.role_management.choose_add_role_limit(add_role['add_role_limit'])
            # 点击保存按钮
            self.role_management.click_add_role_save()
            # 跳出最外层frame
            self.role_management.switch_to_default_content()
            # 从数据库查询验证角色创建成功
            new_role_name_03 = self.role_management.get_add_role_by_sql(add_role['account'])
            self.assertEqual(new_role_name_03, add_role['add_role_name'])
            self.driver.wait(1)


            # 退出登录
            self.user_center.logout()

        csv_file.close()


