def main():
    try :
    
        source = input("Enter source file name: ")
        destination = input("Enter destination file name: ")

        file1 = open(source, "r")
        file2 = open(destination, "w")

        for line in file1:
            file2.write(line)

        file1.close()
        file2.close()

        print("Contents copied successfully.")

    except FileNotFoundError as file :
                print("File is not present in current directory")

if __name__ == "__main__":
    main()