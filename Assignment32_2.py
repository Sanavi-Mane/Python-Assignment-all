import time 
import schedule 
from datetime import datetime
import os 

def createlog(filename):

    filelog = "FileSizeLog.txt"

    Ret = filename 
    
    Ret = os.path.exists(filename)
    if  (Ret == False):
            print("There is no such file with name : ", filename)
            return
    
    Ret = os.path.isfile(filename)
    if (Ret == False):
        print("It is not a file with name : ",filename)
        return

    try :

        fobj = open(filelog , "a")
        fobj.write(f"file path : {os.path.abspath(filename)}\n")
        fobj.write(f"file size in bytes : {os.path.getsize(filename)}\n")
        fobj.write(f"Date and time : {datetime.now().strftime('%d-%m-%Y_%H-%M-%S')}\n")
        fobj.close()

        print("File information saved succesfully ")

    except Exception as e:
         print("Error :",e)

def main():

     filename = input("Enter file name : ")

     schedule.every(30).seconds.do(createlog , filename)

     while True:
          schedule.run_pending()
          time.sleep(1)


if __name__ == "__main__":
     main()
