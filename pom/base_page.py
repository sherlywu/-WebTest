"""
所有页面类的父类
"""
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
import os


class BasePage:
    DRIVER: WebDriver = None

    def __init__(self):
        driverpath = os.path.join(os.path.dirname(__file__), '../drivers/chromedriver')
        self.driver = BasePage.DRIVER
        if BasePage.DRIVER == None:

            self.driver = webdriver.Chrome(executable_path=driverpath)
            BasePage.DRIVER = self.driver
            self.driver.maximize_window()
            self.driver.implicitly_wait(6)
            self.driver.get("http://49.233.108.117:3000/")
