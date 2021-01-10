from selenium.webdriver.common.by import By
from pom.base_page import BasePage

class HomePage(BasePage):
    def click_link_new_page_by_text(self, text):
        eles = self.driver.find_elements(By.XPATH, '//ul[@class="nav pull-right"]/li')
        for ele in eles:
            if ele.text == text:
                ele.click()
                break
        else:
            raise Exception('找不到页面中元素')

    def click_create_topic_btn(self):
        self.driver.find_element(By.XPATH, '//*[@id="create_topic_btn"]').click()

    def click_topic_link_by_index(self, index=0):
        """
        从首页点开话题详情
        :param index: 0表示第一个话题
        :return:
        """
        pass

if __name__=='__main__':
    hp = HomePage()
    hp.click_link_new_page_by_text('登录')
    hp.click_link_new_page_by_text('注册')
    hp.click_link_new_page_by_text('首页')
