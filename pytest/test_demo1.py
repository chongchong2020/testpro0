import pytest

class TestDemo():
    @pytest.mark.smoke
    def test_one(self):
        assert 1==1

    @pytest.mark.king
    def test_two(self):
        assert 2!=3
