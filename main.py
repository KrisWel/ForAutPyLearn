class Calculator:
    def __init__(self):
        pass

    def add(self, number1, number2):
        return number1 + number2

    def sub(self, number1, number2):
        return number1 - number2

    def mult(self, number1, number2):
        return number1 * number2

    def div(self, number1, number2):
        if number2 != 0:
            return number1 / number2
        else:
            return "Error"


if __name__ == '__main__':
    calc = Calculator()
    '''
    print(calc.add(2, 3))
    print(calc.sub(2, 3))
    print(calc.mult(2, 3))
    print(calc.div(2, 3))
    print(calc.div(2, 0))
    '''

    while True:
        print("Calculator:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Divide")

        decision = int(input("What do you want to do? "))
        number1 = int(input("Number 1: "))
        number2 = int(input("Number 2: "))

        if decision == 1:
            print(calc.add(number1, number2))
        elif decision == 2:
            print(calc.sub(number1, number2))
        elif decision == 3:
            print(calc.mult(number1, number2))
        elif decision == 4:
            print(calc.div(number1, number2))
        else:
            print("Error")
