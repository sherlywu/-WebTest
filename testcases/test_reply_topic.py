import unittest

from pom.base_page import BasePage
from pom.home_page import HomePage
from pom.topic_detail_page import TopicDetailPage
from testcases.basecase import MyBaseCase
from pom.create_topic_page import CreateTopicPage


class TestReply(MyBaseCase, BasePage):

    def test_reply(self):
        self.tpdetails = TopicDetailPage()
        self.rp = CreateTopicPage()
        # self.hp = HomePage()
        # 登录成功之后 从首页点开一个话题，进行回复
        self.hp.click_topic_link_by_index(index=4)
        self.rp.reply_topic('测试自动回复话题')

        # 添加断言
        self.assertEqual(self.tpdetails.get_reply_topic_text(), '测试自动回复话题')

if __name__ == '__main__':
    unittest.main()