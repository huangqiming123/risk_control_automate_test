import csv
import unittest
from time import sleep
from automate_driver.automate_driver import AutomateDriver
from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage
from pages.login.log_in_page_read_csv import LogInPageReadCsv
from pages.login.login_page import LoginPage
from pages.user_center.user_center import UserCenter
from pages.user_center.user_center_read_csv import UserCenterReadCsv



class TestCase01UserCenterModifyInfo(unittest.TestCase):
    # 测试个人中心修改资料
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.user_center = UserCenter(self.driver, self.base_url)
        self.log_in_page_read_csv = LogInPageReadCsv()
        self.user_center_read_csv = UserCenterReadCsv()
        self.driver.set_window_max()
        self.connect_sql = ConnectSql()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)



    def tearDown(self):
        self.driver.quit_browser()

    def test_user_center_modify_info(self):
        # 通过csv测试修改资料功能

        csv_file = self.user_center_read_csv.read_csv('user_to_modify_info.csv')
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            user_to_modify_info = {
                "username": row[0],
                "phone": row[1],
            }

            # 打开风控首页-登录页
            self.base_page.open_page()
            sleep(1)
            # 登录账号
            self.login_page.test_user_login()
            # 获取当前登录账号
            log_in_account = self.user_center.get_login_account()
            print(log_in_account)

            # 从数据库获取登录账号的客户名称、电话
            account_info = self.user_center.get_account_info_by_sql(log_in_account)
            print(account_info)

            # 获取修改资料里面的信息
            user_info = self.user_center.get_user_info()

            # 断言
            self.assertEqual(log_in_account, user_info['login_account'])
            self.assertEqual(account_info[1], user_info['name'])
            self.assertEqual(account_info[2], user_info['tel'])



            # 编辑客户名称、电话后点击取消
            self.user_center.edit_user_info_not_save(user_to_modify_info['username'],user_to_modify_info['phone'])
            # 从数据库获取登录账号的客户名称、电话
            account_info1 = self.user_center.get_account_info_by_sql(log_in_account)
            print(account_info1)
            self.assertEqual(account_info, account_info1)

            # 获取修改资料里面的信息
            user_info1 = self.user_center.get_user_info()

            # 断言
            self.assertEqual(log_in_account, user_info1['login_account'])
            self.assertEqual(account_info1[1], user_info1['name'])
            self.assertEqual(account_info1[2], user_info1['tel'])



            # 编辑客户名称、电话后点击关闭按钮
            self.user_center.edit_user_info_close(user_to_modify_info['username'],user_to_modify_info['phone'])
            # 从数据库获取登录账号的客户名称、电话
            account_info2 = self.user_center.get_account_info_by_sql(log_in_account)
            print(account_info2)
            self.assertEqual(account_info, account_info2)

            # 获取修改资料里面的信息
            user_info2 = self.user_center.get_user_info()

            # 断言
            self.assertEqual(log_in_account, user_info2['login_account'])
            self.assertEqual(account_info2[1], user_info2['name'])
            self.assertEqual(account_info2[2], user_info2['tel'])



            # 编辑客户名称、电话后保存
            print(user_to_modify_info['username'],user_to_modify_info['phone'])
            self.user_center.edit_user_info_exception(user_to_modify_info['username'], user_to_modify_info['phone'])
            # 从数据库获取登录账号的客户名称、电话
            account_info3 = self.user_center.get_account_info_by_sql(log_in_account)
            print(account_info3)
            web_data = [log_in_account,user_to_modify_info['username'], user_to_modify_info['phone']]
            self.assertEqual(account_info3, web_data)

            # 获取修改资料里面的信息
            user_info3 = self.user_center.get_user_info()

            # 断言
            self.assertEqual(log_in_account, user_info3['login_account'])
            self.assertEqual(account_info3[1], user_info3['name'])
            self.assertEqual(account_info3[2], user_info3['tel'])



            # 退出登录
            self.user_center.logout()


        csv_file.close()


