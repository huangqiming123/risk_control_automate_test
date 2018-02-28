from time import sleep

from automate_driver.automate_driver import AutomateDriver
from automate_driver.automate_driver_server import AutomateDriverServer
from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage

# 登录页面的元素及操作
# author:孙燕妮
from pages.base.base_page_server import BasePageServer


class UserManagement(BasePage):
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

    # 点击部门管理-用户管理
    def click_user_manage(self):
        self.driver.click_element('x,/html/body/div[2]/div[2]/div/ul/li[1]')
        self.driver.wait(1)
        self.driver.click_element('x,/html/body/div[2]/div[2]/div/ul/li[1]/dl/dd[3]/a')
        self.driver.wait()
        # 切入iframe
        self.driver.switch_to_iframe('myframe')
        self.driver.wait()


    # 点击新增用户
    def click_add_user(self):
        self.driver.click_element('newBsers')
        self.driver.wait()


    # 填写新增用户名
    def input_add_user_name(self,user_name):
        self.driver.operate_input_element('userName',user_name)
        self.driver.wait(1)

    # 填写新增用户登录账号
    def input_add_login_user(self,loginUser):
        self.driver.operate_input_element('loginUser',loginUser)
        self.driver.wait(1)


    # 填写新增用户登录密码
    def input_add_login_passwd(self,loginPwd):
        self.driver.operate_input_element('loginPwd',loginPwd)
        self.driver.wait(1)


    # 填写新增用户手机号码
    def input_add_user_phone(self,tel):
        self.driver.operate_input_element('userTel',tel)
        self.driver.wait(1)

    # 新增用户分配角色
    def input_add_user_role(self):
        self.driver.click_element('x,/html/body/form/div[5]/div/div/div/input')
        self.driver.wait(1)
        self.driver.click_element('x,/html/body/form/div[5]/div/div/dl/dd[4]')
        self.driver.wait(1)

    # 新增用户选择所属上级
    def choose_add_user_org(self):
        self.driver.click_element('x,/html/body/form/div[6]/div[2]/ul/li/a/span[2]')
        self.driver.wait()

    # 新增用户点击保存按钮
    def click_add_user_save(self):
        # 跳出内层frame
        self.driver.parent_frame()
        self.driver.wait()
        self.driver.click_element('c,layui-layer-btn0')
        self.driver.wait()



    # 新增用户点击取消按钮
    def click_add_user_dismiss(self):
        # 跳出内层frame
        self.driver.parent_frame()
        self.driver.click_element('c,layui-layer-btn1')
        self.driver.wait()

    # 新增用户点击关闭按钮
    def click_add_user_close(self):
        # 跳出内层frame
        self.driver.parent_frame()
        self.driver.click_element('c,layui-layer-setwin')
        self.driver.wait()


    # 连接数据库查询新增用户
    def get_add_user_by_sql(self,user_account):
        connect_sql = ConnectSql()
        connect = connect_sql.connect_risk_sql()
        cursor = connect.cursor()
        sql_01 = "SELECT id FROM `system_user_info` WHERE loginUser = '%s';" % user_account
        cursor.execute(sql_01)
        id = cursor.fetchall()[0][0]
        sql_02 = "SELECT loginUser FROM `system_user_info` WHERE userState = '1' and createUserId = '%s'  ORDER BY " \
                 "createTime DESC;" % id
        cursor.execute(sql_02)
        data = cursor.fetchall()
        '''add_user_account = []
        for i in range(len(data)):
            add_user_account.append(data[i][0])'''
        add_user_account = data[0][0]
        print(add_user_account)
        cursor.close()
        connect.close()
        return add_user_account




    # 获取新增公司部门输入有误时的异常提醒
    def get_add_user_exception1(self):
        # 切入内层iframe
        self.driver.switch_to_iframe('x,//iframe[(@scrolling="auto")]')
        text = self.driver.get_element('s,div.layui-layer-msg').text
        return text

    # 获取新增公司部门名称已存在时的异常提醒
    def get_add_user_exception2(self):
        text = self.driver.get_element('s,div.layui-layer-msg').text
        return text



    # 查找部门
    def search_user(self,key):
        # 输入搜索关键词
        self.driver.operate_input_element('search_input',key)
        self.driver.wait(1)
        # 点击搜索按钮
        self.driver.click_element('searchData')
        self.driver.wait()

    # 获取唯一搜索结果的用户名称
    def get_search_result_one(self):
        user_name = self.driver.get_element('x,//td[@data-field="userName"]').text
        return user_name

    # 数据库查询用户搜索关键词结果
    def get_search_result_by_sql(self,user_account,key):
        connect_sql = ConnectSql()
        connect = connect_sql.connect_risk_sql()
        cursor = connect.cursor()
        sql_01 = "SELECT id FROM `system_user_info` WHERE loginUser = '%s';" % user_account
        cursor.execute(sql_01)
        id = cursor.fetchall()[0][0]
        sql_02 = "SELECT userName,userTel FROM `system_user_info` WHERE userState = '1' and createUserId = '" + str(id) +"'  AND " \
                 "(loginUser LIKE '%" + key + "%' OR userName LIKE '%" + key + "%' OR userTel LIKE '%" + key + "%') " \
                 "ORDER BY createTime DESC;"
        cursor.execute(sql_02)
        data = cursor.fetchall()[0]
        user_info = []
        user_info.append(data[0])
        user_info.append(data[1])
        print(user_info)
        cursor.close()
        connect.close()
        return user_info


    # 获取搜索结果总条数
    def get_search_result_num(self):
        num_str = str(self.driver.get_element('c,layui-laypage-count').text)
        num = (num_str.split(' ')[1]).split(' ')[0]
        print(num)
        return num

    # 获取所有搜索结果的用户名称
    def get_search_result_all(self):
        user_name = []
        for i in range(len(self.driver.get_elements('x,/html/body/div/div/div[3]/div/div[1]/div[2]/table/tbody/tr'))):
            user_name.append(self.driver.get_element('x,/html/body/div[2]/div/div[3]/div/div[1]/div[2]/table/tbody/tr[' + str(i+1) + ']/td[2]').text)
        print(user_name)
        return user_name


    # 数据库查询角色搜索结果
    def get_search_result_username_by_sql(self,user_account,key):
        connect_sql = ConnectSql()
        connect = connect_sql.connect_risk_sql()
        cursor = connect.cursor()
        sql_01 = "SELECT id,userName FROM `system_user_info` WHERE loginUser = '%s';" % user_account
        cursor.execute(sql_01)
        data_01 = cursor.fetchall()
        print(data_01)
        id = data_01[0][0]
        userName = data_01[0][1]
        sql_02 = "SELECT userName FROM `system_user_info` WHERE userState = '1' and createUserId = '" + str(
            id) + "'  AND " \
                  "(loginUser LIKE '%" + key + "%' OR userName LIKE '%" + key + "%' OR userTel LIKE '%" + key + "%') " \
                                                                                                                "ORDER BY createTime DESC;"
        cursor.execute(sql_02)
        data = cursor.fetchall()
        user_name = [userName]
        for i in range(len(data)):
            user_name.append(data[i][0])
        print(user_name)
        cursor.close()
        connect.close()
        return user_name


    # 数据库查询部门搜索结果总条数
    def get_search_result_num_by_sql(self,user_account,key):
        userName = self.get_search_result_username_by_sql(user_account,key)
        num = len(userName)
        print(num)
        return num


    # 点击修改
    def click_edit_user(self):
        self.driver.click_element('x,/html/body/div[2]/div/div[3]/div/div[1]/div[3]/div[2]/table/tbody/tr/td/div/a[1]')
        self.driver.wait()


    # 获取当前显示的用户名称
    def get_current_user_name(self):
        user_name = self.driver.get_element('userName').get_attribute('value')
        return user_name


    # 获取当前用户的联系方式
    def get_current_user_tel(self):
        user_tel = self.driver.get_element('userTel').get_attribute('value')
        return user_tel

    # 修改用户名称
    def edit_user_name(self,user_name):
        self.driver.operate_input_element('userName',user_name)
        self.driver.wait(1)


    # 修改用户联系方式
    def edit_user_tel(self,tel):
        self.driver.operate_input_element('userTel',tel)
        self.driver.wait(1)

    # 修改用户-点击修改按钮
    def click_user_modify_button(self):
        self.driver.click_element('c,layui-layer-btn0')
        self.driver.wait()

    # 修改用户-点击取消按钮
    def click_user_modify_dismiss(self):
        self.driver.click_element('c,layui-layer-btn1')
        self.driver.wait()

    # 修改用户-点击关闭按钮
    def click_user_modify_close(self):
        self.driver.click_element('c,layui-layer-setwin')
        self.driver.wait()



    # 点击删除
    def click_delete_user(self):
        self.driver.click_element('x,/html/body/div[2]/div/div[3]/div/div[1]/div[3]/div[2]/table/tbody/tr/td/div/a[2]')
        self.driver.wait()

    # 取消删除
    def delete_user_dismiss(self):
        self.driver.click_element('c,layui-layer-btn1')
        self.driver.wait()

    # 关闭删除确认框
    def delete_user_close(self):
        self.driver.click_element('c,layui-layer-close')
        self.driver.wait()

    # 确认删除
    def delete_user_accept(self):
        self.driver.click_element('c,layui-layer-btn0')
        self.driver.wait()

