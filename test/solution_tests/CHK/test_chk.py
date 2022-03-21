from lib.solutions.CHK.checkout_solution import checkout
from solutions.CHK import checkout_solution


class TestChk:
    def test_chk(self):
        assert checkout_solution.checkout("AA,BB") == -1
        assert checkout_solution.checkout("A,B") == 80
        assert checkout_solution.checkout("A,A,A,B,B") == 175
        assert checkout_solution.checkout("A,A,A,A,B,B,B,C") == 130 + 50 + 45 + 30 + 20

