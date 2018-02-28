from time import sleep
import requests

from automate_driver.automate_driver import AutomateDriver
from automate_driver.automate_driver_server import AutomateDriverServer
from pages.base.base_page import BasePage
from model.connect_sql import ConnectSql

# 贷款客户录入的元素及操作
# author:孙燕妮
from pages.base.base_page_server import BasePageServer


class OperationLog(BasePage):
    def __init__(self, driver: AutomateDriver, base_url):
        super().__init__(driver, base_url)


    # 点击设置
    def click_setup(self):
        self.driver.click_element('x,/html/body/div[2]/div[2]/div/ul/li[6]/a')
        self.driver.wait()


    # 点击进入操作日志
    def click_operation_log(self):
        self.driver.click_element('x,/html/body/div[2]/div[2]/div/ul/li[6]/dl/dd[3]/a')
        self.driver.wait()


    # 切入myframe
    def switch_to_myframe(self):
        self.driver.switch_to_iframe('myframe')
        self.driver.wait()

    # 跳出myframe
    def switch_default(self):
        self.driver.default_frame()
        self.driver.wait()


    # 点击设备分配记录
    def click_dev_assign_log(self):
        self.driver.click_element('x,/html/body/div[1]/div/div/ul/li[1]')
        self.driver.wait()

    # 设备分配记录-选择时间
    def dev_assign_choose_time(self, time):
        self.driver.click_element('x,/html/body/div[1]/div/div/div/div[1]/form/div/div[1]/div/div/input')
        self.driver.wait(1)
        if time == '今天':
            self.driver.click_element('x,/html/body/div[1]/div/div/div/div[1]/form/div/div[1]/div/dl/dd[1]')
        elif time == '昨天':
            self.driver.click_element('x,/html/body/div[1]/div/div/div/div[1]/form/div/div[1]/div/dl/dd[2]')
        elif time == '本周':
            self.driver.click_element('x,/html/body/div[1]/div/div/div/div[1]/form/div/div[1]/div/dl/dd[3]')
        elif time == '上周':
            self.driver.click_element('x,/html/body/div[1]/div/div/div/div[1]/form/div/div[1]/div/dl/dd[4]')
        elif time == '本月':
            self.driver.click_element('x,/html/body/div[1]/div/div/div/div[1]/form/div/div[1]/div/dl/dd[5]')
        elif time == '上月':
            self.driver.click_element('x,/html/body/div[1]/div/div/div/div[1]/form/div/div[1]/div/dl/dd[6]')
        elif time == '自定义':
            self.driver.click_element('x,/html/body/div[1]/div/div/div/div[1]/form/div/div[1]/div/dl/dd[7]')
        self.driver.wait(1)


    # 设备分配记录-时间段输入
    def dev_assign_input_time(self,start_time,end_time):
        self.driver.click_element('startTimeByBusines')
        self.driver.wait(1)
        # 清空
        self.driver.click_element('x,/html/body/div[3]/div[2]/div/span[1]')
        self.driver.wait(1)
        # 输入开始时间
        self.driver.operate_input_element('startTimeByBusines', start_time)
        self.driver.wait(1)

        self.driver.click_element('endTimeByBusines')
        self.driver.wait(1)
        # 清空
        self.driver.click_element('x,/html/body/div[3]/div[2]/div/span[1]')
        self.driver.wait(1)
        # 输入结束时间
        self.driver.operate_input_element('endTimeByBusines', end_time)
        self.driver.wait(1)


    # 设备分配记录-选择类型
    def dev_assign_choose_type(self, type):
        self.driver.click_element('x,/html/body/div[1]/div/div/div/div[1]/form/div/div[4]/div/div/input')
        self.driver.wait(1)
        if type == '全部类型':
            self.driver.click_element('x,/html/body/div[1]/div/div/div/div[1]/form/div/div[4]/div/dl/dd[1]')
        elif type == '分配':
            self.driver.click_element('x,/html/body/div[1]/div/div/div/div[1]/form/div/div[4]/div/dl/dd[2]')
        elif type == '接收':
            self.driver.click_element('x,/html/body/div[1]/div/div/div/div[1]/form/div/div[4]/div/dl/dd[3]')
        self.driver.wait(1)

    # 设备分配记录-输入公司部门名称
    def dev_assign_input_org_name(self, name):
        self.driver.operate_input_element('orgName',name)
        self.driver.wait(1)

    # 设备分配记录-点击搜索
    def dev_assign_click_search(self):
        self.driver.click_element('queryBusinesLog')
        self.driver.wait()


    # 设备分配记录-点击重置
    def dev_assign_click_reset(self):
        self.driver.click_element('resetBusinesLog')
        self.driver.wait()


    # 获取设备分配记录搜索结果
    def get_business_log_search_result(self):
        text = self.driver.get_element('c,layui-laypage-count').text
        count = (str(text).split(sep=' ')[1]).split(sep=' ')[0]
        return count


    # 查询数据库-获取设备分配记录
    def get_business_log_search_result_by_sql(self,user_account,start_time,end_time):
        connect_sql = ConnectSql()
        connect = connect_sql.connect_risk_sql()
        cursor = connect.cursor()
        sql_01 = "SELECT id FROM `system_user_info` WHERE loginUser = '%s';" % user_account
        cursor.execute(sql_01)
        userid = cursor.fetchall()[0][0]
        print(userid)
        sql_02 = "SELECT * FROM `busines_log` WHERE createUserId = '" + str(id) + "' AND createTime >= '" + start_time + "' AND " \
                 "createTime <= '" + end_time + "' ORDER BY createTime DESC;"
        cursor.execute(sql_02)
        data = cursor.fetchall()
        num = len(data)
        cursor.close()
        connect.close()
        return num


    # 点击登录记录
    def click_login_log(self):
        self.driver.click_element('x,/html/body/div[1]/div/div/ul/li[2]')
        self.driver.wait(1)


    # 登录记录-选择时间
    def login_choose_time(self, time):
        self.driver.click_element('x,/html/body/div[1]/div/div/div/div[2]/form/div/div[1]/div/div/input')
        self.driver.wait(1)
        if time == '今天':
            self.driver.click_element('x,/html/body/div[1]/div/div/div/div[2]/form/div/div[1]/div/dl/dd[1]')
        elif time == '昨天':
            self.driver.click_element('x,/html/body/div[1]/div/div/div/div[2]/form/div/div[1]/div/dl/dd[2]')
        elif time == '本周':
            self.driver.click_element('x,/html/body/div[1]/div/div/div/div[2]/form/div/div[1]/div/dl/dd[3]')
        elif time == '上周':
            self.driver.click_element('x,/html/body/div[1]/div/div/div/div[2]/form/div/div[1]/div/dl/dd[4]')
        elif time == '本月':
            self.driver.click_element('x,/html/body/div[1]/div/div/div/div[2]/form/div/div[1]/div/dl/dd[5]')
        elif time == '上月':
            self.driver.click_element('x,/html/body/div[1]/div/div/div/div[2]/form/div/div[1]/div/dl/dd[6]')
        elif time == '自定义':
            self.driver.click_element('x,/html/body/div[1]/div/div/div/div[2]/form/div/div[1]/div/dl/dd[7]')
        self.driver.wait(1)


    # 登录记录-时间段输入
    def login_input_time(self,start_time,end_time):
        self.driver.click_element('startTimeByLogin')
        self.driver.wait(1)
        # 清空
        self.driver.click_element('x,/html/body/div[3]/div[2]/div/span[1]')
        self.driver.wait(1)
        # 输入开始时间
        self.driver.operate_input_element('startTimeByLogin', start_time)
        self.driver.wait(1)

        self.driver.click_element('endTimeByLogin')
        self.driver.wait(1)
        # 清空
        self.driver.click_element('x,/html/body/div[3]/div[2]/div/span[1]')
        self.driver.wait(1)
        # 输入结束时间
        self.driver.operate_input_element('endTimeByLogin', end_time)
        self.driver.wait(1)


    # 登录记录-输入登录账号
    def login_input_account(self, account):
        self.driver.operate_input_element('loginAccount',account)
        self.driver.wait(1)


    # 登录记录-点击搜索
    def login_click_search(self):
        self.driver.click_element('queryLoginLog')
        self.driver.wait()


    # 登录记录-点击重置
    def login_click_reset(self):
        self.driver.click_element('resetLoginLog')
        self.driver.wait()


    # 获取登录记录搜索结果
    def get_login_log_search_result(self):
        text = self.driver.get_element('c,layui-laypage-count').text
        count = (str(text).split(sep=' ')[1]).split(sep=' ')[0]
        return count


    # 查询数据库-获取登录记录
    def get_login_log_search_result_by_sql(self,user_account,start_time,end_time):
        connect_sql = ConnectSql()
        connect = connect_sql.connect_risk_sql()
        cursor = connect.cursor()
        sql_01 = "SELECT id FROM `system_user_info` WHERE loginUser = '%s';" % user_account
        cursor.execute(sql_01)
        userid = cursor.fetchall()[0][0]
        print(userid)
        sql_02 = "SELECT * FROM `user_login_log` WHERE loginUserId = '" + str(id) + "' AND " \
                 "isSuccess = '1' AND loginTime >= '" + start_time + "' AND loginTime <= '" + end_time + "';"
        cursor.execute(sql_02)
        data = cursor.fetchall()
        num = len(data)
        cursor.close()
        connect.close()
        return num




    # 点击设置逾期车主记录
    def click_credit_log(self):
        self.driver.click_element('x,/html/body/div[1]/div/div/ul/li[3]')
        self.driver.wait(1)


    # 逾期车主记录-选择时间
    def credit_choose_time(self, time):
        self.driver.click_element('x,/html/body/div[1]/div/div/div/div[3]/form/div/div[1]/div/div/input')
        self.driver.wait(1)
        if time == '今天':
            self.driver.click_element('x,/html/body/div[1]/div/div/div/div[3]/form/div/div[1]/div/dl/dd[1]')
        elif time == '昨天':
            self.driver.click_element('x,/html/body/div[1]/div/div/div/div[3]/form/div/div[1]/div/dl/dd[2]')
        elif time == '本周':
            self.driver.click_element('x,/html/body/div[1]/div/div/div/div[3]/form/div/div[1]/div/dl/dd[3]')
        elif time == '上周':
            self.driver.click_element('x,/html/body/div[1]/div/div/div/div[3]/form/div/div[1]/div/dl/dd[4]')
        elif time == '本月':
            self.driver.click_element('x,/html/body/div[1]/div/div/div/div[3]/form/div/div[1]/div/dl/dd[5]')
        elif time == '上月':
            self.driver.click_element('x,/html/body/div[1]/div/div/div/div[3]/form/div/div[1]/div/dl/dd[6]')
        elif time == '自定义':
            self.driver.click_element('x,/html/body/div[1]/div/div/div/div[3]/form/div/div[1]/div/dl/dd[7]')
        self.driver.wait(1)


    # 逾期车主记录-时间段输入
    def credit_input_time(self,start_time,end_time):
        self.driver.click_element('startTimeByCredit')
        self.driver.wait(1)
        # 清空
        self.driver.click_element('x,/html/body/div[3]/div[2]/div/span[1]')
        self.driver.wait(1)
        # 输入开始时间
        self.driver.operate_input_element('startTimeByCredit', start_time)
        self.driver.wait(1)

        self.driver.click_element('endTimeByCredit')
        self.driver.wait(1)
        # 清空
        self.driver.click_element('x,/html/body/div[3]/div[2]/div/span[1]')
        self.driver.wait(1)
        # 输入结束时间
        self.driver.operate_input_element('endTimeByCredit', end_time)
        self.driver.wait(1)




    # 逾期车主记录-点击搜索
    def credit_click_search(self):
        self.driver.click_element('queryCredit')
        self.driver.wait()


    # 逾期车主记录-点击重置
    def credit_click_reset(self):
        self.driver.click_element('resetCreditLog')
        self.driver.wait()


    # 获取车主记录搜索结果
    def get_credit_log_search_result(self):
        text = self.driver.get_element('c,layui-laypage-count').text
        count = (str(text).split(sep=' ')[1]).split(sep=' ')[0]
        return count


    # 查询数据库-获取车主记录
    def get_credit_log_search_result_by_sql(self,user_account,start_time,end_time):
        connect_sql = ConnectSql()
        connect = connect_sql.connect_risk_sql()
        cursor = connect.cursor()
        sql_01 = "SELECT id FROM `system_user_info` WHERE loginUser = '%s';" % user_account
        cursor.execute(sql_01)
        userid = cursor.fetchall()[0][0]
        print(userid)
        sql_02 = "SELECT * FROM `customer_credit_log` WHERE createUserId = '" + str(id) + "' AND " \
                 "createTime >= '" + start_time + "' AND createTime <= '" + end_time + "';"
        cursor.execute(sql_02)
        data = cursor.fetchall()
        num = len(data)
        cursor.close()
        connect.close()
        return num




    # 点击设置账号管理记录
    def click_account_log(self):
        self.driver.click_element('x,/html/body/div[1]/div/div/ul/li[4]')
        self.driver.wait(1)



    # 账号管理记录-时间段输入
    def account_input_time(self,start_time,end_time):
        self.driver.click_element('startTimeByAccountOperation')
        self.driver.wait(1)
        # 清空
        self.driver.click_element('x,/html/body/div[3]/div[2]/div/span[1]')
        self.driver.wait(1)
        # 输入开始时间
        self.driver.operate_input_element('startTimeByAccountOperation',start_time)
        self.driver.wait(1)

        self.driver.click_element('endTimeByAccountOperation')
        self.driver.wait(1)
        # 清空
        self.driver.click_element('x,/html/body/div[3]/div[2]/div/span[1]')
        self.driver.wait(1)
        # 输入结束时间
        self.driver.operate_input_element('endTimeByAccountOperation', end_time)
        self.driver.wait(1)


    # 账号管理记录-选择类型
    def account_choose_type(self, type):
        self.driver.click_element('x,/html/body/div[1]/div/div/div/div[4]/form/div/div[4]/div/div/input')
        self.driver.wait(1)
        if type == '全部类型':
            self.driver.click_element('x,/html/body/div[1]/div/div/div/div[4]/form/div/div[4]/div/dl/dd[1]')
        elif type == '新增':
            self.driver.click_element('x,/html/body/div[1]/div/div/div/div[4]/form/div/div[4]/div/dl/dd[2]')
        elif type == '修改':
            self.driver.click_element('x,/html/body/div[1]/div/div/div/div[4]/form/div/div[4]/div/dl/dd[3]')
        elif type == '删除':
            self.driver.click_element('x,/html/body/div[1]/div/div/div/div[4]/form/div/div[4]/div/dl/dd[4]')
        self.driver.wait(1)


    # 账号管理记录-点击搜索
    def account_click_search(self):
        self.driver.click_element('queryAccountOperationLog')
        self.driver.wait()


    # 账号管理记录-点击重置
    def account_click_reset(self):
        self.driver.click_element('resetAccountOperation')
        self.driver.wait()


    # 获取账号管理记录搜索结果
    def get_account_log_search_result(self):
        text = self.driver.get_element('c,layui-laypage-count').text
        count = (str(text).split(sep=' ')[1]).split(sep=' ')[0]
        return count


    # 查询数据库-获取账号管理记录
    def get_account_log_search_result_by_sql(self,user_account,start_time,end_time):
        connect_sql = ConnectSql()
        connect = connect_sql.connect_risk_sql()
        cursor = connect.cursor()
        sql_01 = "SELECT id FROM `system_user_info` WHERE loginUser = '%s';" % user_account
        cursor.execute(sql_01)
        userid = cursor.fetchall()[0][0]
        print(userid)
        sql_02 = "SELECT * FROM `account_operation_log` WHERE createUserId = '" + str(id) + "' AND " \
                 "createTime >= '" + start_time + "' AND createTime <= '" + end_time + "';"
        cursor.execute(sql_02)
        data = cursor.fetchall()
        num = len(data)
        cursor.close()
        connect.close()
        return num






    # 点击公司部门管理记录
    def click_org_log(self):
        self.driver.click_element('x,/html/body/div[1]/div/div/ul/li[5]')
        self.driver.wait(1)



    # 公司部门管理记录-时间段输入
    def org_input_time(self,start_time,end_time):
        self.driver.click_element('startTimeByOrgOperation')
        self.driver.wait(1)
        # 清空
        self.driver.click_element('x,/html/body/div[3]/div[2]/div/span[1]')
        self.driver.wait(1)
        # 输入开始时间
        self.driver.operate_input_element('startTimeByOrgOperation',start_time)
        self.driver.wait(1)

        self.driver.click_element('endTimeByOrgOperation')
        self.driver.wait(1)
        # 清空
        self.driver.click_element('x,/html/body/div[3]/div[2]/div/span[1]')
        self.driver.wait(1)
        # 输入结束时间
        self.driver.operate_input_element('endTimeByOrgOperation', end_time)
        self.driver.wait(1)


    # 公司部门管理记录-选择类型
    def org_choose_type(self, type):
        self.driver.click_element('x,/html/body/div[1]/div/div/div/div[5]/form/div/div[4]/div/div/input')
        self.driver.wait(1)
        if type == '全部类型':
            self.driver.click_element('x,/html/body/div[1]/div/div/div/div[5]/form/div/div[4]/div/dl/dd[1]')
        elif type == '新增':
            self.driver.click_element('x,/html/body/div[1]/div/div/div/div[5]/form/div/div[4]/div/dl/dd[2]')
        elif type == '修改':
            self.driver.click_element('x,/html/body/div[1]/div/div/div/div[5]/form/div/div[4]/div/dl/dd[3]')
        elif type == '删除':
            self.driver.click_element('x,/html/body/div[1]/div/div/div/div[5]/form/div/div[4]/div/dl/dd[4]')
        self.driver.wait(1)


    # 公司部门管理记录-点击搜索
    def org_click_search(self):
        self.driver.click_element('queryOrgOperationLog')
        self.driver.wait()


    # 公司部门管理记录-点击重置
    def org_click_reset(self):
        self.driver.click_element('resetOrgOperation')
        self.driver.wait()



    # 获取公司部门管理记录搜索结果
    def get_org_log_search_result(self):
        text = self.driver.get_element('c,layui-laypage-count').text
        count = (str(text).split(sep=' ')[1]).split(sep=' ')[0]
        return count


    # 查询数据库-获取公司部门管理记录
    def get_org_log_search_result_by_sql(self,user_account,start_time,end_time):
        connect_sql = ConnectSql()
        connect = connect_sql.connect_risk_sql()
        cursor = connect.cursor()
        sql_01 = "SELECT id FROM `system_user_info` WHERE loginUser = '%s';" % user_account
        cursor.execute(sql_01)
        userid = cursor.fetchall()[0][0]
        print(userid)
        sql_02 = "SELECT * FROM `org_operation_log` WHERE createUserId = '" + str(id) + "' AND " \
                 "createTime >= '" + start_time + "' AND createTime <= '" + end_time + "';"
        cursor.execute(sql_02)
        data = cursor.fetchall()
        num = len(data)
        cursor.close()
        connect.close()
        return num






