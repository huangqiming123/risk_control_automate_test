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



class TestCase06OrgManageViewOrg(unittest.TestCase):
    # 测试部门管理查看公司部门
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

    def test_view_org(self):
        # 通过csv测试查看公司部门功能


        # 打开风控首页-登录页
        self.base_page.open_page()
        sleep(1)
        # 登录账号
        self.login_page.test_user_login()

        # 获取当前登录账户
        log_in_account = self.user_center.get_login_account()
        print(log_in_account)

        # 点击进入部门管理
        self.organize_management.click_org_manage()


        csv_file = self.user_center_read_csv.read_csv('view_org_info.csv')
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            view_org_info = {
                "view_org_name": row[0],
                "view_org_tel": row[1],
            }


            # 点击查看公司部门
            self.organize_management.click_view_org()
            # 切入内层frame
            self.organize_management.switch_to_2_frame()

            # 验证所属上级是否显示正确
            sup_org_name = self.organize_management.get_current_sup_org_name()
            # 数据库查询当前登录账户的上级部门
            sup_org_name_by_aql = self.organize_management.get_belong_to_superior_org_by_sql(log_in_account)

            self.assertEqual(sup_org_name,sup_org_name_by_aql)

            # 编辑公司/部门名称
            self.organize_management.edit_org_name(view_org_info['view_org_name'])
            # 编辑联系方式
            self.organize_management.edit_org_tel(view_org_info['view_org_tel'])
            # 跳出内层frame
            self.organize_management.switch_to_parent_content()
            # 取消
            self.organize_management.click_org_modify_dismiss()
            # 从数据库查询验证未修改成功
            current_org_info_01 = self.organize_management.get_current_org_info_by_sql(log_in_account)
            edit_org_name_01 = current_org_info_01[0]
            edit_org_tel_01 = current_org_info_01[1]
            self.assertNotEqual(edit_org_name_01,view_org_info['view_org_name'])
            self.assertNotEqual(edit_org_tel_01, view_org_info['view_org_tel'])
            self.driver.wait(1)



            # 点击查看公司部门
            self.organize_management.click_view_org()
            # 切入内层frame
            self.organize_management.switch_to_2_frame()

            # 验证所属上级是否显示正确
            sup_org_name = self.organize_management.get_current_sup_org_name()
            # 数据库查询当前登录账户的上级部门
            sup_org_name_by_aql = self.organize_management.get_belong_to_superior_org_by_sql(log_in_account)

            self.assertEqual(sup_org_name, sup_org_name_by_aql)

            # 编辑公司/部门名称
            self.organize_management.edit_org_name(view_org_info['view_org_name'])
            # 编辑联系方式
            self.organize_management.edit_org_tel(view_org_info['view_org_tel'])
            # 跳出内层frame
            self.organize_management.switch_to_parent_content()
            # 关闭
            self.organize_management.click_org_modify_close()
            # 从数据库查询验证未修改成功
            current_org_info_02 = self.organize_management.get_current_org_info_by_sql(log_in_account)
            edit_org_name_02 = current_org_info_02[0]
            edit_org_tel_02 = current_org_info_02[1]
            self.assertNotEqual(edit_org_name_02, view_org_info['view_org_name'])
            self.assertNotEqual(edit_org_tel_02, view_org_info['view_org_tel'])
            self.driver.wait(1)





            # 点击查看公司部门
            self.organize_management.click_view_org()
            # 切入内层frame
            self.organize_management.switch_to_2_frame()

            # 验证所属上级是否显示正确
            sup_org_name = self.organize_management.get_current_sup_org_name()
            # 数据库查询当前登录账户的上级部门
            sup_org_name_by_aql = self.organize_management.get_belong_to_superior_org_by_sql(log_in_account)

            self.assertEqual(sup_org_name, sup_org_name_by_aql)

            # 编辑公司/部门名称
            self.organize_management.edit_org_name(view_org_info['view_org_name'])
            # 编辑联系方式
            self.organize_management.edit_org_tel(view_org_info['view_org_tel'])
            # 跳出内层frame
            self.organize_management.switch_to_parent_content()
            # 修改(保存)
            self.organize_management.click_org_modify_button()
            # 从数据库查询验证修改成功
            current_org_info_03 = self.organize_management.get_current_org_info_by_sql(log_in_account)
            edit_org_name_03 = current_org_info_03[0]
            edit_org_tel_03 = current_org_info_03[1]
            self.assertEqual(edit_org_name_03, view_org_info['view_org_name'])
            self.assertEqual(edit_org_tel_03, view_org_info['view_org_tel'])
            self.driver.wait(1)


        # 跳出外层frame
        self.organize_management.switch_to_default_content()
        csv_file.close()

        # 退出登录
        self.user_center.logout()
