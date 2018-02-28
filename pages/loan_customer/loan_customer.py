from time import sleep

from automate_driver.automate_driver import AutomateDriver
from automate_driver.automate_driver_server import AutomateDriverServer
from pages.base.base_page import BasePage
from model.connect_sql import ConnectSql

# 贷款客户录入的元素及操作
# author:孙燕妮
from pages.base.base_page_server import BasePageServer


class LoanCustomer(BasePage):
    def __init__(self, driver: AutomateDriver, base_url):
        super().__init__(driver, base_url)



    # 进入贷款客户录入
    def click_loan_customer_input(self):
        self.driver.click_element('x,/html/body/div[2]/div[2]/div/ul/li[3]')
        self.driver.wait(1)
        self.driver.click_element('x,/html/body/div[2]/div[2]/div/ul/li[3]/dl/dd[1]/a')
        self.driver.wait()


    # 切入外层frame
    def switch_to_1_frame(self):
        self.driver.switch_to_iframe('myframe')
        self.driver.wait()


    # 录入车主信息
    # 输入车主姓名
    def input_owner_name(self,name):
        self.driver.operate_input_element('carOwnerName',name)
        self.driver.wait(1)

    # 输入车主手机
    def input_owner_tel(self,tel):
        self.driver.operate_input_element('carOwnerPhone',tel)
        self.driver.wait(1)

    # 选择车主证件
    def choose_owner_ID_type(self,type):
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[2]/div/form[1]/div[1]/div[3]/div[1]/div/div/div/input')
        self.driver.wait(1)
        if type == '身份证':
            self.driver.click_element('x,/html/body/div[1]/div[2]/div[2]/div/form[1]/div[1]/div[3]/div[1]/div/div/dl/dd[2]')
            self.driver.wait(1)
        elif type == '护照':
            self.driver.click_element('x,/html/body/div[1]/div[2]/div[2]/div/form[1]/div[1]/div[3]/div[1]/div/div/dl/dd[3]')
            self.driver.wait(1)

    # 输入车主证件号
    def input_owner_ID(self,ID):
        self.driver.operate_input_element('carOwnerIdCard',ID)
        self.driver.wait(1)

    # 选择车主性别
    def choose_owner_sex(self,sex):
        if sex == '男':
            self.driver.click_element('x,/html/body/div[1]/div[2]/div[2]/div/form[1]/div[1]/div[4]/div[1]/div/div[1]/i')
            self.driver.wait(1)
        elif sex == '女':
            self.driver.click_element('x,/html/body/div[1]/div[2]/div[2]/div/form[1]/div[1]/div[4]/div[1]/div/div[2]/i')
            self.driver.wait(1)


    # 选择车主贷款单位
    def choose_owner_loan_com(self,com):
        self.driver.click_element('treeBut')
        self.driver.wait(1)
        self.driver.operate_input_element('keyword',com)
        self.driver.click_element('selectOrgBtn')
        self.driver.wait(1)
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[2]/div/form[1]/div[1]/div[4]/div[2]/div/div[3]/div/div/ul/li/a/span[2]')
        self.driver.wait(1)
        self.driver.click_element('treeBut')
        self.driver.wait(1)


    # 车主信息保存
    def save_owner_info(self):
        self.driver.click_element('addCarOwnerBut')
        self.driver.wait()


    # 录入车辆信息
    # 输入车牌号
    def input_car_num(self,num):
        self.driver.operate_input_element('carPlateNumber',num)
        self.driver.wait(1)

    # 输入车型
    def input_car_model(self,model):
        self.driver.operate_input_element('carModel',model)
        self.driver.wait(1)

    # 输入发动机号
    def input_car_engi_num(self,num):
        self.driver.operate_input_element('carEngineNumber',num)
        self.driver.wait(1)

    # 输入车架号
    def input_car_frame_num(self,num):
        self.driver.operate_input_element('carFrameNumber',num)
        self.driver.wait(1)

    # 选择车辆类型
    def choose_car_type(self,type):
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[2]/div/form[2]/div[1]/div[4]/div/div/div/div/input')
        self.driver.wait()
        if type == '新车':
            self.driver.click_element('x,/html/body/div[1]/div[2]/div[2]/div/form[2]/div[1]/div[4]/div/div/div/dl/dd[2]')
        elif type == '二手车':
            self.driver.click_element('x,/html/body/div[1]/div[2]/div[2]/div/form[2]/div[1]/div[4]/div/div/div/dl/dd[3]')
        elif type == '进口车':
            self.driver.click_element('x,/html/body/div[1]/div[2]/div[2]/div/form[2]/div[1]/div[4]/div/div/div/dl/dd[4]')
        self.driver.wait()



    # 输入工作地址
    def input_com_address(self,address):
        self.driver.operate_input_element('workAddress',address)
        self.driver.wait(1)

    # 输入常停留点
    def input_stop_point(self,point):
        self.driver.click_element('address0')
        self.driver.wait()
        self.driver.operate_input_element('mapSearchText',point)
        self.driver.click_element('c,layui-layer-btn0')
        self.driver.wait(1)

    # 保存车辆信息
    def save_car_info(self):
        self.driver.click_element('addCarBut')
        self.driver.wait()




    # 录入贷款信息
    # 输入贷款日期
    def input_loan_date(self):
        self.driver.click_element('loanDate')
        self.driver.wait()
        self.driver.click_element('x,/html/body/div[4]/div[2]/div/span[3]')
        self.driver.wait()

    # 输入贷款金额
    def input_loan_money(self,money):
        self.driver.operate_input_element('loanSum',money)
        self.driver.wait(1)

    # 输入贷款期限
    def input_loan_deadline(self,deadline):
        self.driver.operate_input_element('loanMonth',deadline)
        self.driver.wait(1)

    # 输入应还金额
    def input_current_balance(self,current):
        self.driver.operate_input_element('repaymentSum',current)
        self.driver.wait(1)

    # 选择还款方式
    def choose_pay_type(self,pay_type):
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[2]/div/form[3]/div[1]/div[4]/div[1]/div/div/div/input')
        self.driver.wait()
        if pay_type == '分期':
            self.driver.click_element('x,/html/body/div[1]/div[2]/div[2]/div/form[3]/div[1]/div[4]/div[1]/div/div/dl/dd[2]')
        elif pay_type == '全款':
            self.driver.click_element('x,/html/body/div[1]/div[2]/div[2]/div/form[3]/div[1]/div[4]/div[1]/div/div/dl/dd[3]')
        self.driver.wait()

    # 选择还款日
    def choose_pay_date(self,pay_date):
        self.driver.click_element('x,/html/body/div[1]/div[2]/div[2]/div/form[3]/div[1]/div[4]/div[2]/div[1]/div/div/div/input')
        self.driver.wait(2)
        if pay_date == '1':
            self.driver.click_element('x,/html/body/div[1]/div[2]/div[2]/div/form[3]/div[1]/div[4]/div[2]/div[1]/div/div/dl/dd[2]')
        elif pay_date == '2':
            self.driver.click_element('x,/html/body/div[1]/div[2]/div[2]/div/form[3]/div[1]/div[4]/div[2]/div[1]/div/div/dl/dd[3]')
        elif pay_date == '3':
            self.driver.click_element('x,/html/body/div[1]/div[2]/div[2]/div/form[3]/div[1]/div[4]/div[2]/div[1]/div/div/dl/dd[4]')
        self.driver.wait()

    # 输入合同编号
    def input_contract_number(self,contract_num):
        self.driver.operate_input_element('contractNumber',contract_num)
        self.driver.wait(1)

    # 保存贷款信息
    def save_loan_info(self):
        self.driver.click_element('addCarLoansBut')
        self.driver.wait()


    # 录入安装设备
    # 点击安装设备
    def click_install_dev(self):
        self.driver.click_element('install')
        self.driver.wait()

    # 切入frame
    def switch_to_frame1(self):
        self.driver.switch_to_iframe('myframe')
        self.driver.wait(2)


    # 输入Imei搜索
    def input_dev_imei(self,imei):
        self.driver.operate_input_element('imei',imei)
        self.driver.wait(1)


    # 选择安装时间
    def choose_install_time(self):
        self.driver.click_element('installTime')
        self.driver.wait()
        self.driver.click_element('x,/html/body/div[6]/div[2]/div/span[3]')
        self.driver.wait()

    # 输入安装地址
    def input_install_address(self,install_address):
        self.driver.operate_input_element('installAddress',install_address)
        self.driver.wait(1)

    # 输入安装人员
    def input_install_person(self,install_person):
        self.driver.operate_input_element('installUser',install_person)
        self.driver.wait(1)

    # 保存安装信息
    def save_install_info(self):
        self.driver.click_element("addGpsBut")

    # 跳出frame1
    def switch_out_frame1(self):
        self.driver.default_frame()






