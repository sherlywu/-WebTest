import unittest

from pom.create_topic_page import CreateTopicPage
from pom.home_page import HomePage
from pom.login_page import LoginPage
from pom.topic_detail_page import TopicDetailPage
from testcases.basecase import MyBaseCase


class TestTopics(MyBaseCase):

    def test_create_topic(self):
        self.cp = CreateTopicPage()
        self.tpdetails = TopicDetailPage()
        self.hp.click_create_topic_btn()
        self.cp.create_topic_contents('分享', '自动化测试', '自动化测试用例')

        # 添加断言
        self.assertEqual(self.tpdetails.get_title_text(), '自动化测试')
        self.assertEqual(self.tpdetails.get_tab_text(), '分享')
        self.assertEqual(self.tpdetails.get_content_text(), '自动化测试用例')


if __name__ == '__main__':
    unittest.main()