def main():
    try:
        filename = input("Enter file name: ")

        file = open(filename, "r")

        for line in file:
            print(line, end="")

        file.close()
    except FileNotFoundError as file :
            print("File is not present in current directory")

if __name__ == "__main__":
    main()