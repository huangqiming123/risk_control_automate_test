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



class TestCase08OrgManageDeleteOrg(unittest.TestCase):
    # 测试部门管理删除公司部门
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

    def test_delete_org(self):
        # 通过csv测试删除公司部门功能


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

        csv_file = self.user_center_read_csv.read_csv('delete_org.csv')
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            delete_org = {
                "org_name": row[0],
            }

            # 按名称查找部门
            self.organize_management.search_org(delete_org['org_name'])

            # 点击删除
            self.organize_management.click_delete_org()

            # 跳出frame
            self.organize_management.switch_to_default_content()
            # 取消
            self.organize_management.delete_org_dismiss()

            # 切入frame
            self.organize_management.switch_to_1_frame()
            # 点击删除
            self.organize_management.click_delete_org()
            # 跳出frame
            self.organize_management.switch_to_default_content()
            # 关闭
            self.organize_management.delete_org_close()

            # 切入frame
            self.organize_management.switch_to_1_frame()
            # 点击删除
            self.organize_management.click_delete_org()
            # 跳出frame
            self.organize_management.switch_to_default_content()
            # 确认
            self.organize_management.delete_org_accept()

            # 数据库查找验证部门是否删除成功

            # 数据库查找部门
            org_name_after_delete = self.organize_management.get_search_result_orgname_by_sql(log_in_account, '')

            self.assertNotIn(delete_org['org_name'],org_name_after_delete)

            # 切入frame
            self.organize_management.switch_to_1_frame()


        csv_file.close()

        # 跳出frame
        self.organize_management.switch_to_default_content()
        # 退出登录
        self.user_center.logout()
