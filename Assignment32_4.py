import os 
import time 
import schedule
import shutil
from datetime import datetime 

def filecopy(Source , Destination):

    if not os.path.exists(Source):
        print("The source Directory does not exists ")
        return
    
    if not os.path.isdir(Source):
        print("The Source file entered is not a Directory ")
        return

    if not os.path.exists(Destination):
        print("The Destination file does not exists")
        return
    
    if not os.path.isdir(Destination):
        print("The destination file entered is not a diresctory ")
        return

    logfile = "copylog.txt"

    fobj = open(logfile , "a")
    fobj.write("--------------copied Files--------------")
    fobj.write("Copy operation : " + datetime.now().strftime("%d-%m_%Y_%H:%M:%S")+"\n")

    for file in os.listdir(Source):
        Source_path = os.path.join(Source , file)

        if os.path.isfile(Source_path) and file.endswith(".txt"):
            Destination_path = os.path.join(Destination , file)

            try :
                shutil.copy2(Source_path , Destination_path)

                print( file , "Copied Successfully \n")

                fobj.write(file + " -copied successfully \n")

            except :
                print("Cannot copy : ",file)

                fobj.write(file + " -failed \n")

def main():

    Source = input("Enter source Directory : ")
    Destination = input("Enter Destination Directory : ") 

    schedule.every(1).minutes.do(filecopy , Source = Source , Destination = Destination)

    print("copying files...")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
