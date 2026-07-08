def main():
    size = int(input("Enter number of elements : "))

    data = []

    print("Enter elements : ")

    for i in range(size):
        no = int(input())
        data.append(no)

    search = int(input("Enter element to search : "))

    frequency = data.count(search)

    print("Frequency : ", frequency)

if __name__ == "__main__":
    main()