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



class TestCase02UserCenterModifyInfoException(unittest.TestCase):
    # 测试个人中心修改资料
    def setUp(self):
        self.driver = AutomateDriver()
        self.base_url = self.driver.base_url
        self.base_page = BasePage(self.driver, self.base_url)
        self.login_page = LoginPage(self.driver, self.base_url)
        self.user_center = UserCenter(self.driver, self.base_url)
        self.log_in_page_read_csv = LogInPageReadCsv()
        self.user_center_read_csv = UserCenterReadCsv()
        self.driver.set_window_max()
        self.connect_sql = ConnectSql()
        self.driver.wait(1)
        self.driver.clear_cookies()
        self.driver.wait(1)

        # 打开途强在线首页-登录页
        self.base_page.open_page()
        sleep(1)
        # 登录账号
        self.login_page.test_user_login()

    def tearDown(self):
        self.driver.quit_browser()

    def test_user_center_modify_info_exception(self):
        # 测试修改资料异常

        # 1.特殊字符
        special_char = "/\^<>!~%*"
        # 在电话中输入特殊字符
        self.user_center.edit_user_info_exception('孙燕妮测试用户', special_char)

        # 验证
        # 获取到电话的异常提醒
        phone_text = self.user_center.get_phone_exception_text()
        self.assertEqual('请输入正确的手机号码',phone_text)

        # 关闭修改资料弹框
        self.user_center.click_close_edit_info()

        # 获取修改后的当前用户电话
        phone_text = self.user_center.get_user_info()['tel']

        self.assertNotEqual(phone_text,special_char)




        # 2.验证用户名称、电话必填
        # 用户名称、电话输入为空
        self.user_center.edit_user_info_exception('', '')
        # 获取到用户名称、电话为空的异常提醒
        all_null_text = self.user_center.get_name_and_phone_null_text()
        self.assertEqual('请输入用户名称',all_null_text)
        # 关闭修改资料弹框
        self.user_center.click_close_edit_info()

        # 获取修改后的当前用户名
        username_null_text = self.user_center.get_user_info()['name']
        self.assertNotEqual(username_null_text, '')
        # 获取修改后的当前用户电话
        phone_null_text = self.user_center.get_user_info()['tel']
        self.assertNotEqual(phone_null_text, '')




        # 用户名称输入为空、电话输入正确
        phone_01 = '13852654587'
        self.user_center.edit_user_info_exception('', phone_01)
        # 获取到用户名称为空的异常提醒
        username_text = self.user_center.get_name_null_text()
        self.assertEqual('请输入用户名称',username_text)
        # 关闭修改资料弹框
        self.user_center.click_close_edit_info()
        # 获取修改后的当前用户名
        name_null_only_text = self.user_center.get_user_info()['name']
        self.assertNotEqual(name_null_only_text, '')
        # 获取修改后的当前用户电话
        phone01 = self.user_center.get_user_info()['tel']
        self.assertNotEqual(phone01,phone_01)



        # 用户名输入正确、电话为空
        name_01 = '孙燕妮测试用户'
        self.user_center.edit_user_info_exception(name_01, '')
        # 获取到电话为空的异常提醒
        phone_null_text = self.user_center.get_phone_null_text()
        self.assertEqual('请输入正确的手机号码',phone_null_text)
        # 关闭修改资料弹框
        self.user_center.click_close_edit_info()
        # 获取修改后的当前用户名
        name01 = self.user_center.get_user_info()['name']
        self.assertNotEqual(name01, name_01)
        # 获取修改后的当前用户电话
        phone02 = self.user_center.get_user_info()['tel']
        self.assertNotEqual(phone02, '')



        # 3.验证用户名称、电话长度限制
        long_char = 'fsaffsdafsadfvczxfsdsafdfasdfasdfsdfsdfasdfasdffffffff'
        long_tel = '123456789456'
        short_tel = '1234567894'

        # 用户名输入超出字符长度限制、电话输入正确
        tel = '13582698666'
        self.user_center.edit_user_info_exception(long_char, tel)
        # 获取到用户名超长的异常提醒
        username_long_text = self.user_center.get_username_long_text()
        self.assertEqual('用户名称不能大于50个字符',username_long_text)
        # 关闭修改资料弹框
        self.user_center.click_close_edit_info()
        # 获取修改后的当前用户名
        name03 = self.user_center.get_user_info()['name']
        self.assertNotEqual(name03, long_char)
        # 获取修改后的当前用户电话
        phone03 = self.user_center.get_user_info()['tel']
        self.assertNotEqual(phone03, tel)


        # 用户名输入正确、电话输入超出长度限制
        name_04 = '孙燕妮测试'
        self.user_center.edit_user_info_exception(name_04, long_tel)
        # 获取到电话输入超长的异常提醒
        long_tel_text = self.user_center.get_phone_exception_text()
        self.assertEqual('请输入正确的手机号码',long_tel_text)
        # 关闭修改资料弹框
        self.user_center.click_close_edit_info()
        # 获取修改后的当前用户名
        name04 = self.user_center.get_user_info()['name']
        self.assertNotEqual(name04, name_04)
        # 获取修改后的当前用户电话
        phone04 = self.user_center.get_user_info()['tel']
        self.assertNotEqual(phone04, long_tel)


        # 用户名输入正确、电话输入低于正常限制
        name_05 = '孙燕妮测试'
        self.user_center.edit_user_info_exception(name_05, short_tel)
        # 获取到电话输入超长的异常提醒
        short_tel_text = self.user_center.get_phone_exception_text()
        self.assertEqual('请输入正确的手机号码', short_tel_text)
        # 关闭修改资料弹框
        self.user_center.click_close_edit_info()
        # 获取修改后的当前用户名
        name05 = self.user_center.get_user_info()['name']
        self.assertNotEqual(name05, name_05)
        # 获取修改后的当前用户电话
        phone05 = self.user_center.get_user_info()['tel']
        self.assertNotEqual(phone05, short_tel)



        # 退出登录
        self.user_center.logout()



