from multiprocessing import Pool
import os

def SumOdd(num):
    sum = 0
    for i in range(1, num+1, 2):
        sum = sum + i
    
    print("Process id of the process is : ",os.getpid())
    print("Input : ", num)
    print("Sum of odd numbers : ", sum)
    print()
    
    return sum

def main():

    Data = [10 , 20 , 30 , 40]

    print(Data)

    p = Pool()

    result = p.map(SumOdd,Data)

    p.close()
    p.join()

    print("result :",result)

if __name__ == "__main__":
    main()

