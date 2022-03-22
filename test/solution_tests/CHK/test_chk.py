from lib.solutions.CHK.checkout_solution import checkout


class TestChk:
    def test_chk(self):
        assert checkout("AB") == 80
        assert checkout("AAABB") == 175
        assert checkout("AAAABBBC") == 130 + 50 + 45 + 30 + 20
        assert checkout("") == 0
        assert checkout("A") == 50
        assert checkout("B") == 30
        assert checkout("C") == 20
        assert checkout("D") == 15
        assert checkout("a") == -1
        assert checkout("-") == -1
        assert checkout("ABCa") == -1
        assert checkout("AxA") == -1
        assert checkout("ABCD") == 50 + 30 + 20 + 15
        assert checkout("A") == 50
        assert checkout("AA") == 100
        assert checkout("ABCDABCD") == 215
        assert checkout("BABDDCAC") == 215
        assert checkout("ABCDCBAABCABBAAA") == 200 + 100 + 90 + 30 + 60 + 15
        assert checkout("E") == 40
        assert checkout("ABCDE") == 50 + 30 + 20 + 15 + 40
        assert checkout("ABCDEE") == 50 + 30 * 0 + 20 + 15 + 2 * 40

        assert checkout("AAAAA") == 200
        assert checkout("AAAAAA") == 250
        assert checkout("AAAAAAA") == 300
        assert checkout("AAAAAAAA") == 330
        assert checkout("AAAAAAAAA") == 380
        assert checkout("AAAAAEEBAAABB") == 455

        assert checkout("ABCDEF") == 50 + 30 + 20 + 15 + 40 + 10
        assert checkout("ABCDEFF") == 50 + 30 + 20 + 15 + 40 + 20
        assert checkout("ABCDEFFF") == 50 + 30 + 20 + 15 + 40 + 20
        assert checkout("ABCDEFFFF") == 50 + 30 + 20 + 15 + 40 + 30
        assert checkout("ABCDEFFFFF") == 50 + 30 + 20 + 15 + 40 + 40
        assert checkout("ABCDEFFFFFF") == 50 + 30 + 20 + 15 + 40 + 40

        assert checkout("2K") == 120
