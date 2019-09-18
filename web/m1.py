# coding:utf8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time


# 添加用户文件配置
op = Options()
op.add_argument('--user-data-dir=C:\\Users\\Will\\AppData\\Local\\Google\\Chrome\\User Data')

# selenium打开浏览器
driver = webdriver.Chrome(options=op, executable_path='../lib/chromedriver')
# 添加隐式等待
driver.implicitly_wait(20)

# 打开网站
driver.get('http://112.74.191.10:8000/')

# 点击登录按钮
# 1.找到元素在哪里
ele = driver.find_element_by_xpath('/html/body/div[1]/div[1]/div/div/div[2]/a[1]')
# 2.点击这个元素
ele.click()

# 输入用户名
driver.find_element_by_xpath('//*[@id="username"]').send_keys('13800138006')
driver.find_element_by_xpath('//*[@id="password"]').send_keys('123456')
driver.find_element_by_xpath('//*[@id="verify_code"]').send_keys('1111')
driver.find_element_by_xpath('//*[@id="loginform"]/div/div[6]/a').click()

# 搜索
driver.find_element_by_xpath('//*[@id="q"]').send_keys('手机')
driver.find_element_by_xpath('//*[@id="sourch_form"]/a').click()

# 购物车
driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/ul/li[1]/div/div[5]/div[2]/a').click()
driver.find_element_by_xpath('//*[@id="join_cart"]').click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="layui-layer1"]/span/a').click()

# 结算
# 悬停
ac = ActionChains(driver)
ac.move_to_element(driver.find_element_by_xpath('//*[@id="hd-my-cart"]/a/div')).perform()
driver.find_element_by_xpath('//*[@id="show_minicart"]/div/div/div[2]/a').click()




