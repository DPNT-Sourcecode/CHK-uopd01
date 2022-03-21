from lib.solutions.CHK.checkout_solution import checkout
from solutions.CHK import checkout_solution


class TestChk:
    def test_chk(self):
        assert checkout_solution.checkout("AB") == 80
        assert checkout_solution.checkout("AAABB") == 175
        assert checkout_solution.checkout("AAAABBBC") == 130 + 50 + 45 + 30 + 20

        assert checkout_solution.checkout("") == -1
        assert checkout_solution.checkout("A") == 50
        assert checkout_solution.checkout("B") == 30
        assert checkout_solution.checkout("C") == 20
        assert checkout_solution.checkout("D") == 15
        assert checkout_solution.checkout("a") == -1
        assert checkout_solution.checkout("-") == -1
        assert checkout_solution.checkout("ABCa") == -1
        assert checkout_solution.checkout("AxA") == -1
        assert checkout_solution.checkout("ABCD") == -1
        assert checkout_solution.checkout("A") == 50
        assert checkout_solution.checkout("AA") == -1
        assert checkout_solution.checkout("AAA") == -1
        assert checkout_solution.checkout("AAAA") == -1
        assert checkout_solution.checkout("AAAAA") == -1
        assert checkout_solution.checkout("AAAAAA") == -1
        assert checkout_solution.checkout("B") == 30
        assert checkout_solution.checkout("BB") == -1
        assert checkout_solution.checkout("BBB") == -1
        assert checkout_solution.checkout("BBBB") == -1
        assert checkout_solution.checkout("ABCDABCD") == -1
        assert checkout_solution.checkout("BABDDCAC") == -1
        assert checkout_solution.checkout("AAABB") == -1
        assert checkout_solution.checkout("ABCDCBAABCABBAAA") == -1


