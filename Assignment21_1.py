import threading

def ChkPrime(no):
    if no < 2:
        return False

    for i in range(2, no):
        if no % i == 0:
            return False

    return True


def Prime(data):
    print("Prime Numbers are : ")
    for i in data:
        if ChkPrime(i):
            print(i, end=" ")
    print()


def NonPrime(data):
    print("Non-Prime Numbers are : ")
    for i in data:
        if not ChkPrime(i):
            print(i, end=" ")
    print()


def main():
    size = int(input("Enter number of elements : "))

    arr = []

    print("Enter elements :")
    for i in range(size):
        arr.append(int(input()))

    T1 = threading.Thread(target=Prime, args=(arr,))
    T2 = threading.Thread(target=NonPrime, args=(arr,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()



if __name__ == "__main__":
    main()