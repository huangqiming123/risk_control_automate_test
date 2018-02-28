import csv
import unittest
from time import sleep
from automate_driver.automate_driver import AutomateDriver
from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage
from pages.login.log_in_page_read_csv import LogInPageReadCsv
from pages.login.login_page import LoginPage
from pages.operation_log.operation_log import OperationLog
from pages.operation_log.operation_log_read_csv import OperationLogReadCsv
from pages.user_center.user_center import UserCenter
from pages.user_center.user_center_read_csv import UserCenterReadCsv



class TestCase01DevAssignLog(unittest.TestCase):
    # 设备分配记录
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.user_center = UserCenter(self.driver, self.base_url)
        self.operation_log = OperationLog(self.driver, self.base_url)
        self.log_in_page_read_csv = LogInPageReadCsv()
        self.user_center_read_csv = UserCenterReadCsv()
        self.operation_log_read_csv = OperationLogReadCsv()
        self.driver.set_window_max()
        self.connect_sql = ConnectSql()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)



    def tearDown(self):
        self.driver.quit_browser()

    def test_dev_assign_log(self):
        # 测试设备分配记录


        # 打开风控首页-登录页
        self.base_page.open_page()
        sleep(1)
        # 登录账号
        self.login_page.test_log_login_user_normal()
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

        # 点击设置
        self.operation_log.click_setup()

        # 点击进入操作日志
        self.operation_log.click_operation_log()


        # 切入frame
        self.operation_log.switch_to_myframe()

        # 点击设备分配记录
        self.operation_log.click_dev_assign_log()


        csv_file = self.operation_log_read_csv.read_csv('dev_assign_log.csv')
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            dev_assign_log = {
                "time": row[0],
                "start_time": row[1],
                "end_time": row[2],
                "type": row[3],
                "name": row[4],
            }



            # 选择时间
            self.operation_log.dev_assign_choose_time(dev_assign_log['time'])


            # 输入时间段
            self.operation_log.dev_assign_input_time(dev_assign_log['start_time'],dev_assign_log['end_time'])

            # 选择类型
            self.operation_log.dev_assign_choose_type(dev_assign_log['type'])

            # 输入公司部门名称
            self.operation_log.dev_assign_input_org_name(dev_assign_log['name'])

            # 点击搜索
            self.operation_log.dev_assign_click_search()

            '''# 获取搜索结果
            result_info = self.operation_log.get_business_log_search_result()
            print(result_info)


            # 获取数据库查询结果
            info = self.operation_log.get_business_log_search_result_by_sql(log_in_account,dev_assign_log['start_time'],dev_assign_log['end_time'])


            # 验证搜索结果是否一致
            self.assertEqual(result_info,info)'''

            # 点击重置
            self.operation_log.dev_assign_click_reset()



        # 跳出frame
        self.operation_log.switch_default()

        # 退出登录
        self.user_center.logout()




