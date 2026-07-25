def main():
    filename = input("Enter file name: ")

    try:
        file = open(filename, "r")

        data = file.read()

        print("Contents of file:")
        print(data)

        file.close()

    except FileNotFoundError:
        print("File is not present in the current directory.")

if __name__ == "__main__":
    main()