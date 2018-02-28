from time import sleep
import requests

from automate_driver.automate_driver import AutomateDriver
from automate_driver.automate_driver_server import AutomateDriverServer
from pages.base.base_page import BasePage
from model.connect_sql import ConnectSql

# 贷款客户录入的元素及操作
# author:孙燕妮
from pages.base.base_page_server import BasePageServer


class StatisticsReport(BasePage):
    def __init__(self, driver: AutomateDriver, base_url):
        super().__init__(driver, base_url)


    # 点击统计报表
    def click_statistics_report(self):
        self.driver.click_element('x,/html/body/div[2]/div[2]/div/ul/li[5]/a')
        self.driver.wait()


    # 点击进入电量过低统计报表
    def click_low_power_report(self):
        self.driver.click_element('x,/html/body/div[2]/div[2]/div/ul/li[5]/dl/dd[3]/a')
        self.driver.wait()


    # 切入myframe
    def switch_to_myframe(self):
        self.driver.switch_to_iframe('myframe')
        self.driver.wait()

    # 跳出myframe
    def switch_default(self):
        self.driver.default_frame()
        self.driver.wait()


    # 低电量报表-选择公司/部门
    def choose_org(self,key):
        self.driver.click_element('org-option-btn')
        self.driver.wait(1)
        self.driver.operate_input_element('org-search-key',key)
        self.driver.wait(1)
        self.driver.click_element('selectOrgBtn')
        self.driver.wait(1)
        self.driver.click_element('x,/html/body/div/form/div[1]/div[1]/div[3]/div/div/ul/li/a/span[2]')
        self.driver.click_element('org-option-btn')
        self.driver.wait()

    # 低电量报表-选择电量低于x%
    def choose_low_power(self,power):
        self.driver.click_element('x，/html/body/div/form/div[2]/div[2]/div/div/input')
        self.driver.wait(1)
        if power == '10%':
            self.driver.click_element('x,/html/body/div/form/div[2]/div[2]/div/dl/dd[1]')
        elif power == '20%':
            self.driver.click_element('x,/html/body/div/form/div[2]/div[2]/div/dl/dd[2]')
        elif power == '30%':
            self.driver.click_element('x,/html/body/div/form/div[2]/div[2]/div/dl/dd[3]')
        elif power == '40%':
            self.driver.click_element('x,/html/body/div/form/div[2]/div[2]/div/dl/dd[4]')
        elif power == '50%':
            self.driver.click_element('x,/html/body/div/form/div[2]/div[2]/div/dl/dd[5]')
        elif power == '60%':
            self.driver.click_element('x,/html/body/div/form/div[2]/div[2]/div/dl/dd[6]')
        elif power == '70%':
            self.driver.click_element('x,/html/body/div/form/div[2]/div[2]/div/dl/dd[7]')
        elif power == '80%':
            self.driver.click_element('x,/html/body/div/form/div[2]/div[2]/div/dl/dd[8]')
        elif power == '90%':
            self.driver.click_element('x,/html/body/div/form/div[2]/div[2]/div/dl/dd[9]')
        elif power == '100%':
            self.driver.click_element('x,/html/body/div/form/div[2]/div[2]/div/dl/dd[10]')
        self.driver.wait(1)

    # 低电量报表-勾选包含下级复选框
    def check_contain_lower(self):
        self.driver.click_element('x,/html/body/div/form/div[1]/div[2]/div/i')
        self.driver.wait()

    # 低电量报表-勾选包含已还清车辆
    def check_contain_paid(self):
        self.driver.click_element('x,/html/body/div/form/div[1]/div[3]/div/i')
        self.driver.wait()

    # 低电量报表-点击搜索按钮
    def click_power_search(self):
        self.driver.click_element('x,/html/body/div/form/div[2]/div[3]/input')
        self.driver.wait()

    # 低电量报表-点击重置按钮
    def click_power_reset(self):
        self.driver.click_element('x,/html/body/div/form/div[2]/div[4]/button')
        self.driver.wait()

    # 低电量报表-获取搜索结果
    def get_power_search_result(self):
        el = self.driver.get_elements('x,/html/body/div[1]/div/div/div[1]/div[2]/table/tbody/tr[1]')
        result_num = len(el)
        if result_num == 0:
            print("搜索结果为空")
            result_info = []
            return result_info
        else:
            result_info = []
            for i in range(result_num):
                imei = self.driver.get_element('x,/html/body/div[1]/div/div/div[1]/div[2]/table/tbody/tr[' +
                                                  str(i + 1) + ']/td[7]/div').text
                power = self.driver.get_element('x,/html/body/div[1]/div/div/div[1]/div[2]/table/tbody/tr[' +
                                               str(i + 1) + ']/td[8]/div').text
                result_info.append(imei)
                result_info.append(power)
                print(result_info)
            return result_info

    # 低电量报表-查询架构接口获取搜索结果
    def get_power_search_result_by_api(self,response_text):
        result_num = len(response_text['data'])
        if result_num == 0:
            print("搜索结果为空")
            result_info = []
            return result_info
        else:
            result_info = []
            for i in range(result_num):
                imei = response_text['data'][i]['imei']
                power = response_text['data'][i]['rsoc']
                result_info.append(imei)
                result_info.append(power)
                print(result_info)
            return result_info



    # 点击进入逾期还款统计
    def click_loan(self):
        self.driver.click_element('x,/html/body/div[2]/div[2]/div/ul/li[5]/dl/dd[7]/a/cite')
        self.driver.wait()


    # 逾期还款统计-勾选包含下级车主
    def click_contain_lower(self):
        self.driver.click_element('x,/html/body/div/form/div[1]/div[2]/div')
        self.driver.wait(1)

    # 逾期还款统计-选择逾期次数
    def choose_loan_times(self,times):
        self.driver.click_element('x,/html/body/div/form/div[1]/div[3]/div/div/input')
        self.driver.wait(1)
        if times == '全部逾期车主':
            self.driver.click_element('x,/html/body/div/form/div[1]/div[3]/div/dl/dd[1]')
        elif times == '逾期超过一次车主':
            self.driver.click_element('x,/html/body/div/form/div[1]/div[3]/div/dl/dd[2]')
        elif times == '逾期超过两次车主':
            self.driver.click_element('x,/html/body/div/form/div[1]/div[3]/div/dl/dd[3]')
        elif times == '逾期超过三次车主':
            self.driver.click_element('x,/html/body/div/form/div[1]/div[3]/div/dl/dd[4]')
        elif times == '逾期超过四次车主':
            self.driver.click_element('x,/html/body/div/form/div[1]/div[3]/div/dl/dd[5]')
        elif times == '逾期超过五次车主':
            self.driver.click_element('x,/html/body/div/form/div[1]/div[3]/div/dl/dd[6]')
        self.driver.wait(1)


    # 逾期还款统计-点击搜索按钮
    def click_loan_search(self):
        self.driver.click_element('x,/html/body/div/form/div[1]/div[4]/input')
        self.driver.wait()

    # 逾期还款统计-点击重置按钮
    def click_loan_reset(self):
        self.driver.click_element('x,/html/body/div/form/div[1]/div[5]/button')
        self.driver.wait()

    # 逾期还款统计-查询数据库获取搜索结果
    def get_loan_search_result_by_sql(self,user_account):
        connect_sql = ConnectSql()
        connect = connect_sql.connect_risk_sql()
        cursor = connect.cursor()
        sql_01 = "SELECT * FROM `system_user_info` WHERE loginUser = '%s';" % user_account
        cursor.execute(sql_01)
        userid = cursor.fetchall()[0][0]
        print(userid)
        sql_02 = "SELECT imeis,carPlateNumber,carFrameNumber,carEngineNumber,homeAddress,workAddress FROM " \
                 "`customer_car` WHERE carStatus = 'OVERDUE' AND createUserId = '" + str(userid) + "';"
        cursor.execute(sql_02)
        data = cursor.fetchall()
        num = len(data)
        cursor.close()
        connect.close()
        if num == 0:
            print("搜索结果为空")
            result_info = []
            return result_info
        else:
            result_info = []
            for i in range(num):
                imeis = data[i][0]
                carPlateNumber = data[i][1]
                carFrameNumber = data[i][2]
                carEngineNumber = data[i][3]
                homeAddress = data[i][4]
                workAddress = data[i][5]
                result_info.append(imeis)
                result_info.append(carPlateNumber)
                result_info.append(carFrameNumber)
                result_info.append(carEngineNumber)
                result_info.append(homeAddress)
                result_info.append(workAddress)
                print(result_info)
            return result_info



    # 逾期还款统计-获取搜索结果
    def get_loan_search_result(self):
        el = self.driver.get_elements('x,/html/body/div/div/div/div[1]/div[2]/table/tbody/tr')
        result_num = len(el)
        if result_num == 0:
            print("搜索结果为空")
            result_info = []
            return result_info
        else:
            result_info = []
            for i in range(result_num):
                imeis = self.driver.get_element('x,/html/body/div/div/div/div[1]/div[2]/table/tbody/tr[' +
                                                  str(i + 1) + ']/td[4]/div').text
                carPlateNumber = self.driver.get_element('x,/html/body/div/div/div/div[1]/div[2]/table/tbody/tr[' +
                                                  str(i + 1) + ']/td[6]/div').text
                carFrameNumber = self.driver.get_element('x,/html/body/div/div/div/div[1]/div[2]/table/tbody/tr[' +
                                                  str(i + 1) + ']/td[7]/div').text
                carEngineNumber = self.driver.get_element('x,/html/body/div/div/div/div[1]/div[2]/table/tbody/tr[' +
                                                  str(i + 1) + ']/td[8]/div').text
                homeAddress = self.driver.get_element('x,/html/body/div/div/div/div[1]/div[2]/table/tbody/tr[' +
                                                  str(i + 1) + ']/td[12]/div').text
                workAddress = self.driver.get_element('x,/html/body/div/div/div/div[1]/div[2]/table/tbody/tr[' +
                                                  str(i + 1) + ']/td[13]/div').text

                result_info.append(imeis)
                result_info.append(carPlateNumber)
                result_info.append(carFrameNumber)
                result_info.append(carEngineNumber)
                result_info.append(homeAddress)
                result_info.append(workAddress)
                print(result_info)
            return result_info



