import csv
import unittest
from time import sleep
from automate_driver.automate_driver import AutomateDriver
from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage
from pages.loan_customer.loan_customer import LoanCustomer
from pages.loan_customer.loan_customer_read_csv import LoanCustomerReadCsv
from pages.login.log_in_page_read_csv import LogInPageReadCsv
from pages.login.login_page import LoginPage
from pages.user_center.user_center import UserCenter
from pages.user_center.user_center_read_csv import UserCenterReadCsv



class TestCase01LoanCustomerInput(unittest.TestCase):
    # 贷款客户信息录入
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.user_center = UserCenter(self.driver, self.base_url)
        self.loan_customer = LoanCustomer(self.driver, self.base_url)
        self.log_in_page_read_csv = LogInPageReadCsv()
        self.user_center_read_csv = UserCenterReadCsv()
        self.loan_customer_read_csv = LoanCustomerReadCsv()
        self.driver.set_window_max()
        self.connect_sql = ConnectSql()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)



    def tearDown(self):
        self.driver.quit_browser()

    def test_user_center_modify_info(self):
        # 通过csv测试贷款客户信息录入


        csv_file = self.loan_customer_read_csv.read_csv('loan_customer_input_info.csv')
        csv_data = csv.reader(csv_file)
        for row in csv_data:
            loan_customer_input_info = {
                "name": row[0],
                "tel": row[1],
                "type": row[2],
                "ID": row[3],
                "sex": row[4],
                "com": row[5],
                "car_num": row[6],
                "model": row[7],
                "engi_num": row[8],
                "frame_num": row[9],
                "car_type": row[10],
                "loan_money": row[11],
                "loan_deadline": row[12],
                "current_balance": row[13],
                "pay_type": row[14],
                "pay_date": row[15],
                "contract_number": row[16],
                "imei": row[17],
                "install_address": row[18],
                "install_person": row[19],
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


            # 点击进入贷款客户录入
            self.loan_customer.click_loan_customer_input()

            # 切入外层frame
            self.loan_customer.switch_to_1_frame()

            # 录入车主信息
            # 录入车主姓名
            self.loan_customer.input_owner_name(loan_customer_input_info['name'])

            # 录入车主电话
            self.loan_customer.input_owner_tel(loan_customer_input_info['tel'])

            # 选择车主证件类型
            self.loan_customer.choose_owner_ID_type(loan_customer_input_info['type'])

            # 输入车主证件号
            self.loan_customer.input_owner_ID(loan_customer_input_info['ID'])

            # 选择车主性别
            self.loan_customer.choose_owner_sex(loan_customer_input_info['sex'])

            # 选择车主贷款单位
            self.loan_customer.choose_owner_loan_com(loan_customer_input_info['com'])

            # 保存
            self.loan_customer.save_owner_info()

            # 验证是否保存成功


            # 录入车辆信息
            # 输入车牌号
            self.loan_customer.input_car_num(loan_customer_input_info['car_num'])

            # 输入车型
            self.loan_customer.input_car_model(loan_customer_input_info['model'])

            # 输入发动机号
            self.loan_customer.input_car_engi_num(loan_customer_input_info['engi_num'])

            # 输入车架号
            self.loan_customer.input_car_frame_num(loan_customer_input_info['frame_num'])

            # 选择车辆类型
            self.loan_customer.choose_car_type(loan_customer_input_info['car_type'])


            # 保存车辆信息
            self.loan_customer.save_car_info()

            # 验证是否保存成功


            # 录入贷款信息
            # 输入贷款日期
            self.loan_customer.input_loan_date()

            # 输入贷款金额
            self.loan_customer.input_loan_money(loan_customer_input_info['loan_money'])

            # 输入贷款期限
            self.loan_customer.input_loan_deadline(loan_customer_input_info['loan_deadline'])

            # 输入应还金额
            self.loan_customer.input_current_balance(loan_customer_input_info['current_balance'])

            # 选择还款方式
            self.loan_customer.choose_pay_type(loan_customer_input_info['pay_type'])

            # 选择还款日
            self.loan_customer.choose_pay_date(loan_customer_input_info['pay_date'])

            # 输入合同编号
            self.loan_customer.input_contract_number(loan_customer_input_info['contract_number'])

            # 保存贷款信息
            self.loan_customer.save_loan_info()

            # 验证是否保存成功


            # 录入安装设备
            # 点击安装设备
            self.loan_customer.click_install_dev()


            # 输入Imei
            self.loan_customer.input_dev_imei(loan_customer_input_info['imei'])

            # 选择安装时间
            self.loan_customer.choose_install_time()

            # 输入安装地址
            self.loan_customer.input_install_address(loan_customer_input_info['install_address'])

            # 输入安装人员
            self.loan_customer.input_install_person(loan_customer_input_info['install_person'])

            # 保存安装信息
            self.loan_customer.save_install_info()

            # 跳出frame1
            self.loan_customer.switch_out_frame1()

            # 验证是否保存成功



            # 退出登录
            self.user_center.logout()


        csv_file.close()


