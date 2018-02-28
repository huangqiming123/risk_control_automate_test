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


class TestCase06UserCenterFeedback(unittest.TestCase):
    # 测试用户中心意见反馈
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.user_center = UserCenter(self.driver, self.base_url)
        self.user_center_read_csv = UserCenterReadCsv()
        self.driver.set_window_max()
        self.connect_sql = ConnectSql()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

    def tearDown(self):
        self.driver.quit_browser()

    def test_user_center_feedback(self):
        '''通过csv测试用户中心意见反馈功能'''
        data = ["部门管理", "设备", "贷款客户", "车辆监控中心", "统计报表", "设置"]

        csv_file = self.user_center_read_csv.read_csv('user_feedback_info.csv')
        csv_data = csv.reader(csv_file)

        for row in csv_data:
            user_feedback_info = {
                "account": row[0],
                "passwd": row[1],
                "type": row[2],
                "content": row[3],
                "linkman": row[4],
                "phone": row[5],
            }

            # 打开风控首页-登录页
            self.base_page.open_page()
            # 输入用户信息进行登录
            self.login_page.user_login(user_feedback_info["account"], user_feedback_info["passwd"])
            self.driver.wait(1)

            # 判断登录成功后招呼栏的用户名是否正确
            username = self.user_center.get_username()

            # 从数据库获取登录账号的用户名
            account_info = self.user_center.get_account_info_by_sql(user_feedback_info['account'])
            print(account_info)
            account_name = account_info[1]

            self.assertEqual(account_name, username, '登录成功后招呼栏的用户名错误')

            # 验证模块
            module = self.user_center.get_module_name()
            print(module)
            self.assertEqual(data, module, "用户账号登录，模块显示错误")

            self.driver.wait(10)

            # 进入意见反馈
            self.user_center.click_feedback()

            # 提交反馈信息
            self.user_center.choose_problem_type(user_feedback_info['type'])
            self.user_center.input_problem_content(user_feedback_info['content'])
            self.user_center.input_linkman(user_feedback_info['linkman'])
            self.user_center.input_phone(user_feedback_info['phone'])
            self.user_center.click_submit()

            # 获取提交反馈信息成功提示语
            text = self.user_center.get_feedback_success_text()
            self.assertEqual('意见反馈成功',text)

            # 从数据库获取反馈信息验证是否提交成功
            feedback_info = self.user_center.get_feedback_info_by_sql(user_feedback_info['account'])
            print(feedback_info)

            self.assertEqual(user_feedback_info['account'],feedback_info[0])
            self.assertEqual(user_feedback_info['type'],feedback_info[1])
            self.assertEqual(user_feedback_info['content'], feedback_info[2])
            self.assertEqual(user_feedback_info['linkman'], feedback_info[3])
            self.assertEqual(user_feedback_info['phone'], feedback_info[4])


            # # 成功退出系统
            sleep(2)
            self.user_center.logout()

        csv_file.close()
