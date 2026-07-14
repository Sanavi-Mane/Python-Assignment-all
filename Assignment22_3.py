from multiprocessing import Pool

def CountPrime(n):

    count = 0

    for i in range(2, n + 1):

        prime = True

        for j in range(2, int(i ** 0.5) + 1):

            if i % j == 0:
                prime = False
                break

        if prime:
            count = count + 1

    return count

def main():

    size = int(input("Enter size : "))

    Data = []

    print("Enter numbers:")

    for i in range(size):
        no = int(input())
        Data.append(no)

    print("Input List :", Data)

    p = Pool()
    Result = p.map(CountPrime, Data)

    print("\nPrime Counts")

    for i in range(size):
        print("Prime numbers between 1 and", Data[i], "=", Result[i])

if __name__ == "__main__":
    main()                     