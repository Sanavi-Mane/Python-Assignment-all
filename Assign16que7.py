def Check(num):
    
    if (num % 5 == 0 ):
        return True
    else :
        return False

def main():
    value = int(input("Enter a number : "))
    Ret = Check(value)
    print(Ret)

if __name__ == "__main__":
    main() 