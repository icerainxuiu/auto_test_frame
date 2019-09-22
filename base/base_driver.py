from selenium import webdriver


class DriverUtil(object):
    _driver = None
    _auto_quit = True
    @classmethod
    def get_driver(cls):
        if cls._driver is None:
            cls._driver = webdriver.Chrome()

        return cls._driver

    @classmethod
    def quit_driver(cls):
        if cls._auto_quit and cls._driver:
            cls._driver.quit()
            cls._driver = None

    @classmethod
    def set_auto_quit(cls, flag):
        cls._auto_quit = flag
