from testcases.basecase import MyBaseCase
from pom.home_page import HomePage
from pom.login_page import LoginPage
import unittest
from ddt import ddt, data, unpack
from common.file_handler import FileHandler

fl = FileHandler()
login_data = fl.read_excel_by_sheet('datadriven.xlsx', '登录')

@ddt
class TestLogin(MyBaseCase):

    @classmethod
    def setUpClass(cls) -> None:
        # 因为不需要登录，覆盖父类中的登录方法
        cls.hp = HomePage()
        cls.lp = LoginPage()
        cls.hp.click_link_new_page_by_text('登录')

    @data(*login_data)
    @unpack
    def test_login(self, username, password, except_val):
        if username == None:
            username = ''
        if password == None:
            password = ''
        self.lp.user_login_with_username_password(username, password)
        result = self.lp.get_login_fail_msg()
        self.assertEqual(result, except_val)

if __name__ == '__main__':
    unittest.main()