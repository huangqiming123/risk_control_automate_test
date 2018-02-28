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



class TestCase05OrgManageEditOrgException(unittest.TestCase):
    # 测试部门管理修改公司部门异常情况
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

    def test_edit_org_exception(self):
        # 通过csv测试修改公司部门功能异常情况


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

        # 查找test00000部门
        search_key = '00000'
        self.organize_management.search_org(search_key)

        # 获取页面查找结果
        search_org_name_01 = self.organize_management.get_search_result_one()
        # 查询数据库获取搜索结果
        org_info_00 = self.organize_management.get_search_result_by_sql(log_in_account,
                                                                        search_key)
        org_name_00 = org_info_00[0]
        sup_org_name_00 = org_info_00[1]
        org_tel_00 = org_info_00[2]
        self.assertEqual(search_org_name_01, org_name_00)

        csv_file = self.user_center_read_csv.read_csv('edit_org_info_exception.csv')
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            edit_org_info_exception = {
                "edit_org_name": row[0],
                "edit_org_tel": row[1],
                "exception_text": row[2],
            }


            # 点击修改
            self.organize_management.click_edit_org()
            # 切入内层frame
            self.organize_management.switch_to_2_frame()
            # 获取当前显示的部门名称是否与未修改前一致
            current_org_name_01 = self.organize_management.get_current_org_name()
            self.assertEqual(search_org_name_01, current_org_name_01)
            # 获取显示的所属上级是否与未修改前一致
            current_sup_org = self.organize_management.get_current_sup_org_name()
            self.assertEqual(sup_org_name_00, current_sup_org)
            # 获取显示的联系方式是否与未修改前一致
            current_org_tel = self.organize_management.get_current_org_tel()
            self.assertEqual(org_tel_00, current_org_tel)

            # 修改部门名称
            self.organize_management.edit_org_name(edit_org_info_exception['edit_org_name'])
            # 修改联系方式
            self.organize_management.edit_org_tel(edit_org_info_exception['edit_org_tel'])
            # 跳出内层frame
            self.organize_management.switch_to_parent_content()

            # 修改(保存)
            self.organize_management.click_org_modify_button()
            # 获取异常提示语
            exception_text = self.organize_management.get_edit_org_exception_text()
            self.assertEqual(edit_org_info_exception['exception_text'],exception_text)

            # 数据库查询是否修改失败
            org_info = self.organize_management.get_search_result_by_sql(log_in_account,
                                                                         search_key)
            org_name = org_info[0]
            org_tel = org_info[2]
            self.assertNotEqual(edit_org_info_exception['edit_org_name'], org_name)
            self.assertNotEqual(edit_org_info_exception['edit_org_tel'], org_tel)

            # 跳出内层frame
            self.organize_management.switch_to_parent_content()

            # 关闭
            self.organize_management.click_org_modify_close()



        csv_file.close()

        # 跳出外层frame
        self.organize_management.switch_to_default_content()

        # 退出登录
        self.user_center.logout()
