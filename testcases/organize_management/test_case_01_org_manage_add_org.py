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



class TestCase01OrgManageAddOrg(unittest.TestCase):
    # 测试部门管理新增公司部门
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.user_center = UserCenter(self.driver, self.base_url)
        self.organize_management = OrganizeManagement(self.driver, self.base_url)
        self.log_in_page_read_csv = LogInPageReadCsv()
        self.user_center_read_csv = UserCenterReadCsv()
        self.organize_management_read_csv = OrganizeManagementReadCsv()
        self.driver.set_window_max()
        self.connect_sql = ConnectSql()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)



    def tearDown(self):
        self.driver.quit_browser()

    def test_add_org(self):
        # 通过csv测试新增公司部门功能

        csv_file = self.user_center_read_csv.read_csv('add_org_info.csv')
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            add_org_info = {
                "account": row[0],
                "password": row[1],
                "add_org_name": row[2],
                "add_org_tel": row[3],
            }

            # 打开风控首页-登录页
            self.base_page.open_page()
            sleep(1)
            # 登录账号
            self.login_page.user_login(add_org_info['account'],add_org_info['password'])


            # 判断登录成功后招呼栏的用户名是否正确
            username = self.user_center.get_username()

            # 从数据库获取登录账号的用户名
            account_info = self.user_center.get_account_info_by_sql(add_org_info['account'])
            print(account_info)
            account_name = account_info[1]

            self.assertEqual(account_name, username, '登录成功后招呼栏的用户名错误')


            # 点击进入部门管理
            self.organize_management.click_org_manage()
            # 点击新增公司部门
            self.organize_management.click_add_org()
            # 验证上级部门是否显示正确
            sup_org_name = self.organize_management.get_sup_org_name()
            # 数据库查询当前登录账户的上级部门
            sup_org_name_by_aql = self.organize_management.get_user_sup_org_by_sql(add_org_info['account'])

            self.assertEqual(sup_org_name,sup_org_name_by_aql)

            # 选择上级部门
            self.organize_management.choose_sup_org()
            # 填写新增部门名称
            self.organize_management.input_add_org_name(add_org_info['add_org_name'])
            # 填写联系方式
            self.organize_management.input_add_org_tel(add_org_info['add_org_tel'])
            # 点击取消
            self.organize_management.click_add_org_dismiss()
            # 从数据库查询验证未新增成功
            new_org_name_01 = self.organize_management.get_add_org_by_sql(add_org_info['account'])
            self.assertNotEqual(new_org_name_01,add_org_info['add_org_name'])
            self.driver.wait(1)


            # 点击新增公司部门
            self.organize_management.click_add_org()
            # 验证上级部门是否显示正确
            sup_org_name = self.organize_management.get_sup_org_name()
            # 数据库查询当前登录账户的上级部门
            sup_org_name_by_aql = self.organize_management.get_user_sup_org_by_sql(add_org_info['account'])

            self.assertEqual(sup_org_name, sup_org_name_by_aql)

            # 选择上级部门
            self.organize_management.choose_sup_org()
            # 填写新增部门名称
            self.organize_management.input_add_org_name(add_org_info['add_org_name'])
            # 填写联系方式
            self.organize_management.input_add_org_tel(add_org_info['add_org_tel'])
            # 点击关闭按钮
            self.organize_management.click_add_org_close()

            # 从数据库查询验证未新增成功
            new_org_name_02 = self.organize_management.get_add_org_by_sql(add_org_info['account'])
            self.assertNotEqual(new_org_name_02, add_org_info['add_org_name'])
            self.driver.wait(1)


            # 点击新增公司部门
            self.organize_management.click_add_org()
            # 验证上级部门是否显示正确
            sup_org_name = self.organize_management.get_sup_org_name()
            # 数据库查询当前登录账户的上级部门
            sup_org_name_by_aql = self.organize_management.get_user_sup_org_by_sql(add_org_info['account'])

            self.assertEqual(sup_org_name, sup_org_name_by_aql)

            # 选择上级部门
            self.organize_management.choose_sup_org()
            # 填写新增部门名称
            self.organize_management.input_add_org_name(add_org_info['add_org_name'])
            # 填写联系方式
            self.organize_management.input_add_org_tel(add_org_info['add_org_tel'])
            # 点击保存按钮
            self.organize_management.click_add_org_save()
            # 跳出最外层frame
            self.organize_management.switch_to_default_content()
            # 从数据库查询验证新增成功
            new_org_name_03 = self.organize_management.get_add_org_by_sql(add_org_info['account'])
            self.assertEqual(new_org_name_03, add_org_info['add_org_name'])
            self.driver.wait(1)


            # 退出登录
            self.user_center.logout()

        csv_file.close()


