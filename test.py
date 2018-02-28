from selenium import webdriver
import time

from selenium.webdriver import ActionChains

driver=webdriver.Firefox()
driver.maximize_window()
driver.get('http://fk.tuqiangol.com/')
time.sleep(1)
d1=driver.find_element_by_id('username')
d1.clear()
d1.send_keys('syntest')
d2=driver.find_element_by_id('password')
d2.clear()
d2.send_keys('jimi123')
driver.find_element_by_id('loginButton').click()
time.sleep(2)
# d3=driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/ul/li[3]/a/i')
# ActionChains(driver).move_to_element(d3).perform()
# time.sleep(1)
# # driver.find_element_by_css_selector('html body.layui-layout-body div.layui-layout.layui-layout-admin div.layui-header div.layui-layout-right ul.layui-nav.help li.layui-nav-item dl.layui-nav-child.layui-anim.layui-anim-upbit dd a.js-edit-phone').click()
# driver.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/ul/li[3]/dl/dd[2]/a').click()
# time.sleep(1)
# # layui-layer-content
# d4=driver.find_element_by_id('userTel')
# d4.clear()
# d4.send_keys('1319999900000')
# driver.find_element_by_class_name('layui-layer-btn0').click()
# time.sleep(1)
# d5=driver.find_element_by_css_selector('div.layui-layer-content').get_attribute('name')
# print(d5)
# 点击部门管理1
driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/ul/li[1]/a/cite").click()
time.sleep(1)
# 点击部门管理2
driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/ul/li[1]/dl/dd[1]/a/cite').click()
time.sleep(2)
# 进入第一个iframe
driver.switch_to.frame('myframe')
# 点击新增部门
driver.find_element_by_xpath('//button[contains(@data-type,"toAddOrg")]').click()
time.sleep(2)
# 进入第二层iframe
ele = driver.find_element_by_xpath('//iframe[(@scrolling="auto")]')
driver.switch_to.frame(ele)
# driver.switch_to.frame('layui-layer-iframe1')
time.sleep(1)
# js移除readonly属性
# js='document.getElementById("orgSupName").removeAttribute("readonly");'
# driver.execute_script(js)
# 定位上级部门输入框清除内容
text = driver.find_element_by_id('orgSupName').get_attribute('value')
print(text)