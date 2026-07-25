def main():
    try :
    
        Filename = input("Enter filename : ")

        file = open(Filename ,"r")

        count = 0

        for lines in Filename:
            count = count + 1

        file.close()
        print( "number of lines in file", Filename,"=" ,count)

    except FileNotFoundError as file :
        print("File is not present in current directory")

if __name__ == "__main__":
    main()


    
