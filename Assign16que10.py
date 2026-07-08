def CheckLength(name):
    return len(name)
def main():
    name = input("Enter your name : ")

    Ret = CheckLength(name)

    print("Length od name is : ", Ret)

if __name__ == "__main__":
    main()