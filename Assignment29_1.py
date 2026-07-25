import os

def main():
    filename = input("Enter file name: ")

    if os.path.exists(filename):
        print(filename, "exists in the current directory.")
    else:
        print(filename, "does not exist in the current directory.")

if __name__ == "__main__":
    main()