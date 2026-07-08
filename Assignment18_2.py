def main():
    size = int(input("Enter number of elements : "))

    data = []

    print("Enter elements :")

    for i in range(size):
        no = int(input())
        data.append(no)

    print("Maximum number :", max(data))

if __name__ == "__main__":
    main()