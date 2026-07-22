class Numbers:

    # Constructor
    def __init__(self, Value):
        self.Value = Value

    # Check Prime Number
    def ChkPrime(self):
        if self.Value <= 1:
            return False

        for i in range(2, int(self.Value ** 0.5) + 1):
            if self.Value % i == 0:
                return False

        return True

    # Check Perfect Number
    def ChkPerfect(self):
        Sum = 0

        for i in range(1, self.Value):
            if self.Value % i == 0:
                Sum = Sum + i

        if Sum == self.Value:
            return True
        else:
            return False

    # Display Factors
    def Factors(self):
        print("Factors are :", end=" ")

        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                print(i, end=" ")

        print()

    # Sum of Factors
    def SumFactors(self):
        Sum = 0

        for i in range(1, self.Value + 1):
            if self.Value % i == 0:
                Sum = Sum + i

        return Sum


def main():

    size = int(input("Enter number of objects : "))

    Objects = []

    for i in range(size):
        print("\nEnter number for Object", i + 1)
        no = int(input("Enter number : "))

        obj = Numbers(no)
        Objects.append(obj)

    print("\n========== Result ==========\n")

    for i, obj in enumerate(Objects, start=1):

        print("Object", i)
        print("Number :", obj.Value)

        if obj.ChkPrime():
            print("Prime Number")
        else:
            print("Not Prime Number")

        if obj.ChkPerfect():
            print("Perfect Number")
        else:
            print("Not Perfect Number")

        obj.Factors()

        print("Sum of Factors :", obj.SumFactors())
        print()


if __name__ == "__main__":
    main()