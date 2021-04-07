import pytest
def fun(x):
    return x + 1
# 参数化，a（argnames）参数化的变量，b（argvalues）
@pytest.mark.parametrize('a,b',[(1,2),(10,20),('a','a1')])
def test_answer(a,b):
    assert fun(a) == b

def test_answer1(a,b):
    assert fun(a) == b

def test_answer2(a,b):
    assert fun(a) == b

@pytest.fixture()
def login():
    username = "JK"
    return username

class TestDemo:
    def test_a(self,login):
        print(f"a username = {login}")
    def test_b(self):
        print("b")
    def test_c(self,login):
        print(f"c username = {login}")

if __name__=='main':
    pytest.main(['test_a.py::TestDemo','-v'])