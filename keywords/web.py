# coding:utf8
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time, traceback


class Web:
    """
    封装常用的Web自动化关键字
    """

    def __init__(self):
        self.driver = None
        self.text = ''

    def openbrowser(self, b=''):
        """
        打开浏览器
        :param b: 标识需要打开的浏览器。默认是谷歌浏览器
                  gc代表谷歌
                  ff代表火狐
                  ie代表ie
        :return: 浏览器的driver对象
        """
        if b == '' or b == 'gc':
            # 添加用户文件配置
            op = Options()
            op.add_argument('--user-data-dir=C:\\Users\\Will\\AppData\\Local\\Google\\Chrome\\User Data')

            # selenium打开浏览器
            self.driver = webdriver.Chrome(options=op, executable_path='./lib/chromedriver')
            self.driver.implicitly_wait(20)
            # self.driver.find_element_by_xpath().text
            # self.driver.switch_to.default_content()
        else:
            print('待实现......')

        return self.driver

    def wait(self,t):
        """
                固定等待的关键字
                :param t: 需要等待的时间
                :return: 是否执行成功
                """
        try:
            t = int(t)
            self.driver.implicitly_wait(t)
        except Exception as e:
            print(traceback.format_exc(e))
            return False

        return True

    def geturl(self, url):
        """
        在浏览器打开网址，需要先打开浏览器
        :param url: 需要打开的网址
        :return: 是否执行成功
        """
        try:
            self.driver.get(url)
        except Exception as e:
            print(traceback.format_exc(e))
            return False

        return True

    def click(self, xpath):
        """
        根据xpath找到元素，并完成对元素点击
        :param xpath: 定位元素的xpath定位器
        :return: 是否执行成功
        """
        try:
            ele = self.driver.find_element_by_xpath(xpath)
            ele.click()
        except Exception as e:
            print(traceback.format_exc(e))
            return False

        return True

    def input(self, xpath, text):
        """
        根据xpath找到元素，并完成对元素输入text文本
        :param xpath: 定位元素的xpath定位器
        :param text: 需要输入的文本
        :return: 是否执行成功
        """
        try:
            ele = self.driver.find_element_by_xpath(xpath)
            ele.send_keys(text)
        except Exception as e:
            print(traceback.format_exc(e))
            return False

        return True

    def sleep(self, t):
        """
        固定等待的关键字
        :param t: 需要等待的时间
        :return: 是否执行成功
        """
        try:
            t = int(t)
            time.sleep(t)
        except Exception as e:
            print(traceback.format_exc(e))
            return False

        return True

    def moveto(self,xpath):
        """
        鼠标移动到元素，并完成悬停操作（悬停的时间只有大概0.5到2s）
        :param xpath: 定位元素的xpath定位器
        :return: 是否执行成功
        """
        try:
            ac = ActionChains(self.driver)
            ac.move_to_element(self.driver.find_element_by_xpath(xpath)).perform()
        except Exception as e:
            print(traceback.format_exc(e))
            return False

        return True

    def gettext(self,xpath):
        """
        根据xpath找到元素，并获取到元素的文本
        :param xpath: 定位元素的xpath定位器
        :return: 是否执行成功
        """
        try:
            ele = self.driver.find_element_by_xpath(xpath)
            self.text = ele.text
        except Exception as e:
            print(traceback.format_exc(e))
            return False

        return True

    def assertequals(self,param,value):
        """
        断言预期结果和实际结果相等
        :param param: 实际结果，支持关联
        :param value: 预期结果
        :return: 断言成功还是失败
        """
        if self.text == value:
            print('PASS')
            return True
        else:
            print('FAIL')
            return False

    def intoiframe(self,xpath):
        """
        进入iframe的关键字
        :param xpath: iframe的定位xpath
        :return: 是否执行成功
        """
        try:
            frame = self.driver.find_element_by_xpath(xpath)
            self.driver.switch_to.frame(frame)
        except Exception as e:
            print(traceback.format_exc(e))
            return False

        return True

    def outiframe(self):
        """
        进入iframe之后，退出到默认网页的方法
        :return: 是否执行成功
        """
        try:
            self.driver.switch_to.default_content()
        except Exception as e:
            print(traceback.format_exc(e))
            return False

        return True