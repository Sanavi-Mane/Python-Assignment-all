Multiply = lambda A, B: A * B

def main():
    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))

    result = Multiply(num1, num2)

    print("Multiplication : ", result)

if __name__ == "__main__":
    main()