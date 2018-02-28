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


class TestCase04UserManageEditUser(unittest.TestCase):
    # 测试用户管理修改用户
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

    def test_edit_user(self):
        # 通过csv测试修改用户功能

        csv_file = self.user_management_read_csv.read_csv('edit_user_info.csv')
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            edit_user_info = {
                "account": row[0],
                "password": row[1],
                "search_key": row[2],
                "edit_user_name": row[3],
                "edit_user_phone": row[4],
            }

            # 打开风控首页-登录页
            self.base_page.open_page()
            sleep(1)
            # 登录账号
            self.login_page.user_login(edit_user_info['account'], edit_user_info['password'])

            # 判断登录成功后招呼栏的用户名是否正确
            username = self.user_center.get_username()

            # 从数据库获取登录账号的用户名
            account_info = self.user_center.get_account_info_by_sql(edit_user_info['account'])
            print(account_info)
            account_name = account_info[1]

            self.assertEqual(account_name, username, '登录成功后招呼栏的用户名错误')

            # 点击进入用户管理
            self.user_management.click_user_manage()

            # 查找用户testAddUser2
            self.user_management.search_user(edit_user_info['search_key'])
            # 获取页面查找结果
            search_user_name_01 = self.user_management.get_search_result_one()
            # 查询数据库获取搜索结果
            user_info_00 = self.user_management.get_search_result_by_sql(edit_user_info['account'],
                                                                         edit_user_info['search_key'])
            user_name_00 = user_info_00[0]
            user_tel_00 = user_info_00[1]
            self.assertEqual(search_user_name_01, user_name_00)

            # 点击修改
            self.user_management.click_edit_user()
            # 切入内层frame
            self.user_management.switch_to_2_frame()
            # 获取当前显示的用户名称是否与未修改前一致
            current_user_name_01 = self.user_management.get_current_user_name()
            self.assertEqual(search_user_name_01, current_user_name_01)
            # 获取显示的用户手机号码是否与未修改前一致
            current_user_tel_01 = self.user_management.get_current_user_tel()
            self.assertEqual(user_tel_00, current_user_tel_01)

            # 输入用户名称
            self.user_management.input_add_user_name(edit_user_info['edit_user_name'])
            # 输入用户手机号码
            self.user_management.input_add_user_phone(edit_user_info['edit_user_phone'])
            # 点击取消
            self.user_management.click_add_user_dismiss()
            # 数据库查询是否修改失败
            user_info_01 = self.user_management.get_search_result_by_sql(edit_user_info['account'],
                                                                         edit_user_info['search_key'])
            user_name_01 = user_info_01[0]
            user_tel_01 = user_info_01[1]
            self.assertEqual(user_name_00, user_name_01)
            self.assertEqual(user_tel_00, user_tel_01)


            # 点击修改
            self.user_management.click_edit_user()
            # 切入内层frame
            self.user_management.switch_to_2_frame()
            # 获取当前显示的角色名称是否与未修改前一致
            current_user_name_02 = self.user_management.get_current_user_name()
            self.assertEqual(search_user_name_01, current_user_name_02)
            # 获取显示的角色描述是否与未修改前一致
            current_user_tel_02 = self.user_management.get_current_user_tel()
            self.assertEqual(user_tel_00, current_user_tel_02)

            # 输入用户名称
            self.user_management.input_add_user_name(edit_user_info['edit_user_name'])
            # 输入用户手机号码
            self.user_management.input_add_user_phone(edit_user_info['edit_user_phone'])
            # 点击关闭按钮
            self.user_management.click_add_user_close()
            # 数据库查询是否修改失败
            user_info_02 = self.user_management.get_search_result_by_sql(edit_user_info['account'],
                                                                         edit_user_info['search_key'])
            user_name_02 = user_info_02[0]
            user_tel_02 = user_info_02[1]
            self.assertEqual(user_name_00, user_name_02)
            self.assertEqual(user_tel_00, user_tel_02)

            # 点击修改
            self.user_management.click_edit_user()
            # 切入内层frame
            self.user_management.switch_to_2_frame()
            # 获取当前显示的角色名称是否与未修改前一致
            current_user_name_03 = self.user_management.get_current_user_name()
            self.assertEqual(search_user_name_01, current_user_name_03)
            # 获取显示的角色描述是否与未修改前一致
            current_user_tel_03 = self.user_management.get_current_user_tel()
            self.assertEqual(user_tel_00, current_user_tel_03)

            # 输入用户名称
            self.user_management.input_add_user_name(edit_user_info['edit_user_name'])
            # 输入用户手机号码
            self.user_management.input_add_user_phone(edit_user_info['edit_user_phone'])
            # 点击保存按钮
            self.user_management.click_add_user_save()
            # 数据库查询是否修改成功
            user_info_03 = self.user_management.get_search_result_by_sql(edit_user_info['account'],
                                                                         edit_user_info['edit_user_name'])
            user_name_03 = user_info_03[0]
            user_tel_03 = user_info_03[1]
            self.assertNotEqual(user_name_00, user_name_03)
            self.assertNotEqual(user_tel_00, user_tel_03)

            # 跳出外层frame
            self.user_management.switch_to_default_content()

            # 退出登录
            self.user_center.logout()

        csv_file.close()


