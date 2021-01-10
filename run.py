"""
组织测试用例集
"""
import unittest
from BeautifulReport import BeautifulReport

from pom.base_page import BasePage
from testcases.test_create_topic import TestTopics

def sample_testing():
    # 创建测试用例集
    suite = unittest.TestSuite()
    # 创建单个测试用例
    suite.addTest(TestTopics('test_create_topic'))
    return suite

def regression_testing():
    """
    运行testcases下所有的测试用例方法
    :return:
    """
    suite = unittest.TestSuite()
    # 创建测试用例加载器
    loader = unittest.TestLoader()
    tests = loader.discover('testcases', pattern='test_*.py')  # 加载testcases目录下所有test_开头的python文件
    suite.addTests(tests)
    return suite

def smoke_testing():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    tests = loader.loadTestsFromTestCase(TestTopics)  # 传入类名，根据类型加载所有测试用例
    suite.addTests(tests)
    return suite

if __name__ == '__main__':
    # 创建unittest runner
    # runner = unittest.TextTestRunner(verbosity=2) # 设置相信日志信息

    # 设置测试用例集
    suite = sample_testing()
    # runner.run(suite)
    runner = BeautifulReport(suite)
    import os
    reports = os.path.join(os.path.dirname(__file__),'reports')
    if not os.path.exists(reports):
        os.mkdir(reports)
    import time
    filename = time.strftime('%Y_%m_%d_%H_%M_%S')
    file = os.path.join(reports,filename)
    # runner.report(filename=file, description='抽样测试')
    runner.report(filename=f'reports/{filename}.html', description='抽样测试')
    BasePage.DRIVER.quit()
    BasePage.DRIVER = None