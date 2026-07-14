from multiprocessing import Pool

def SumSquare(num):
    sum = 0
    
    for i in range(1, num +1):
        sum = sum + (i *i)

    return sum

def main():

    size = int(input("Enter size of the list : "))

    Data = []
    print("Enter elements : ")

    for i in range(size):
        no = int(input())
        Data.append(no)

    print("Input list : ",Data)

    p = Pool()

    result = p.map(SumSquare , Data)

    print("Square of list is : ", result)

if __name__ == "__main__":
    main()

