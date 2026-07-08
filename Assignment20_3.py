import threading

def EvenList(data):
    sum = 0

    print("Even Elements are:")

    for i in data:
        if i % 2 == 0:
            print(i, end=" ")
            sum += i

    print("Sum of Even Elements : ", sum)


def OddList(data):
    sum = 0

    print("Odd Elements are:")

    for i in data:
        if i % 2 != 0:
            print(i, end=" ")
            sum += i

    print("Sum of Odd Elements : ", sum)


def main():
    size = int(input("Enter number of elements : "))

    arr = []

    print("Enter elements :")

    for i in range(size):
        value = int(input())
        arr.append(value)

    T1 = threading.Thread(target=EvenList, args=(arr,))
    T2 = threading.Thread(target=OddList, args=(arr,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

if __name__ == "__main__":
    main()