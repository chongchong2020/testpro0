import pytest

from pythoncode.calculator import Calculator


class TestCalc:
    def setup_class(self):
        self.calc = Calculator()

    @pytest.mark.parametrize("a,b,expect",[(1,2,3),(100,200,300),(300,300,600)])
    def test_add(self,a,b,expect):
        result = self.calc.add(a,b)
        assert result == expect
