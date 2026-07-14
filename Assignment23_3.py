from multiprocessing import Pool
import os

def CountEven(num):
    count = 0
    
    for i in range(1, num+1):
        if i % 2 == 0:
            count +=  1

    print("Process id of the process is : ",os.getpid())
    print("Input : ", num)
    print("count of even numbers : ", count)
    
    return count


def main():

    size = int(input("Enter size of the list : "))

    Data = []
    print("Enter elements : ")

    for i in range(size):
        no = int(input())
        Data.append(no)

    p = Pool()

    result = p.map(CountEven , Data)
    
    p.close()
    p.join()

  
    
    

if __name__ == "__main__":
    main()

