from pyse import Pyse, TestCase, TestRunner

import sys, pprint
pprint.pprint(sys.path)

from .. import page

class BaiduTest(TestCase):
    ''' Baidu serach test case'''

    @classmethod
    def setUpClass(cls):
        cls.driver = Pyse("chrome")

    def test_case(self):
        ''' baidu search key : pyse '''
        bd = page.Baidu_page.BaiduPage(self.driver)
        bd.open()
        bd.search_input("pyse")
        bd.search_button()
        self.assertTitle("pyse_百度搜索")


if __name__ == '__main__':
    runner = TestRunner()
    runner.debug()  # debug 模拟不会生成测试报告


