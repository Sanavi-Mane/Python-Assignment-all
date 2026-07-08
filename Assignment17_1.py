import Arithmetic

def main():

    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))

    print("Addition is : ",Arithmetic.Add(num1,num2))
    print("Subtraction is : ",Arithmetic.Sub(num1,num2))
    print("Multiplication is : ",Arithmetic.Mul(num1,num2))
    print("Division is : ",Arithmetic.Div(num1,num2))

if (__name__) == "__main__":
    main()