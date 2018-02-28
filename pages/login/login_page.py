from time import sleep

from automate_driver.automate_driver import AutomateDriver
from automate_driver.automate_driver_server import AutomateDriverServer
from pages.base.base_page import BasePage

# 登录页面的元素及操作
# author:孙燕妮
from pages.base.base_page_server import BasePageServer


class LoginPage(BasePage):
    def __init__(self, driver: AutomateDriver, base_url):
        super().__init__(driver, base_url)

    # 用户名输入框
    def account_input(self, account):
        self.driver.operate_input_element("username", account)

    # 密码输入框
    def password_input(self, password):
        self.driver.operate_input_element("password", password)

    # 点击密码输入框
    def click_password(self):
        self.driver.get_element('password').click()

    # 忘记密码点击操作
    def forget_password(self):
        # self.driver.click_element("l,忘记密码")
        self.driver.click_element("c,js-password")

    # 体验账号登入
    def taste(self):
        #self.user_login("taste", "888888")
        self.driver.click_element("loginNovice")
        self.driver.wait()

    # 登录时记住我勾选框
    def remember_me(self):
        checkbox = self.driver.get_element("c,layui-icon")
        checkbox.click()

    # 检查记住我勾选框状态
    def check_remember_me(self):
        is_checked = self.driver.get_element("c,layui-unselect").get_attribute('class')
        print(is_checked)
        if 'layui-form-checked' in is_checked:
            box_status = True
        else:
            box_status = False
        return box_status

    # 登录按钮点击操作
    def login_button_click(self):
        self.driver.click_element("loginButton")

    # 获取登录按钮的文本内容
    def login_button_text(self):
        login_button_text = self.driver.get_element("loginButton").text
        return login_button_text


    # 封装登录操作
    def user_login(self, account, password):
        self.account_input(account)
        self.password_input(password)
        self.login_button_click()
        self.driver.wait(3)

    # 默认测试账号syntest登录
    def test_user_login(self):
        self.account_input('syntest')
        self.password_input('jimi123')
        self.login_button_click()
        self.driver.wait(3)


    # 获取登录异常提示语
    def get_exception_text(self):
        text = self.driver.get_element('x,/html/body/div/div/div[1]/p').text
        return text


    # 测试统计报表登录账号线上环境hqjceshi
    def test_statistics_login_user_normal(self):
        self.account_input('hqjceshi')
        self.password_input('123456')
        self.login_button_click()
        self.driver.wait(3)


    # 测试统计报表登录账号测试环境hqjceshi
    def test_statistics_login_user(self):
        self.account_input('xintest')
        self.password_input('123')
        self.login_button_click()
        self.driver.wait(3)

    # 测试操作日志登录账号线上环境zhangyuan1
    def test_log_login_user_normal(self):
        self.account_input('zhangyuan1')
        self.password_input('123')
        self.login_button_click()
        self.driver.wait(3)







