from multiprocessing import Pool
import os

def SumEven(num):
    sum = 0
    
    for i in range(1, num +1):
        if i % 2 == 0:
            sum = sum + i

    return sum

def main():

    size = int(input("Enter size of the list : "))

    Data = []
    print("Enter elements : ")

    for i in range(size):
        no = int(input())
        Data.append(no)

    p = Pool()

    result = p.map(SumEven , Data)

    print("Process id of the process is : ",os.getpid())
    print("Input : ", Data)
    print("Sum of even numbers : ", result)

    

if __name__ == "__main__":
    main()

