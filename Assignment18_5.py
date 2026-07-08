import MarvellousNum

def main():
    size = int(input("Enter number of elements : "))

    data = []

    print("Enter elements : ")

    for i in range(size):
        no = int(input())
        data.append(no)

    total = 0

    for value in data:
        if MarvellousNum.ChkPrime(value):
            total = total + value

    print("Addition of prime numbers : ", total)

if __name__ == "__main__":
    main()