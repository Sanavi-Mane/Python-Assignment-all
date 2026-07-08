import threading

Sum = 0
Product = 1


def Addition(data):
    global Sum

    for i in data:
        Sum += i


def Multiplication(data):
    global Product

    for i in data:
        Product *= i


def main():
    global Sum
    global Product

    size = int(input("Enter number of elements : "))

    arr = []

    print("Enter elements : ")

    for i in range(size):
        arr.append(int(input()))

    T1 = threading.Thread(target=Addition, args=(arr,))
    T2 = threading.Thread(target=Multiplication, args=(arr,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Sum : ", Sum)
    print("Product : ", Product)


if __name__ == "__main__":
    main()