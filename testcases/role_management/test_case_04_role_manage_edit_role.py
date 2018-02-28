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



class TestCase04RoleManageEditRole(unittest.TestCase):
    # 测试角色管理修改角色
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

    def test_edit_role(self):
        # 通过csv测试修改角色功能

        csv_file = self.role_management_read_csv.read_csv('edit_role_info.csv')
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            edit_role_info = {
                "account": row[0],
                "password": row[1],
                "search_key": row[2],
                "edit_role_name": row[3],
                "edit_role_description": row[4],
                "edit_role_limit": row[5],
            }

            # 打开风控首页-登录页
            self.base_page.open_page()
            sleep(1)
            # 登录账号
            self.login_page.user_login(edit_role_info['account'],edit_role_info['password'])


            # 判断登录成功后招呼栏的用户名是否正确
            username = self.user_center.get_username()

            # 从数据库获取登录账号的用户名
            account_info = self.user_center.get_account_info_by_sql(edit_role_info['account'])
            print(account_info)
            account_name = account_info[1]

            self.assertEqual(account_name, username, '登录成功后招呼栏的用户名错误')

            # 点击进入角色管理
            self.role_management.click_role_manage()

            # 查找11111角色
            self.role_management.search_role(edit_role_info['search_key'])
            # 获取页面查找结果
            search_role_name_01 = self.role_management.get_search_result_one()
            # 查询数据库获取搜索结果
            role_info_00 = self.role_management.get_search_result_by_sql(edit_role_info['account'], edit_role_info['search_key'])
            role_name_00 = role_info_00[0]
            role_desc_00 = role_info_00[1]
            self.assertEqual(search_role_name_01,role_name_00)

            # 点击修改
            self.role_management.click_edit_role()
            # 切入内层frame
            self.role_management.switch_to_2_frame()
            # 获取当前显示的角色名称是否与未修改前一致
            current_role_name_01 = self.role_management.get_current_role_name()
            self.assertEqual(search_role_name_01,current_role_name_01)
            # 获取显示的角色描述是否与未修改前一致
            current_role_desc = self.role_management.get_current_role_desc()
            self.assertEqual(role_desc_00,current_role_desc)

            # 输入角色名称
            self.role_management.input_add_role_name(edit_role_info['edit_role_name'])
            # 输入角色描述
            self.role_management.input_add_role_description(edit_role_info['edit_role_description'])
            # 选择角色权限
            self.role_management.choose_add_role_limit(edit_role_info['edit_role_limit'])
            # 点击取消
            self.role_management.click_add_role_dismiss()
            # 数据库查询是否修改失败
            role_info_01 = self.role_management.get_search_result_by_sql(edit_role_info['account'],
                                                                        edit_role_info['search_key'])
            role_name_01 = role_info_01[0]
            role_desc_01 = role_info_01[1]
            self.assertEqual(role_name_00, role_name_01)
            self.assertEqual(role_desc_00, role_desc_01)



            # 点击修改
            self.role_management.click_edit_role()
            # 切入内层frame
            self.role_management.switch_to_2_frame()
            # 获取当前显示的角色名称是否与未修改前一致
            current_role_name_01 = self.role_management.get_current_role_name()
            self.assertEqual(search_role_name_01, current_role_name_01)
            # 获取显示的角色描述是否与未修改前一致
            current_role_desc = self.role_management.get_current_role_desc()
            self.assertEqual(role_desc_00, current_role_desc)

            # 输入角色名称
            self.role_management.input_add_role_name(edit_role_info['edit_role_name'])
            # 输入角色描述
            self.role_management.input_add_role_description(edit_role_info['edit_role_description'])
            # 选择角色权限
            self.role_management.choose_add_role_limit(edit_role_info['edit_role_limit'])
            # 点击关闭按钮
            self.role_management.click_add_role_close()
            # 数据库查询是否修改失败
            role_info_02 = self.role_management.get_search_result_by_sql(edit_role_info['account'],
                                                                        edit_role_info['search_key'])
            role_name_02 = role_info_02[0]
            role_desc_02 = role_info_02[1]
            self.assertEqual(role_name_00, role_name_02)
            self.assertEqual(role_desc_00, role_desc_02)




            # 点击修改
            self.role_management.click_edit_role()
            # 切入内层frame
            self.role_management.switch_to_2_frame()
            # 获取当前显示的角色名称是否与未修改前一致
            current_role_name_01 = self.role_management.get_current_role_name()
            self.assertEqual(search_role_name_01, current_role_name_01)
            # 获取显示的角色描述是否与未修改前一致
            current_role_desc = self.role_management.get_current_role_desc()
            self.assertEqual(role_desc_00, current_role_desc)

            # 输入角色名称
            self.role_management.input_add_role_name(edit_role_info['edit_role_name'])
            # 输入角色描述
            self.role_management.input_add_role_description(edit_role_info['edit_role_description'])
            # 选择角色权限
            self.role_management.choose_add_role_limit(edit_role_info['edit_role_limit'])
            # 点击保存按钮
            self.role_management.click_add_role_save()
            # 数据库查询是否修改成功
            role_info_03 = self.role_management.get_search_result_by_sql(edit_role_info['account'],
                                                                        edit_role_info['edit_role_name'])
            role_name_03 = role_info_03[0]
            role_desc_03 = role_info_03[1]
            self.assertNotEqual(role_name_00, role_name_03)
            self.assertNotEqual(role_desc_00, role_desc_03)

            # 跳出外层frame
            self.role_management.switch_to_default_content()

            # 退出登录
            self.user_center.logout()

        csv_file.close()


