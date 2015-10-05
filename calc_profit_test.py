import unittest 

from general_simulations import calc_profit

class CalcProfitTest(unittest.TestCase):
    def test_calc_profit(self):
        y = [100] * 10
        x = [100, 103, 97, 92, 97,99, 100, 101, 103, 108] 
        result = calc_profit(x, y, thresh=2)
        expected = {"profit": 9, "loss": 5, "profit_from_trading": 14}
        self.assertEquals(result, expected)

def main():
    unittest.main()

if __name__ == "__main__":
    main()
