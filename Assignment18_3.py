def main():
    size = int(input("Enter number of elements : "))

    data = []

    print("Enter elements :")

    for i in range(size):
        no = int(input())
        data.append(no)

    print("Minimum number :", min(data))

if __name__ == "__main__":
    main()