from time import sleep

from automate_driver.automate_driver import AutomateDriver
from automate_driver.automate_driver_server import AutomateDriverServer
from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage

# 登录页面的元素及操作
# author:孙燕妮
from pages.base.base_page_server import BasePageServer


class OrganizeManagement(BasePage):
    def __init__(self, driver: AutomateDriver, base_url):
        super().__init__(driver, base_url)


    # 切入外层frame
    def switch_to_1_frame(self):
        self.driver.switch_to_iframe('myframe')
        self.driver.wait()

    # 切入内层frame
    def switch_to_2_frame(self):
        self.driver.switch_to_iframe('x,//iframe[(@scrolling="auto")]')
        self.driver.wait()


    # 跳出内层frame
    def switch_to_parent_content(self):
        self.driver.parent_frame()


    # 跳出最外层frame
    def switch_to_default_content(self):
        # 跳出最外层frame
        self.driver.default_frame()

    # 点击部门管理-部门管理
    def click_org_manage(self):
        self.driver.click_element('x,/html/body/div[2]/div[2]/div/ul/li[1]')
        self.driver.wait(1)
        self.driver.click_element('x,/html/body/div[2]/div[2]/div/ul/li[1]/dl/dd[1]/a')
        self.driver.wait()
        # 切入iframe
        self.driver.switch_to_iframe('myframe')
        self.driver.wait()


    # 点击新增公司部门
    def click_add_org(self):
        self.driver.click_element('x,/html/body/div[1]/div[1]/div[2]/div[1]/button')
        self.driver.wait()

    # 获取新增部门弹框显示的上级部门信息
    def get_sup_org_name(self):
        # 切入内层iframe
        self.driver.switch_to_iframe('x,//iframe[(@scrolling="auto")]')
        self.driver.wait()
        sup_org_name = self.driver.get_element('orgSupName').get_attribute('value')
        return sup_org_name

    # 数据库查询当前登录账户所属部门名称
    def get_user_sup_org_by_sql(self,user_account):
        connect_sql = ConnectSql()
        connect = connect_sql.connect_risk_sql()
        cursor = connect.cursor()
        sql = "SELECT o.orgName FROM `system_user_info` u INNER JOIN `system_org_info` o on u.orgId = o.id WHERE u.loginUser = '%s';" % user_account
        cursor.execute(sql)
        data = cursor.fetchall()[0][0]
        print(data)
        cursor.close()
        connect.close()
        return data


    # 数据库查询当前登录账户部门的所属上级部门名称
    def get_belong_to_superior_org_by_sql(self,user_account):
        connect_sql = ConnectSql()
        connect = connect_sql.connect_risk_sql()
        cursor = connect.cursor()
        sql_01 = "SELECT o.orgSupId FROM `system_user_info` u INNER JOIN `system_org_info` o on u.orgId = o.id WHERE u.loginUser = '%s';" % user_account
        cursor.execute(sql_01)
        orgSupId = cursor.fetchall()[0][0]
        sql_02 = "SELECT orgName FROM `system_org_info` WHERE id = '%s';" % orgSupId
        cursor.execute(sql_02)
        sup_org_name = cursor.fetchall()[0][0]
        print(sup_org_name)
        cursor.close()
        connect.close()
        return sup_org_name


    # 数据库查询当前登录账号所属部门的信息
    def get_current_org_info_by_sql(self,user_account):
        connect_sql = ConnectSql()
        connect = connect_sql.connect_risk_sql()
        cursor = connect.cursor()
        sql = "SELECT o.orgName,o.orgTel FROM `system_user_info` u INNER JOIN system_org_info o ON u.orgId = o.id WHERE u.loginUser = '%s';" % user_account
        cursor.execute(sql)
        data = cursor.fetchall()[0]
        current_org_info = []
        current_org_info.append(data[0])
        current_org_info.append(data[1])
        print(current_org_info)
        cursor.close()
        connect.close()
        return current_org_info


    # 选择上级部门
    def choose_sup_org(self):
        self.driver.click_element('editTree_1_span')
        self.driver.wait(1)

    # 填写新增部门名称
    def input_add_org_name(self,org_name):
        self.driver.operate_input_element('orgName',org_name)
        self.driver.wait(1)


    # 填写新增部门联系方式
    def input_add_org_tel(self,tel):
        self.driver.operate_input_element('orgTel',tel)
        self.driver.wait(1)


    # 新增部门点击保存按钮
    def click_add_org_save(self):
        # 跳出内层frame
        self.driver.parent_frame()
        self.driver.wait()
        self.driver.click_element('c,layui-layer-btn0')
        self.driver.wait()



    # 新增部门点击取消按钮
    def click_add_org_dismiss(self):
        # 跳出内层frame
        self.driver.parent_frame()
        self.driver.click_element('c,layui-layer-btn1')
        self.driver.wait()

    # 新增部门点击关闭按钮
    def click_add_org_close(self):
        # 跳出内层frame
        self.driver.parent_frame()
        self.driver.click_element('c,layui-layer-setwin')
        self.driver.wait()


    # 连接数据库查询新增部门
    def get_add_org_by_sql(self,user_account):
        connect_sql = ConnectSql()
        connect = connect_sql.connect_risk_sql()
        cursor = connect.cursor()
        sql = "SELECT o.orgName FROM  `system_user_info` u INNER JOIN `system_org_info` o ON u.id = o.createUserId WHERE " \
              "u.loginUser = '%s' ORDER BY o.createTime DESC;" % user_account
        cursor.execute(sql)
        data = cursor.fetchall()[0]
        print(data)
        data_01 = data[0]
        print(data_01)
        cursor.close()
        connect.close()
        return data_01


    # 获取新增公司部门输入有误时的异常提醒
    def get_add_org_exception1(self):
        # 切入内层iframe
        self.driver.switch_to_iframe('x,//iframe[(@scrolling="auto")]')
        text = self.driver.get_element('s,div.layui-layer-msg').text
        return text

    # 获取新增公司部门名称已存在时的异常提醒
    def get_add_org_exception2(self):
        text = self.driver.get_element('s,div.layui-layer-msg').text
        return text

    # 查找部门
    def search_org(self,key):
        # 输入搜索关键词
        self.driver.operate_input_element('searchId',key)
        self.driver.wait(1)
        # 点击搜索按钮
        self.driver.click_element('x,//button[@data-type="searchData"]')
        self.driver.wait()

    # 获取搜索结果总条数
    def get_search_result_num(self):
        num_str = str(self.driver.get_element('c,layui-laypage-count').text)
        num = (num_str.split(' ')[1]).split(' ')[0]
        print(num)
        return num

    # 获取所有搜索结果的公司/部门名称
    def get_search_result_all(self):
        org_name = []
        for i in range(len(self.driver.get_elements('x,/html/body/div/div[2]/div/div[1]/div[2]/table/tbody/tr'))):
            org_name.append(self.driver.get_element('x,/html/body/div/div[2]/div/div[1]/div[2]/table/tbody/tr[' + str(i+1) + ']/td[2]').text)
        print(org_name)
        return org_name

    # 获取唯一搜索结果的部门名称
    def get_search_result_one(self):
        org_name = self.driver.get_element('x,//td[@data-field="orgName"]').text
        return org_name

    # 数据库查询部门搜索关键词结果
    def get_search_result_by_sql(self,user_account,key):
        connect_sql = ConnectSql()
        connect = connect_sql.connect_risk_sql()
        cursor = connect.cursor()
        sql_01 = "SELECT orgId FROM `system_user_info` WHERE loginUser = '%s';" % user_account
        cursor.execute(sql_01)
        orgId = cursor.fetchall()[0][0]
        sql_02 = "SELECT orgName,orgSupId,orgTel FROM system_org_info WHERE (id = '" + str(orgId) + "' OR orgSupId = '" + str(orgId) + "') AND " \
                                                                               "orgName LIKE '%" + key + "%';"
        cursor.execute(sql_02)
        data_02 = cursor.fetchall()[0]
        print(data_02)
        orgName = data_02[0]
        orgSupId = data_02[1]
        orgTel = data_02[2]
        sql_03 = "SELECT orgName FROM `system_org_info` WHERE id = '%s';" % orgSupId
        cursor.execute(sql_03)
        orgSupName = cursor.fetchall()[0][0]
        org_info = []
        org_info.append(orgName)
        org_info.append(orgSupName)
        org_info.append(orgTel)
        print(org_info)
        cursor.close()
        connect.close()
        return org_info

    # 数据库查询部门搜索结果
    def get_search_result_orgname_by_sql(self,user_account,key):
        connect_sql = ConnectSql()
        connect = connect_sql.connect_risk_sql()
        cursor = connect.cursor()
        sql_01 = "SELECT orgId FROM `system_user_info` WHERE loginUser = '%s';" % user_account
        cursor.execute(sql_01)
        orgId = cursor.fetchall()[0][0]
        sql_02 = "SELECT orgName FROM system_org_info WHERE (id = '" + str(
            orgId) + "' OR orgSupId = '" + str(orgId) + "') AND orgName LIKE '%" + key + "%';"
        cursor.execute(sql_02)
        data_02 = cursor.fetchall()
        orgName = []
        for i in range(len(data_02)):
            orgName.append(data_02[i][0])
        print(orgName)
        cursor.close()
        connect.close()
        return orgName

    # 数据库查询部门搜索结果总条数
    def get_search_result_num_by_sql(self,user_account,key):
        org_name = self.get_search_result_orgname_by_sql(user_account,key)
        num = len(org_name)
        print(num)
        return num


    # 点击修改
    def click_edit_org(self):
        self.driver.click_element('x,/html/body/div[1]/div[2]/div/div[1]/div[3]/div[2]/table/tbody/tr/td/div/a[2]')
        self.driver.wait()


    # 点击删除
    def click_delete_org(self):
        self.driver.click_element('x,/html/body/div/div[2]/div/div[1]/div[3]/div[2]/table/tbody/tr/td/div/a[1]')
        self.driver.wait()


    # 取消删除
    def delete_org_dismiss(self):
        self.driver.click_element('c,layui-layer-btn1')
        self.driver.wait()

    # 关闭删除确认框
    def delete_org_close(self):
        self.driver.click_element('c,layui-layer-close')
        self.driver.wait()

    # 确认删除
    def delete_org_accept(self):
        self.driver.click_element('c,layui-layer-btn0')
        self.driver.wait()


    # 获取当前显示的部门名称
    def get_current_org_name(self):
        org_name = self.driver.get_element('orgName').get_attribute('value')
        return org_name

    # 获取当前显示的所属上级名称
    def get_current_sup_org_name(self):
        sup_org_name = self.driver.get_element('orgSupName').get_attribute('value')
        return sup_org_name

    # 获取当前部门的联系方式
    def get_current_org_tel(self):
        org_tel = self.driver.get_element('orgTel').get_attribute('value')
        return org_tel

    # 修改部门名称
    def edit_org_name(self,org_name):
        self.driver.operate_input_element('orgName',org_name)
        self.driver.wait(1)

    # 选择所属上级
    def edit_sup_org(self,sup_org):
        # 点击下拉按钮
        self.driver.click_element('c,js-select-sales-btn')
        self.driver.wait()
        # 输入部门名称搜索关键词
        self.driver.operate_input_element('keyword',sup_org)
        self.driver.wait(1)
        # 点击搜索按钮
        self.driver.click_element('selectOrgBtn')
        self.driver.wait()
        # 选择原来的上级
        self.driver.click_element('x,/html/body/div/div/div[2]/form/div[2]/div/div[3]/div/div/ul/li/a/span[2]')
        self.driver.wait(1)
        # 点击收回下拉框
        self.driver.click_element('c,js-select-sales-btn')
        self.driver.wait(1)

    # 修改部门联系方式
    def edit_org_tel(self,tel):
        self.driver.operate_input_element('orgTel',tel)
        self.driver.wait(1)

    # 修改部门-点击修改按钮
    def click_org_modify_button(self):
        self.driver.click_element('c,layui-layer-btn0')
        self.driver.wait()

    # 修改部门-点击取消按钮
    def click_org_modify_dismiss(self):
        self.driver.click_element('c,layui-layer-btn1')
        self.driver.wait()

    # 修改部门-点击关闭按钮
    def click_org_modify_close(self):
        self.driver.click_element('c,layui-layer-setwin')
        self.driver.wait()


    # 修改部门-获取异常提示语
    def get_edit_org_exception_text(self):
        # 切入内层iframe
        self.driver.switch_to_iframe('x,//iframe[(@scrolling="auto")]')
        text = self.driver.get_element('s,div.layui-layer-msg').text
        return text


    # 点击查看公司部门
    def click_view_org(self):
        self.driver.click_element('x,/html/body/div[1]/div[1]/div[2]/div[2]/button')
        self.driver.wait()

