import unittest
import time, os
from pom.base_page import BasePage
from pom.home_page import HomePage
from pom.login_page import LoginPage


class MyBaseCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.hp = HomePage()
        cls.lp = LoginPage()
        cls.hp.click_link_new_page_by_text('登录')
        cls.lp.user_login_with_username_password('fanmao1', '123456')

    @classmethod
    def tearDownClass(cls) -> None:
        # BasePage.DRIVER.quit()
        # BasePage.DRIVER = None
        BasePage.DRIVER.delete_all_cookies()
        BasePage.DRIVER.get('http://49.233.108.117:3000/')

    def tearDown(self) -> None:
        print('每个用例运行执行之后添加截图')
        import time
        day = time.strftime('%Y_%m_%d')
        current_time = time.strftime('%H_%M_%S')
        screenshots = os.path.join(os.path.dirname(__file__), f'../screenshots/{day}')
        if not os.path.exists(screenshots):
            os.makedirs(screenshots)
        png_file = os.path.join(screenshots, current_time + ".png")
        self.lp.driver.save_screenshot(png_file)
        self.lp.driver.delete_all_cookies()