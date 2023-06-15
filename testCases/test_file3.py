class Test_py03:

    def test_sum_006(self):
        a = 7
        b = 9
        sum = a + b
        print("sum -- >" + str(sum))
        if sum == 16:
            assert True
        else:
            assert False
