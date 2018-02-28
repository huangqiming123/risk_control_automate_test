import csv
import unittest
import requests
from time import sleep
from automate_driver.automate_driver import AutomateDriver
from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage
from pages.loan_customer.loan_customer import LoanCustomer
from pages.loan_customer.loan_customer_read_csv import LoanCustomerReadCsv
from pages.login.log_in_page_read_csv import LogInPageReadCsv
from pages.login.login_page import LoginPage
from pages.statistics_report.statistics_report import StatisticsReport
from pages.statistics_report.statistics_report_read_csv import StatisticsReportReadCsv
from pages.user_center.user_center import UserCenter
from pages.user_center.user_center_read_csv import UserCenterReadCsv



class TestCase01LowPowerReport(unittest.TestCase):
    # 电量过低统计
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.user_center = UserCenter(self.driver, self.base_url)
        self.statistics_report = StatisticsReport(self.driver, self.base_url)
        self.log_in_page_read_csv = LogInPageReadCsv()
        self.user_center_read_csv = UserCenterReadCsv()
        self.statistics_report_read_csv = StatisticsReportReadCsv()
        self.driver.set_window_max()
        self.connect_sql = ConnectSql()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)



    def tearDown(self):
        self.driver.quit_browser()

    def test_low_power_report(self):
        # 测试电量过低统计


        # 打开风控首页-登录页
        self.base_page.open_page()
        sleep(1)
        # 登录账号
        self.login_page.test_statistics_login_user_normal()
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

        # 点击统计报表
        self.statistics_report.click_statistics_report()

        # 点击进入电量过低报表
        self.statistics_report.click_low_power_report()

        # 切入frame
        self.statistics_report.switch_to_myframe()


        csv_file = self.statistics_report_read_csv.read_csv('low_power.csv')
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            low_power = {
                "power": row[0],
            }



            # 勾选包含下级复选框
            self.statistics_report.check_contain_lower()

            # 勾选包含已经还清车辆
            self.statistics_report.check_contain_paid()

            # 选择电量
            self.statistics_report.choose_low_power(low_power['power'])

            # 点击搜索
            self.statistics_report.click_power_search()

            # 获取搜索结果
            result_info = self.statistics_report.get_power_search_result()
            print(result_info)


            # 获取接口请求结果
            # 请求的url
            get_url = self.base_page.api_url_normal() + 'getBatteryLeft'

            # 请求参数
            payload = {
                'currentUser': '1,182,',
                'childUserFlag': '1',
                'RSOC': '100.00',
                'userIds': '182',
            }

            # 发送请求
            r = requests.post(get_url, params=payload)

            # 获取响应的文本
            response_text = r.json()
            print(response_text)

            info = self.statistics_report.get_power_search_result_by_api(response_text)


            # 验证搜索结果是否一致
            self.assertEqual(result_info,info)



        # 跳出frame
        self.statistics_report.switch_default()

        # 退出登录
        self.user_center.logout()




