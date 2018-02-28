from time import sleep

from automate_driver.automate_driver import AutomateDriver
from automate_driver.automate_driver_server import AutomateDriverServer
from model.connect_sql import ConnectSql
from pages.base.base_page import BasePage

# 登录页面的元素及操作
# author:孙燕妮
from pages.base.base_page_server import BasePageServer


class RoleManagement(BasePage):
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

    # 点击部门管理-角色管理
    def click_role_manage(self):
        self.driver.click_element('x,/html/body/div[2]/div[2]/div/ul/li[1]')
        self.driver.wait(1)
        self.driver.click_element('x,/html/body/div[2]/div[2]/div/ul/li[1]/dl/dd[2]/a')
        self.driver.wait()
        # 切入iframe
        self.driver.switch_to_iframe('myframe')
        self.driver.wait()


    # 点击创建角色
    def click_add_role(self):
        self.driver.click_element('createRoleBtn')
        self.driver.wait()


    # 输入新增角色名称
    def input_add_role_name(self,role_name):
        self.driver.operate_input_element('roleName',role_name)
        self.driver.wait(1)


    # 填写新增角色描述
    def input_add_role_description(self,text):
        self.driver.operate_input_element('roleRemark',text)
        self.driver.wait(1)

    # 选择创建角色权限
    def choose_add_role_limit(self,limit):
        if limit == 'all':
            self.driver.click_element('x,/html/body/form/div[3]/div[1]/div')
        elif limit == 'view':
            self.driver.click_element('x,/html/body/form/div[3]/div[2]/div')
        self.driver.wait(1)


    # 创建角色点击保存按钮
    def click_add_role_save(self):
        # 跳出内层frame
        self.driver.parent_frame()
        self.driver.wait()
        self.driver.click_element('c,layui-layer-btn0')
        self.driver.wait()



    # 创建角色点击取消按钮
    def click_add_role_dismiss(self):
        # 跳出内层frame
        self.driver.parent_frame()
        self.driver.click_element('c,layui-layer-btn1')
        self.driver.wait()

    # 创建角色点击关闭按钮
    def click_add_role_close(self):
        # 跳出内层frame
        self.driver.parent_frame()
        self.driver.click_element('c,layui-layer-setwin')
        self.driver.wait()


    # 连接数据库查询创建角色
    def get_add_role_by_sql(self,user_account):
        connect_sql = ConnectSql()
        connect = connect_sql.connect_risk_sql()
        cursor = connect.cursor()
        sql = "SELECT r.roleName FROM `system_user_info` u INNER JOIN `system_role_info` r ON u.id = r.createUserId " \
              "WHERE u.loginUser = '%s' ORDER BY r.createTime DESC;" % user_account
        cursor.execute(sql)
        data = cursor.fetchall()[0][0]
        print(data)
        cursor.close()
        connect.close()
        return data


    # 获取创建角色输入有误时的异常提醒
    def get_add_role_exception1(self):
        # 切入内层iframe
        self.driver.switch_to_iframe('x,//iframe[(@scrolling="auto")]')
        text = self.driver.get_element('s,div.layui-layer-msg').text
        return text

    # 获取创建角色名称已存在时的异常提醒
    def get_add_role_exception2(self):
        text = self.driver.get_element('s,div.layui-layer-msg').text
        return text





    # 查找角色
    def search_role(self,key):
        # 输入搜索关键词
        self.driver.operate_input_element('search_input',key)
        self.driver.wait(1)
        # 点击搜索按钮
        self.driver.click_element('searchData')
        self.driver.wait()

    # 获取唯一搜索结果的角色名称
    def get_search_result_one(self):
        org_name = self.driver.get_element('x,//td[@data-field="roleName"]').text
        return org_name

    # 数据库查询角色搜索关键词结果
    def get_search_result_by_sql(self,user_account,key):
        connect_sql = ConnectSql()
        connect = connect_sql.connect_risk_sql()
        cursor = connect.cursor()
        sql_01 = "SELECT r.roleName,r.roleRemark FROM `system_user_info` u INNER JOIN `system_role_info` r ON " \
                 "u.id = r.createUserId WHERE u.loginUser = '" + user_account + "' AND r.roleName LIKE '%" + key + "%';"
        cursor.execute(sql_01)
        data = cursor.fetchall()[0]
        print(data)
        roleName = data[0]
        roleRemark = data[1]
        role_info = []
        role_info.append(roleName)
        role_info.append(roleRemark)
        print(role_info)
        cursor.close()
        connect.close()
        return role_info


    # 点击修改
    def click_edit_role(self):
        self.driver.click_element('x,/html/body/div/div/div[3]/div/div[1]/div[2]/table/tbody/tr/td[8]/div/a[1]')
        self.driver.wait()


    # 点击删除
    def click_delete_role(self):
        self.driver.click_element('x,/html/body/div[1]/div/div[3]/div/div[1]/div[2]/table/tbody/tr/td[8]/div/a[2]')
        self.driver.wait()

    # 取消删除
    def delete_role_dismiss(self):
        self.driver.click_element('c,layui-layer-btn1')
        self.driver.wait()

    # 关闭删除确认框
    def delete_role_close(self):
        self.driver.click_element('c,layui-layer-close')
        self.driver.wait()

    # 确认删除
    def delete_role_accept(self):
        self.driver.click_element('c,layui-layer-btn0')
        self.driver.wait()



    # 获取当前显示的角色名称
    def get_current_role_name(self):
        role_name = self.driver.get_element('roleName').get_attribute('value')
        return role_name


    # 获取当前角色描述
    def get_current_role_desc(self):
        org_tel = self.driver.get_element('roleRemark').get_attribute('value')
        return org_tel

    # 修改角色名称
    def edit_role_name(self,org_name):
        self.driver.operate_input_element('roleName',org_name)
        self.driver.wait(1)


    # 修改角色描述
    def edit_role_tel(self,tel):
        self.driver.operate_input_element('roleRemark',tel)
        self.driver.wait(1)

    # 修改角色-点击修改按钮
    def click_role_modify_button(self):
        self.driver.click_element('c,layui-layer-btn0')
        self.driver.wait()

    # 修改角色-点击取消按钮
    def click_role_modify_dismiss(self):
        self.driver.click_element('c,layui-layer-btn1')
        self.driver.wait()

    # 修改角色-点击关闭按钮
    def click_role_modify_close(self):
        self.driver.click_element('c,layui-layer-setwin')
        self.driver.wait()


    # 修改角色-获取异常提示语
    def get_edit_org_exception_text(self):
        # 切入内层iframe
        self.driver.switch_to_iframe('x,//iframe[(@scrolling="auto")]')
        text = self.driver.get_element('s,div.layui-layer-msg').text
        return text


    # 获取搜索结果总条数
    def get_search_result_num(self):
        num_str = str(self.driver.get_element('c,layui-laypage-count').text)
        num = (num_str.split(' ')[1]).split(' ')[0]
        print(num)
        return num

    # 获取所有搜索结果的角色名称
    def get_search_result_all(self):
        role_name = []
        for i in range(len(self.driver.get_elements('x,/html/body/div/div/div[3]/div/div[1]/div[2]/table/tbody/tr'))):
            role_name.append(self.driver.get_element('x,/html/body/div/div/div[3]/div/div[1]/div[2]/table/tbody/tr[' + str(i+1) + ']/td[2]').text)
        print(role_name)
        return role_name


    # 数据库查询角色搜索结果
    def get_search_result_rolename_by_sql(self,user_account,key):
        connect_sql = ConnectSql()
        connect = connect_sql.connect_risk_sql()
        cursor = connect.cursor()
        sql_01 = "SELECT r.roleName FROM `system_user_info` u INNER JOIN `system_role_info` r ON u.id = r.createUserId " \
                 "WHERE u.loginUser = '" + user_account + "' AND r.roleName LIKE '%" + key + "%';"
        cursor.execute(sql_01)
        data = cursor.fetchall()
        roleName = []
        for i in range(len(data)):
            roleName.append(data[i][0])
        print(roleName)
        cursor.close()
        connect.close()
        return roleName

    # 数据库查询部门搜索结果总条数
    def get_search_result_num_by_sql(self,user_account,key):
        roleName = self.get_search_result_rolename_by_sql(user_account,key)
        num = len(roleName)
        print(num)
        return num
