import threading

def Maximum(data):
    print("Maximum element : ", max(data))


def Minimum(data):
    print("Minimum element : ", min(data))


def main():
    size = int(input("Enter number of elements : "))

    arr = []

    print("Enter elements :")
    for i in range(size):
        arr.append(int(input()))

    T1 = threading.Thread(target=Maximum, args=(arr,))
    T2 = threading.Thread(target=Minimum, args=(arr,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()


if __name__ == "__main__":
    main()