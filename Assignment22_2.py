from multiprocessing import Pool
import os

def factorial(num):
    
    fact = 1
    for i in range(1, num +1):
        fact = fact * i 

    return fact

def main():

    size = int(input("Enter size of the list : "))

    Data = []
    print("Enter elements : ")

    for i in range(size):
        no = int(input())
        Data.append(no)

    print("Input list : ",Data)

    p = Pool()

    result = p.map(factorial , Data)

    print("Process id of the process is : ",os.getpid())
    print("Input :", Data)
    print("Factorial :", result)

    

if __name__ == "__main__":
    main()

