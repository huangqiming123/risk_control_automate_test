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



class TestCase06RoleManageDeleteRole(unittest.TestCase):
    # 测试角色管理删除角色
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

    def test_delete_role(self):
        # 通过csv测试删除角色功能


        csv_file = self.role_management_read_csv.read_csv('delete_role.csv')
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            delete_role = {
                "account": row[0],
                "passwd": row[1],
                "delete_role_name": row[2],
            }

            # 打开风控首页-登录页
            self.base_page.open_page()
            sleep(1)
            # 登录账号
            self.login_page.user_login(delete_role['account'],delete_role['passwd'])


            # 点击进入角色管理
            self.role_management.click_role_manage()

            # 按名称查找角色
            self.role_management.search_role(delete_role['delete_role_name'])

            # 点击删除
            self.role_management.click_delete_role()
            # 跳出frame
            self.role_management.switch_to_default_content()
            # 点击取消
            self.role_management.delete_role_dismiss()



            # 切入frame
            self.role_management.switch_to_1_frame()
            # 点击删除
            self.role_management.click_delete_role()
            # 跳出frame
            self.role_management.switch_to_default_content()
            # 点击关闭
            self.role_management.delete_role_close()




            # 切入frame
            self.role_management.switch_to_1_frame()
            # 点击删除
            self.role_management.click_delete_role()
            # 跳出frame
            self.role_management.switch_to_default_content()
            # 点击确认
            self.role_management.delete_role_accept()

            # 数据库查找验证部门是否删除成功

            # 数据库查找角色
            role_name_after_delete = self.role_management.get_search_result_rolename_by_sql(delete_role['account'], '')

            self.assertNotIn(delete_role['delete_role_name'], role_name_after_delete)

            # 退出登录
            self.user_center.logout()

        csv_file.close()




