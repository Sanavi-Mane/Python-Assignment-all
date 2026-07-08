def main():
    num = int(input("Enter a number : "))
    
    fact = 1

    if num <0 :
        print("Negative number !!")
    elif num == 0 :
        print("Factorial of 0 is 1")
    else : 
        for i in range(1, num+1):
            fact *= i
        print(f"The factorial if {num} is {fact}")


if __name__ == "__main__":
    main()