def additionfact(num):
    Sum  = 0
    for i in range(1, num):
        if num % i == 0:
            Sum = Sum + i
    return Sum 

def main():
    number = int(input("Enter a number : "))
    result = additionfact(number)

    print("Addition of factors is : ",result)
if __name__ == "__main__":
    main()