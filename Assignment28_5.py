def main():
    filename = input("Enter file name: ")
    word = input("Enter word to search: ")

    try:
        file = open(filename, "r")

        found = False

        for line in file:
            words = line.split()

            if word in words:
                found = True
                break

        file.close()

        if found:
            print(word, "is present in", filename)
        else:
            print(word, "is not present in", filename)

    except FileNotFoundError:
        print("File is not present in the current directory.")

if __name__ == "__main__":
    main()