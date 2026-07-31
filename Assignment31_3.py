import os
import schedule
import time
from datetime import datetime

def Directory_Scanner():

    if not os.path.exists("Sanavi"):
        print("Directory does not exist")
        return
    
    
    for FolderName , SubFolder , FileName in os.walk("Sanavi"):
        print("Directory  Name : ", FolderName)

        print("Number of Files : ", len(FileName))
        
        print("Number of SubDirectories : ",len(SubFolder))

    current_time = datetime.now().strftime("%d-%m-%Y_%H:%M:%S_%p")
    print("scanned Date and Time : ",current_time )
    print("-"*50)
        

def main():

    print("scheduling started")

    schedule.every(1).minutes.do(Directory_Scanner)

    while True:
        schedule.run_pending()
        time.sleep(1)
       
if __name__ == "__main__":
    main()