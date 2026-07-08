from functools import reduce

def ChkPrime(No):
    if No < 2:
        return False

    for i in range(2, No):
        if No % i == 0:
            return False

    return True

def main():

    size = int(input("Enter number of elements : "))

    data = [ ]

    print("Enter elements : ")

    for i in range(size):
        no = int(input())
        data.append(no)

    print("Input List :", data)

    FData = list(filter(ChkPrime, data))
    print("List after Filter :", FData)

    MData = list(map(lambda No: No * 2, FData))
    print("List after Map :", MData)

    RData = reduce(lambda A, B: A if A > B else B, MData)

    print("Output of Reduce :", RData)

if __name__ == "__main__":
    main()