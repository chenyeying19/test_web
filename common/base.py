from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def open_browser( browser="chrome" ):
    """
    打开浏览器
    :return:
    """
    driver=None
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox
    elif browser == "ie":
        driver = webdriver.Ie()
    else:
        print("请输入正确的浏览器名,例如'chrome','firefox','ie'")
    return driver


class Base(object):
    def __init__( self, driver ):
        self.driver = driver

    def open_url( self, url ):
        """
        输入网站
        :param url:网站地址
        :return:
        """
        self.driver.get(url)
        self.driver.maximize_window()

    def close_browser( self ):
        """关闭浏览器"""
        self.driver.quit()

    def find_element( self, locator, timeout=10 ):
        """
        定位一个元素
        :param locator: 定位器,是一个元组
        :param timeout: 等待的最大时间
        :return: 单个元素
        """
        element = WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        return element

    def find_elements( self, locator, timeout=10 ):
        """
        定位一组元素
        :param locator: 定位器,是一个元组
        :param timeout: 等待的最大时间
        :return: 返回一组元素
        """
        elements = WebDriverWait(self.driver, timeout).until(EC.presence_of_all_elements_located(locator))
        return elements

    def click( self, locator, timeout=10 ):
        """

        :param locator: 定位器,是一个元组
        :param timeout: 等待的最大时间
        :return:
        """
        element = self.find_element(locator=locator, timeout=timeout)
        element.click()

    def send_keys( self, locator, text, timeout=10 ):
        """
        输入
        :param locator:定位器,是一个元组
        :param timeout:等待的最大时间
        :return:
        """
        element = self.find_element(locator=locator, timeout=timeout)
        element.clear()
        element.send_keys(str(text))

    def is_text_element( self, locator, text, timeout=10 ):
        """
        判断文本是否在元素中,
        :param locator: 定位器,是一个元组
        :param timeout: 等待的最大时间
        :return:
        """
        try:
            result = WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element(locator, text))
            return result
        except Exception:
            return False

    def is_text_value( self, locator, value, timeout=10 ):
        """
        判断value是否与元素的value值相等
        :param locator: 定位器,是一个元组
        :param timeout: 等待的最大时间
        :param value: value值
        :return:
        """
        try:
            result = WebDriverWait(self.driver, timeout).until(EC.text_to_be_present_in_element_value(locator, value))
            return result
        except Exception:
            return False

# if __name__ == '__main__':
#     driver = open_browser()
#     base = Base(driver)
#     url = "http://localhost:8080/ecshop/user.php"
#     base.open_url(url)
#     time.sleep(2)
#     username_loc = ("name", "username")
#     text = "a1234"
#     base.send_keys(username_loc, text)
#     password_loc = ("name", "password")
#     text2 = "123456"
#     base.send_keys(password_loc, text2)
#     submit_loc = ("name", "submit")
#     base.click(submit_loc)
#     name_text=("class name","f4_b")
#     text1="rrre"
#     result=base.is_text_element(name_text, text1)
#     print(result)
#     time.sleep(3)
#     base.close_browser()
