from selenium.webdriver.common.by import By
from pom.base_page import BasePage
from pom.home_page import HomePage

class LoginPage(BasePage):

    def user_login_with_username_password(self, username, password):
        """
          输入用户名和密码
          :param username:
          :param password:
          :return:
        """
        u_input = self.driver.find_element(By.XPATH, '//input[@id="name"]')
        u_input.clear()
        u_input.send_keys(username)

        p_input = self.driver.find_element(By.XPATH, '//input[@id="pass"]')
        p_input.clear()
        p_input.send_keys(password)

        self.driver.find_element(By.XPATH, '//*[@value="登录"]').click()

    def get_login_fail_msg(self):
        return self.driver.find_element(By.XPATH, '//div[@class="alert alert-error"]/strong').text

if __name__=='__main__':
    hp = HomePage()
    hp.click_link_new_page_by_text('登录')
    lp = LoginPage()
    lp.user_login_with_username_password('helloworld', '123456')