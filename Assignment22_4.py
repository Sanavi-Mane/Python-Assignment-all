from multiprocessing import Pool
import time

def SumOfPower5(n):

    total = 0

    for i in range(1, n + 1):
        total = total + (i ** 5)

    return total


def main():

    size = int(input("Enter size of list : "))

    Data = []

    print("Enter numbers:")

    for i in range(size):
        no = int(input())
        Data.append(no)

    print("Input List :", Data)

    start = time.time()

    with Pool() as p:
        Result = p.map(SumOfPower5, Data)

    end = time.time()

    print("\nResults")

    for i in range(size):
        print("Sum of 5th powers from 1 to", Data[i], "=", Result[i])

    print("\nExecution Time :", end - start, "seconds")


if __name__ == "__main__":
    main()