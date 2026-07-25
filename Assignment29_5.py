def main():
    filename = input("Enter file name: ")
    word = input("Enter word to search: ")

    try:
        file = open(filename, "r")

        count = 0

        for line in file:
            words = line.split()

            for w in words:
                if w == word:
                    count += 1

        file.close()

        print(word, "appears", count, "times in", filename)

    except FileNotFoundError:
        print("File is not present in the current directory.")

if __name__ == "__main__":
    main()