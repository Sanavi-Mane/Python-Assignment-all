def CheckPrime(num):
    

    if (num <= 1):
        print(" is not a  prime number ")
        return

    else:
        for i in range(2, num):
            if num % i == 0:
                print(" is not a prime number ")
                return
        print("IS a prime number ")

def main():
    value = int(input("Enter a number : "))
    CheckPrime(value)
    


if __name__ == "__main__":
    main()