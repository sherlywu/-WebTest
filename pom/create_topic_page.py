from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from pom.base_page import BasePage
from pom.home_page import HomePage
from pom.login_page import LoginPage


class CreateTopicPage(BasePage):
    def create_topic_contents(self, tab, title, content):
        tab_select = self.driver.find_element(By.ID, "tab-value")
        tab_select.click()
        eles = self.driver.find_elements(By.XPATH, '//*[@id="tab-value"]/option')
        for ele in eles:
            if ele.text == tab:
                ele.click()
                break
        else:
            raise Exception(f'找不到{tab}')

        title_input = self.driver.find_element(By.XPATH, '//*[@id="title"]')
        title_input.clear()
        title_input.send_keys(title)

        content_input = self.driver.find_element(By.XPATH, '//*[@class="CodeMirror-scroll"]')
        content_input.click()

        ac = ActionChains(self.driver)  # 模拟鼠标的方式输入（不是input标签的输入框使用这个方式）
        ac.move_to_element(content_input).send_keys(content).perform()

        self.driver.find_element_by_xpath('//*[@value="提交"]').click()

if __name__ == '__main__':
    hp = HomePage()
    hp.click_link_new_page_by_text('登录')
    lp = LoginPage()
    lp.user_login_with_username_password('fanmao1', '123456')
    hp.click_create_topic_btn()
    cp = CreateTopicPage()
    cp.create_topic_contents('分享', '赵老师很帅', '从0到1搭建自动化测试框架')
