import pytest
from  python_testcode.calculator import Calculator

class TestClass():

    def setup_class(self):
        self.cal = Calculator()
        print(" 开始计算")
    def teardoen_class(self):
        print("结束计算")

    #每个test方法前使用
    # def setup_method(self):
    #     print("开始计算")
    # def teardown_method(self):
    #     print("结束计算")

    @pytest.mark.parametrize("a,b,expected", [(1,1,2),(1, -5, -4), (-1, -9, -10),(30,50,80), (10000, 10000, 20000)],ids=["one", "two", "thiret","four","five"])
    def test_add(self,a,b,expected):
        assert self.cal.add(a,b) == expected

    @pytest.mark.parametrize("a,b,expected", [(1,5,-4),(1, 44, -43), (-1, 9, -10),(20,50,-30), (-40000, 10000, -50000)],ids=["one", "two", "thiret","four","five"])
    def test_sub(self,a,b,expected):
        assert self.cal.sub(a,b) == expected

    @pytest.mark.parametrize("a,b,expected", [(0,5,0)])
    def test_mul(self,a,b,expected):
        assert self.cal.mul(a,b) == expected

    @pytest.mark.parametrize("a,b,expected",[(12,4,3),(15,3,5)],ids=["one","two"])
    def test_div(self,a,b,expected):
        assert self.cal.div(a,b) == expected






