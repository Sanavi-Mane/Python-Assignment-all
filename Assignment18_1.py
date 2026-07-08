def main():
    size = int(input("Enter number of elements : "))

    data = []

    print("Enter elements :")

    for i in range(size):
        no = int(input())
        data.append(no)

    total = sum(data)

    print("Addition of all elements : ", total)

if __name__ == "__main__":
    main()