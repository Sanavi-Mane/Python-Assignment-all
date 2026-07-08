def main():
    num = int(input("Enter number : "))

    sum = 0

    while num > 0:
        digit = num % 10
        sum = sum + digit
        num = num // 10

    print("Addition of digits : ", sum)

if __name__ == "__main__":
    main()