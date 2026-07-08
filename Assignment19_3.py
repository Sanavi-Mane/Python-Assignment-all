from functools import reduce

def main():

    size = int(input("Enter number of elements : "))

    data = [ ]
    print("Enter elements : ")

    for i in range(size):
        no = int(input())
        data.append(no)


    print("Input List : ", data)

    FData = list(filter(lambda No: No >= 70 and No <= 90, data))
    print("List after Filter : ", FData)

    MData = list(map(lambda No: No + 10, FData))
    print("List after Map : ", MData)

    RData = reduce(lambda A, B: A * B, MData)

    print("Output of Reduce : ", RData)

if __name__ == "__main__":
    main()