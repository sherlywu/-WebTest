from pom.topic_detail_page import TopicDetailPage
from testcases.basecase import MyBaseCase

class TestReply(MyBaseCase):

    def test_reply(self):
        # 登录成功之后 从首页点开第一个话题，进行回复
        self.hp.click_topic_link_by_index()
        tpdetail = TopicDetailPage()
        tpdetail.reply_topic('xxxxxxxxxxxxxxx')
        # 添加断言