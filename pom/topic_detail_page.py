from selenium.webdriver.common.by import By

from pom.base_page import BasePage


class TopicDetailPage(BasePage):

    def get_title_text(self):
        return self.driver.find_element(By.XPATH, '//span[@class="topic_full_title"]').text

    def get_tab_text(self):
        ele_text: str = self.driver.find_element(By.XPATH, '//div[@class="changes"]/span[last()]').text
        return ele_text.split(' ')[-1]

    def get_content_text(self):
        return self.driver.find_element(By.XPATH, '//div[@class="topic_content"]').text