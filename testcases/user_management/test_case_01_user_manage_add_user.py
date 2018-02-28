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


class TestCase01UserManageAddUser(unittest.TestCase):
    # 测试用户管理新增用户
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

    def test_add_user(self):
        # 通过csv测试新增用户功能

        csv_file = self.user_management_read_csv.read_csv('add_user.csv')
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            add_user = {
                "account": row[0],
                "password": row[1],
                "add_user_name": row[2],
                "add_login_user": row[3],
                "add_login_passwd": row[4],
                "add_user_phone": row[5],
            }

            # 打开风控首页-登录页
            self.base_page.open_page()
            sleep(1)
            # 登录账号
            self.login_page.user_login(add_user['account'], add_user['password'])

            # 判断登录成功后招呼栏的用户名是否正确
            username = self.user_center.get_username()

            # 从数据库获取登录账号的用户名
            account_info = self.user_center.get_account_info_by_sql(add_user['account'])
            print(account_info)
            account_name = account_info[1]

            self.assertEqual(account_name, username, '登录成功后招呼栏的用户名错误')

            # 点击进入用户管理
            self.user_management.click_user_manage()
            # 点击新增用户
            self.user_management.click_add_user()
            # 切入内层frame
            self.user_management.switch_to_2_frame()
            # 输入新增用户名
            self.user_management.input_add_user_name(add_user['add_user_name'])
            # 输入登陆账号
            self.user_management.input_add_login_user(add_user['add_login_user'])
            # 输入登录密码
            self.user_management.input_add_login_passwd(add_user['add_login_passwd'])
            # 输入手机号码
            self.user_management.input_add_user_phone(add_user['add_user_phone'])
            # 分配角色
            self.user_management.input_add_user_role()
            # 选择所属公司部门
            self.user_management.choose_add_user_org()

            # 点击取消
            self.user_management.click_add_user_dismiss()
            # 从数据库查询验证角色未创建成功
            new_user_account_01 = self.user_management.get_add_user_by_sql(add_user['account'])
            self.assertNotEqual(new_user_account_01, add_user['add_login_user'])
            self.driver.wait(1)





            # 点击新增用户
            self.user_management.click_add_user()
            # 切入内层frame
            self.user_management.switch_to_2_frame()
            # 输入新增用户名
            self.user_management.input_add_user_name(add_user['add_user_name'])
            # 输入登陆账号
            self.user_management.input_add_login_user(add_user['add_login_user'])
            # 输入登录密码
            self.user_management.input_add_login_passwd(add_user['add_login_passwd'])
            # 输入手机号码
            self.user_management.input_add_user_phone(add_user['add_user_phone'])
            # 分配角色
            self.user_management.input_add_user_role()
            # 选择所属公司部门
            self.user_management.choose_add_user_org()
            # 点击关闭按钮
            self.user_management.click_add_user_close()

            # 从数据库查询验证角色未创建成功
            new_user_account_02 = self.user_management.get_add_user_by_sql(add_user['account'])
            self.assertNotEqual(new_user_account_02, add_user['add_login_user'])
            self.driver.wait(1)





            # 点击新增用户
            self.user_management.click_add_user()
            # 切入内层frame
            self.user_management.switch_to_2_frame()
            # 输入新增用户名
            self.user_management.input_add_user_name(add_user['add_user_name'])
            # 输入登陆账号
            self.user_management.input_add_login_user(add_user['add_login_user'])
            # 输入登录密码
            self.user_management.input_add_login_passwd(add_user['add_login_passwd'])
            # 输入手机号码
            self.user_management.input_add_user_phone(add_user['add_user_phone'])
            # 分配角色
            self.user_management.input_add_user_role()
            # 选择所属公司部门
            self.user_management.choose_add_user_org()
            # 点击保存按钮
            self.user_management.click_add_user_save()
            # 跳出最外层frame
            self.user_management.switch_to_default_content()
            # 从数据库查询验证角色创建成功
            new_add_account_03 = self.user_management.get_add_user_by_sql(add_user['account'])
            self.assertEqual(new_add_account_03, add_user['add_login_user'])
            self.driver.wait(1)

            # 退出登录
            self.user_center.logout()

        csv_file.close()


