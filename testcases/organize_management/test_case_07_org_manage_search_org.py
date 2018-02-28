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



class TestCase07OrgManageSearchOrg(unittest.TestCase):
    # 测试部门管理搜索公司部门
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

    def test_search_org(self):
        # 通过csv测试搜索公司部门功能

        csv_file = self.user_center_read_csv.read_csv('search_org.csv')
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            search_org = {
                "account": row[0],
                "password": row[1],
                "key": row[2],
            }

            # 打开风控首页-登录页
            self.base_page.open_page()
            sleep(1)
            # 登录账号
            self.login_page.user_login(search_org['account'],search_org['password'])

            # 判断登录成功后招呼栏的用户名是否正确
            username = self.user_center.get_username()

            # 从数据库获取登录账号的用户名
            account_info = self.user_center.get_account_info_by_sql(search_org['account'])
            print(account_info)
            account_name = account_info[1]

            self.assertEqual(account_name, username, '登录成功后招呼栏的用户名错误')


            # 点击进入部门管理
            self.organize_management.click_org_manage()

            # 输入搜索关键词进行搜索
            self.organize_management.search_org(search_org['key'])

            # 获取搜索结果
            num = int(self.organize_management.get_search_result_num())
            org_name = self.organize_management.get_search_result_all()


            # 数据库查询搜索结果
            org_name_by_sql = self.organize_management.get_search_result_orgname_by_sql(search_org['account'],search_org['key'])
            num_by_sql = self.organize_management.get_search_result_num_by_sql(search_org['account'],search_org['key'])


            # 验证搜索结果是否一致
            self.assertEqual(num,num_by_sql)
            self.assertEqual(set(org_name),set(org_name_by_sql))

            # 跳出外层frame
            self.organize_management.switch_to_default_content()

            # 退出登录
            self.user_center.logout()

        csv_file.close()


