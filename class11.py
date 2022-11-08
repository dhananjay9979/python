class Calculator:

    def __init__(self):
        self.x = input("Enter the first value: ")
        self.y = input("Enter the second value: ")

    def addition(self):
        self.value = float(self.x) + float(self.y)
        print("Addition of ", self.x, " and ", self.y, " = ", self.value)

    def subtraction(self):
        self.value = float(self.x) - float(self.y)
        print("Subtraction of ", self.x, " and ", self.y, " = ", self.value)

    def multiplication(self):
        self.value = float(self.x) * float(self.y)
        print("Multiplication of ", self.x, " and ", self.y, " = ", self.value)

    def division(self):
        self.value = float(self.x) / float(self.y)
        print("Division of ", self.x, " and ", self.y, " = ", self.value)

calc = Calculator()
calc.addition()
calc.subtraction()
calc.multiplication()
calc.division()