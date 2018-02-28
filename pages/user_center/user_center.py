from time import sleep

from automate_driver.automate_driver import AutomateDriver
from automate_driver.automate_driver_server import AutomateDriverServer
from pages.base.base_page import BasePage
from model.connect_sql import ConnectSql

# 用户中心的元素及操作
# author:孙燕妮
from pages.base.base_page_server import BasePageServer


class UserCenter(BasePage):
    def __init__(self, driver: AutomateDriver, base_url):
        super().__init__(driver, base_url)


    def get_account_info_by_sql(self, user_account):
        # 获取当前登录账号的客户信息
        connect_sql = ConnectSql()
        connect = connect_sql.connect_risk_sql()
        cursor = connect.cursor()
        sql = "SELECT loginUser,userName,userTel FROM `system_user_info` WHERE loginUser = '%s';" % user_account
        cursor.execute(sql)
        data = cursor.fetchall()
        print(data)
        data_list = []
        data_list.append(data[0][0])
        data_list.append(data[0][1])
        data_list.append(data[0][2])
        cursor.close()
        connect.close()
        return data_list


    # 取提示语
    def get_modify_prompt(self, select):
        try:
            prompt = self.driver.get_text(select)
            return prompt
        except:
            prompt = ""
            return prompt

    # 获取登录成功后导航栏显示的用户名
    def get_username(self):
        text = self.driver.get_element('x,/html/body/div[2]/div[1]/div[2]/ul/li[5]/p[1]/span').text
        return text


    # 退出登录操作
    def logout(self):
        self.driver.click_element('signOutSystem')
        self.driver.wait()
        self.driver.click_element('c,layui-layer-btn0')
        self.driver.wait()

    # 取消退出登录
    def logout_dismiss(self):
        self.driver.click_element('signOutSystem')
        self.driver.wait()
        self.driver.click_element('c,layui-layer-btn1')
        self.driver.wait()

    # 关闭退出登录弹框
    def logout_close(self):
        self.driver.click_element('signOutSystem')
        self.driver.wait()
        self.driver.click_element('c,layui-layer-setwin')
        self.driver.wait()


    # 获取首页各模块名称
    def get_module_name(self):
        li_list = self.driver.get_elements('x,/html/body/div[2]/div[2]/div/ul/li')
        module_name = []
        for i in range(len(li_list)):
            module_name.append(li_list[i].text)
        return module_name


    # 打开用户中心-修改资料，获取修改资料框中的用户信息
    def get_user_info(self):
        # 将鼠标悬浮在用户中心图标处
        self.driver.wait()
        ele = self.driver.get_element('x,/html/body/div[2]/div[1]/div[2]/ul/li[3]/a/i')
        self.driver.float_element(ele)
        self.driver.wait()
        # 点击“修改个人资料”
        self.driver.click_element("c,js-edit-phone")
        self.driver.wait()
        # 获取登录账号输入框的信息
        login_account = self.driver.get_element('x,/html/body/div[4]/div[2]/div/div[1]/div/div/input').get_attribute('value')
        # 获取用户姓名
        name = self.driver.get_element('userName').get_attribute('value')
        # 获取用户电话
        tel = self.driver.get_element('userTel').get_attribute('value')
        # 关闭弹框
        self.driver.click_element('c,layui-layer-setwin')
        self.driver.wait(1)
        user_info = {
            'login_account': login_account,
            'name': name,
            'tel': tel
        }
        return user_info

    # 修改资料框打开状态下，点击关闭
    def click_close_edit_info(self):
        self.driver.click_element('c,layui-layer-setwin')
        self.driver.wait()




    # 用户中心-修改资料
    def edit_user_info(self, username, phone):
        # 将鼠标悬浮在用户中心图标处
        self.driver.wait()
        ele = self.driver.get_element('x,/html/body/div[2]/div[1]/div[2]/ul/li[3]/a/i')
        self.driver.float_element(ele)
        self.driver.wait()
        # 点击“修改个人资料”
        self.driver.click_element("c,js-edit-phone")
        self.driver.wait()
        # 修改用户姓名
        self.driver.operate_input_element('userName',username)
        self.driver.wait(1)
        # 修改用户电话
        self.driver.operate_input_element('userTel',phone)
        self.driver.wait(1)
        # 点击确认
        self.driver.click_element('c,layui-layer-btn0')
        self.driver.wait()


    # 用户中心-修改资料-用于修改资料异常测试
    def edit_user_info_exception(self,username,phone):
        # 将鼠标悬浮在用户中心图标处
        self.driver.wait()
        ele = self.driver.get_element('x,/html/body/div[2]/div[1]/div[2]/ul/li[3]/a/i')
        self.driver.float_element(ele)
        self.driver.wait()
        # 点击“修改个人资料”
        self.driver.click_element("c,js-edit-phone")
        self.driver.wait()
        # 修改用户姓名
        self.driver.operate_input_element('userName',username)
        self.driver.wait(1)
        # 修改用户电话
        self.driver.operate_input_element('userTel',phone)
        self.driver.wait(1)
        # 点击确认
        self.driver.click_element('c,layui-layer-btn0')
        self.driver.wait(3)

    # 用户中心-修改资料不保存
    def edit_user_info_not_save(self,username,phone):
        # 将鼠标悬浮在用户中心图标处
        self.driver.wait()
        ele = self.driver.get_element('x,/html/body/div[2]/div[1]/div[2]/ul/li[3]/a/i')
        self.driver.float_element(ele)
        self.driver.wait()
        # 点击“修改个人资料”
        self.driver.click_element("c,js-edit-phone")
        self.driver.wait()
        # 修改用户姓名
        self.driver.operate_input_element('userName',username)
        self.driver.wait(1)
        # 修改用户电话
        self.driver.operate_input_element('userTel',phone)
        self.driver.wait(1)
        # 点击取消
        self.driver.click_element('c,layui-layer-btn1')
        self.driver.wait()

    # 用户中心-修改资料不保存直接关闭
    def edit_user_info_close(self,username,phone):
        # 将鼠标悬浮在用户中心图标处
        self.driver.wait()
        ele = self.driver.get_element('x,/html/body/div[2]/div[1]/div[2]/ul/li[3]/a/i')
        self.driver.float_element(ele)
        self.driver.wait()
        # 点击“修改个人资料”
        self.driver.click_element("c,js-edit-phone")
        self.driver.wait()
        # 修改用户姓名
        self.driver.operate_input_element('userName',username)
        self.driver.wait(1)
        # 修改用户电话
        self.driver.operate_input_element('userTel',phone)
        self.driver.wait(1)
        # 点击关闭
        self.driver.click_element('c,layui-layer-setwin')
        self.driver.wait()


    # 获取当前登录账号
    def get_login_account(self):
        self.driver.wait()
        ele = self.driver.get_element('x,/html/body/div[2]/div[1]/div[2]/ul/li[3]/a/i')
        self.driver.float_element(ele)
        self.driver.wait()
        # 点击“修改个人资料”
        self.driver.click_element("c,js-edit-phone")
        self.driver.wait()
        # 获取登录账号输入框的信息
        login_account = self.driver.get_element('x,/html/body/div[4]/div[2]/div/div[1]/div/div/input').get_attribute('value')
        print(login_account)
        # 关闭
        self.driver.click_element('c,layui-layer-setwin')
        self.driver.wait()
        return login_account







    # 修改资料--取长度
    def get_modify_info_element_len(self):
        phone_len = int(self.driver.get_element("x,//*[@id='edit-modal-phone']").get_attribute("maxlength"))
        email_len = int(self.driver.get_element("x,//*[@id='edit-modal-email']").get_attribute("maxlength"))
        len = {"phone_len": phone_len,
               "email_len": email_len
               }
        return len

    # 获取到电话填写错误的异常提醒
    def get_phone_exception_text(self):
        text = self.driver.get_element('s,div.layui-layer-msg').text
        return text

    # 修改资料框打开状态下，获取用户名
    def get_user_name(self):
        name = self.driver.get_element('userName').get_attribute('value')
        return name


    # 修改资料框打开状态下，获取用户电话信息
    def get_user_phone(self):
        phone = self.driver.get_element('userTel').get_attribute('value')
        return phone

    # 获取到用户名、电话均为空时的异常提醒
    def get_name_and_phone_null_text(self):
        text = self.driver.get_element('s,div.layui-layer-msg').text
        return text

    # 获取到仅用户名为空时的异常提醒
    def get_name_null_text(self):
        text = self.driver.get_element('s,div.layui-layer-msg').text
        return text

    # 获取到仅电话为空时的异常提醒
    def get_phone_null_text(self):
        text = self.driver.get_element('s,div.layui-layer-msg').text
        return text


    # 获取到用户名超出长度限制的异常提醒
    def get_username_long_text(self):
        text = self.driver.get_element('s,div.layui-layer-msg').text
        return text



    # 点击打开修改密码框
    def click_edit_password(self):
        # 将鼠标悬浮在用户中心图标处
        self.driver.wait()
        ele = self.driver.get_element('x,/html/body/div[2]/div[1]/div[2]/ul/li[3]/a/i')
        self.driver.float_element(ele)
        self.driver.wait()
        # 点击“修改密码”
        self.driver.click_element('c,js-edit-password')
        self.driver.wait()

    # 修改密码-输入原密码
    def input_old_password(self,old_password):
        self.driver.operate_input_element('oldPassword',old_password)
        self.driver.wait(1)

    # 修改密码-输入修改密码（新密码）
    def input_new_password(self,new_password):
        self.driver.operate_input_element('newPassword',new_password)
        self.driver.wait(1)

    # 修改密码-输入确认密码
    def input_password_again(self,password_again):
        self.driver.operate_input_element('confirmPassword',password_again)
        self.driver.wait(1)

    # 修改密码---错误提示
    def get_modify_pwd_exception_prompt(self, old_password,new_password,password_again):
        # 旧密码、新密码、确认新密码
        self.input_old_password(old_password)
        self.input_new_password(new_password)
        self.input_password_again(password_again)
        # 点击确认按钮
        self.driver.click_element('c,layui-layer-btn0')
        self.driver.wait()

        # 获取弹出框的提示
        text = self.driver.get_element("s,div.layui-layer-msg").text

        print(text)
        return text


    # 修改密码-点击确认按钮
    def click_edit_password_confirm(self):
        self.driver.click_element('c,layui-layer-btn0')

    # 修改密码-点击取消按钮
    def click_edit_password_dismiss(self):
        self.driver.click_element('c,layui-layer-btn1')

    # 修改密码-点击关闭弹框
    def click_edit_password_close(self):
        self.driver.click_element('c,layui-layer-setwin')



    # 点击进入意见反馈
    def click_feedback(self):
        # 将鼠标悬浮在帮助图标处
        self.driver.wait()
        ele = self.driver.get_element('c,icon-bangzhu')
        self.driver.float_element(ele)
        self.driver.wait()
        # 点击“意见反馈”
        self.driver.click_element("x,/html/body/div[2]/div[1]/div[2]/ul/li[2]/dl/dd[3]/a")
        self.driver.wait()
        # 进入frame
        self.driver.switch_to_iframe('myframe')
        self.driver.wait(1)


    # 意见反馈-选择问题类型
    def choose_problem_type(self,type):
        if type == 'GPS设备相关问题':
            self.driver.click_element('x,/html/body/div/div[1]/div[1]/div/div[1]/i')
        elif type == '车主信息管理相关问题':
            self.driver.click_element('x,/html/body/div/div[1]/div[1]/div/div[2]/i')
        elif type == '车辆异常追踪问题':
            self.driver.click_element('x,/html/body/div/div[1]/div[1]/div/div[3]/i')
        elif type == '设置车辆异常提醒问题':
            self.driver.click_element('x,/html/body/div[1]/div[1]/div[2]/div/div[1]/i')
        elif type == '公司部门管理问题':
            self.driver.click_element('x,/html/body/div[1]/div[1]/div[2]/div/div[2]/i')
        elif type == 'GPS参数设置问题':
            self.driver.click_element('x,/html/body/div[1]/div[1]/div[2]/div/div[3]/i')
        self.driver.wait(1)


    # 意见反馈-填写反馈意见内容
    def input_problem_content(self,content):
        self.driver.operate_input_element('feedbackContent',content)
        self.driver.wait(1)

    # 意见反馈-填写意见反馈联系人
    def input_linkman(self,linkman):
        self.driver.operate_input_element('linkman',linkman)
        self.driver.wait(1)

    # 意见反馈-填写意见反馈联系方式
    def input_phone(self,phone):
        self.driver.operate_input_element('phone',phone)
        self.driver.wait(1)


    # 意见反馈-点击提交按钮
    def click_submit(self):
        self.driver.click_element('submitOpinion')
        self.driver.wait()




    def get_feedback_info_by_sql(self, user_account):
        # 获取当前登录账号提交的反馈信息
        connect_sql = ConnectSql()
        connect = connect_sql.connect_risk_sql()
        cursor = connect.cursor()
        sql = "SELECT loginUser,type,content,linkman,phone FROM system_user_info u INNER JOIN user_feedback f on" \
              " u.id = f.createUserId WHERE u.loginUser = '%s' ORDER BY f.createTime DESC;" % user_account
        cursor.execute(sql)
        data = cursor.fetchall()
        print(data)
        data_list = []
        data_list.append(data[0][0])
        data_list.append(data[0][1])
        data_list.append(data[0][2])
        data_list.append(data[0][3])
        data_list.append(data[0][4])
        cursor.close()
        connect.close()
        return data_list


    # 提交反馈意见成功提示语
    def get_feedback_success_text(self):
        text = self.driver.get_element('s,div.layui-layer-msg').text
        # 退出iframe
        self.driver.default_frame()
        self.driver.wait(1)
        return text







