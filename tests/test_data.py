import calculator.logic

class Testcals:
    def test_mathod1(self):
        assert calculator.logic.add(3,5) == 8
    
    def test_mathod2(self):
        assert calculator.logic.subtract(5,3) == 2
    
    def test_mathod3(self):
        assert calculator.logic.multiply(3,5) == 15
    
    def test_mathod4(self):
        assert calculator.logic.divide(8,4) == 2
    


if __name__ == '__main__':
    Testcals.test_method()