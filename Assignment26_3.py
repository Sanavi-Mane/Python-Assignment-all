class Arithmetic:

    # Constructor
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    # Accept values from user
    def Accept(self):
        self.Value1 = int(input("Enter first number : "))
        self.Value2 = int(input("Enter second number : "))

    # Addition
    def Addition(self):
        return self.Value1 + self.Value2

    # Subtraction
    def Subtraction(self):
        return self.Value1 - self.Value2

    # Multiplication
    def Multiplication(self):
        return self.Value1 * self.Value2

    # Division
    def Division(self):
        if self.Value2 == 0:
            return "Division by zero is not possible"
        else:
            return self.Value1 / self.Value2


def main():

    size = int(input("Enter number of objects : "))

    Objects = []

    for i in range(size):
        print("\nEnter values for Object", i + 1)

        obj = Arithmetic()
        obj.Accept()
        Objects.append(obj)

    print("\n------ Results ------\n")

    for i, obj in enumerate(Objects, start=1):
        print("Object", i)
        print("Addition       :", obj.Addition())
        print("Subtraction    :", obj.Subtraction())
        print("Multiplication :", obj.Multiplication())
        print("Division       :", obj.Division())
        print()


if __name__ == "__main__":
    main()