def main():
    num = int(input("Enter number : "))

    count = 0

    while num > 0:
        count += 1
        num = num // 10

    print("Number of digits : ", count)

if __name__ == "__main__":
    main()