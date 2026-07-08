import threading

def EvenFactor(no):
    sum = 0

    print("Even Factors are:")

    for i in range(1, no + 1):
        if no % i == 0 and i % 2 == 0:
            print(i, end=" ")
            sum += i

    print("Sum of Even Factors : ", sum)


def OddFactor(no):
    sum = 0

    print("Odd Factors are:")

    for i in range(1, no + 1):
        if no % i == 0 and i % 2 != 0:
            print(i, end=" ")
            sum += i

    print("Sum of Odd Factors : ", sum)


def main():
    num = int(input("Enter number : "))

    T1 = threading.Thread(target=EvenFactor, args=(num,))
    T2 = threading.Thread(target=OddFactor, args=(num,))

    T1.start()
    T2.start()

    T1.join()
    T2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()