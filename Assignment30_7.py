import os
import shutil
import schedule
import time
from datetime import datetime

def BackupFile(source , destination):

    if not os.path.isfile(source): 
        print("Source file does not exist")

    filename = os.path.basename(source)
    name , extention = os.path.splitext(filename)

    timestamp = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")

    backup_filename = name + "_"+timestamp + extention

    destination_file = os.path.join(destination ,backup_filename)

    shutil.copy2(source , destination_file)

    print("Backup created : ",backup_filename)

    with open("backup_log.txt","a") as file:
        log = datetime .now().strftime("%d-%m-%y_%H:%M:%S_%p")
        file.write(f"Backup completed successfully at {log}\n")

def main():

    source = input("Enter source file path : ")
    destination = input("Enter destination folder path : ")

    schedule.every(1).hours.do(BackupFile, source, destination)

    print("Backup schedular started...")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()