import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from base.base_driver import DriverUtil


class Action(object):
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, feature, timeout=10, poll=0.5):
        """
        通过对象特征查找对应元素并返回，特征为元组，可填范围("id","class","css","link","partial","xpath","tag","name")
        :param feature: 二元元组，值1范围("id","class","css","link","partial","xpath","tag","name"),值2为值一对应的值
        :param timeout:
        :param poll:
        :return: element
        """
        feature_dict = {
            "id": By.ID,
            "class": By.CLASS_NAME,
            "css": By.CSS_SELECTOR,
            "link": By.LINK_TEXT,
            "partial": By.PARTIAL_LINK_TEXT,
            "xpath": By.XPATH,
            "tag": By.TAG_NAME,
            "name": By.NAME
        }

        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(
            lambda x: x.find_element(feature_dict[feature[0]], feature[1]))

    def find_elements(self, feature, timeout=10, poll=0.5):
        """
        通过对象特征查找对应元素并返回元素列表，特征为元组，可填范围("id","class","css","link","partial","xpath","tag","name")
        :param feature: 二元元组，值1范围("id","class","css","link","partial","xpath","tag","name"),值2为值一对应的值
        :param timeout:
        :param poll:
        :return: elements
        """
        FEATURE_DICT = {
            "id": By.ID,
            "class": By.CLASS_NAME,
            "css": By.CSS_SELECTOR,
            "link": By.LINK_TEXT,
            "partial": By.PARTIAL_LINK_TEXT,
            "xpath": By.XPATH,
            "tag": By.TAG_NAME,
            "name": By.NAME
        }

        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(
            lambda x: x.find_elements(FEATURE_DICT[feature[0]], feature[1]))

    def element_click(self, feature):
        self.find_element(feature).click()

    # def scroll_find_element(self, feature, direction=(0, 400)):
    #     java_script = "window.scrollTo({})".format(direction)
    #     page_source_get = ""
    #     while True:
    #         try:
    #             return self.find_element(feature)
    #         except BaseException:
    #             self.driver.execute_script(java_script)
    #             if page_source_get == self.driver.page_source:
    #                 print("到底了")
    #                 break
    #             page_source_get = self.driver.page_source

    def scroll_to_down(self, direction=(0, 10000)):
        time.sleep(2)
        java_script = "window.scrollTo{}".format(direction)
        self.driver.execute_script(java_script)

    def get_element_text(self, feature):
        return self.find_element(feature).text

    def window_max(self):
        self.driver.maximaze_window()

    def forward(self):
        self.driver.forward()


if __name__ == '__main__':
    driver1 = DriverUtil().get_driver()
    driver1.get("http://www.baidu.com")
    action = Action(driver1)

    element = action.find_element(("id", "kw"))
    element.send_keys("python")

    action.scroll_to_down()
    element2 = action.find_element(("partial", "下一页"))
    element2.click()
    time.sleep(10)
    DriverUtil().quit_driver()
