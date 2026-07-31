import time 
import schedule
import os 

def filecontent(filename):
    
    if not os.path.exists(filename):
        print("File does not exists ")
        return 

    try :
        fobj = open(filename ,"r")
        content = fobj.read()

        if len(content) == 0:
            print("File is Empty ")
        else :
            print("\n---------File content is---------\n")
            print(content)

    except PermissionError:
        print("Permission Denied to access File")
    except OSError:
        print("File cannot be opened")
        
def main():

    filename = input("Enter a text file name:  ")

    schedule.every(1).minutes.do(filecontent , filename )\

    print("Reading File...")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()