class Calculator:
    def __init__(self,input1,input2):
        self.input1 = input1
        self.input2 = input2
    def add(self):
        return self.input1 + self.input2
    def substract(self):
        return self.input1 - self.input2
    def multiply(self):
        return self.input1 * self.input2
    def divide(self):
        return self.input1 / self.input2

class ChildCalculator(Calculator):
    def __init__(self,input1, input2):
        super().__init__(input1, input2)
    def multiply(self):
        print(" the multiplication result is ",self.input1 * self.input2)
    def divide(self):
        print(" the division result is ",self.input1 / self.input2)

def main():
    calc1 = Calculator(5,4)
    childcalc1= ChildCalculator(4,3)
    print("Calculator class multiply function : ",calc1.multiply())
    print("ChildCalculator class multiply function : ",end='')
    childcalc1.multiply()

    
if __name__ == "__main__":
    main()
