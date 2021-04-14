import pytest

def setup_module():
    print("\nsetup_module:该文件所有用例执行前执行")

def teardown_module():
    print("\nteardown_module:该文件所有用例执行后执行")

def setup_function():
    print("\nsetup_function：不在类中的用例执行前执行")

def teardown_function():
    print("\ntear_function:不在类中的用例后执行")
def test_three():
    print("正在执行test_three")

def test_four():
    print("正在执行test_four")

class TestClass():

    def setup_class(self):
        print("\nsetup_class:所有用例执行前执行")

    def teardown_class(self):
        print("\nteardown_class:所有用例结束后执行")

    def setup_method(self):
        print("\nsetup_method:每个用例结束后执行")
    def teardown_method(self):
        print("\nteardown_method:每个用例结束时执行")

    def test_one(self):
        print("正在执行test_one")

    def test_two(self):
        print("正在执行test_two")