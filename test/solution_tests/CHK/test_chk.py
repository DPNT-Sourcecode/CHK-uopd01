from lib.solutions.CHK.checkout_solution import checkout
from solutions.CHK import checkout_solution


class TestChk:
    def test_chk(self):
        assert checkout_solution.checkout("AB") == 80
        assert checkout_solution.checkout("AAABB") == 175
        assert checkout_solution.checkout("AAAABBBC") == 130 + 50 + 45 + 30 + 20

        assert checkout_solution.checkout("") == 0
        assert checkout_solution.checkout("A") == 50
        assert checkout_solution.checkout("B") == 30
        assert checkout_solution.checkout("C") == 20
        assert checkout_solution.checkout("D") == 15
        assert checkout_solution.checkout("a") == -1
        assert checkout_solution.checkout("-") == -1
        assert checkout_solution.checkout("ABCa") == -1
        assert checkout_solution.checkout("AxA") == -1
        assert checkout_solution.checkout("ABCD") == 50 + 30 + 20 + 15
        assert checkout_solution.checkout("A") == 50
        assert checkout_solution.checkout("AA") == 100
        assert checkout_solution.checkout("ABCDABCD") == 215
        assert checkout_solution.checkout("BABDDCAC") == 215
        assert checkout_solution.checkout("ABCDCBAABCABBAAA") == 495

        assert checkout_solution.checkout("E") == 40
        assert checkout_solution.checkout("ABCDE") == 50 + 30 + 20 + 15 + 40
        assert checkout_solution.checkout("ABCDEE") == 50 + 30 * 0 + 20 + 15 + 2 * 40

        assert checkout_solution.checkout("AAAAA") == 200
        assert checkout_solution.checkout("AAAAAA") == 250
        assert checkout_solution.checkout("AAAAAAA") == 300
        assert checkout_solution.checkout("AAAAAAAA") == 330
        assert checkout_solution.checkout("AAAAAAAAA") == 380
        assert checkout_solution.checkout("AAAAAEEBAAABB") == 455


