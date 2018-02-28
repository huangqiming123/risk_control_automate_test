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



class TestCase05RoleManageSearchRole(unittest.TestCase):
    # 测试角色管理搜索角色
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

    def test_search_role(self):
        # 通过csv测试搜索角色功能

        csv_file = self.role_management_read_csv.read_csv('search_role.csv')
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            search_role = {
                "account": row[0],
                "password": row[1],
                "search_name": row[2],
            }

            # 打开风控首页-登录页
            self.base_page.open_page()
            sleep(1)
            # 登录账号
            self.login_page.user_login(search_role['account'],search_role['password'])

            # 判断登录成功后招呼栏的用户名是否正确
            username = self.user_center.get_username()

            # 从数据库获取登录账号的用户名
            account_info = self.user_center.get_account_info_by_sql(search_role['account'])
            print(account_info)
            account_name = account_info[1]

            self.assertEqual(account_name, username, '登录成功后招呼栏的用户名错误')


            # 点击进入角色管理
            self.role_management.click_role_manage()

            # 输入搜索关键词进行搜索
            self.role_management.search_role(search_role['search_name'])

            # 获取搜索结果
            num = int(self.role_management.get_search_result_num())
            role_name = self.role_management.get_search_result_all()

            # 数据库查询搜索结果
            role_name_by_sql = self.role_management.get_search_result_rolename_by_sql(search_role['account'],search_role['search_name'])
            num_by_sql = self.role_management.get_search_result_num_by_sql(search_role['account'], search_role['search_name'])

            # 验证搜索结果是否一致
            self.assertEqual(num, num_by_sql)
            self.assertEqual(set(role_name), set(role_name_by_sql))

            # 跳出外层frame
            self.role_management.switch_to_default_content()


            # 退出登录
            self.user_center.logout()

        csv_file.close()


