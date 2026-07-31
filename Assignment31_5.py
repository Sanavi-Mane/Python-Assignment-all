import time 
import schedule
import os
from datetime import datetime

def createLog(filename):

    if not os.path.exists(filename):
        print("There is no Directory with name : ",filename)
        return

    if not os.path.isdir(filename):
        print("It is not a Directory with name : ",filename)

    filecount = 0

    for FolderName , SubFolder , FileName in os.walk(filename):
        filecount = filecount + len(FileName)

    filelog = "DirectoryCountLog.txt" 

    fobj = open(filelog ,"a")
    fobj.write("---File Scanned---\n")
    fobj.write("-"*50)

    fobj.write(f"\nDirectory Name : {filename}\n")
    fobj.write(f"Number of Files : {filecount}\n")
    fobj.write(f"Date and Time : {datetime.now().strftime('%d-%m-%Y_%H-%M-%S_%p')}\n ")

    fobj.close()

    print("Log file Created successfully...")

   

def main():

    print("-Automation Script Sarted-")

    filename = input("Enter directory name : ")
    
    schedule.every(10).seconds.do(createLog , filename)

    while True:
        schedule.run_pending()
        time.sleep(1)

    
if __name__ == "__main__":
    main()
