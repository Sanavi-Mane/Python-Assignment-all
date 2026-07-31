import os
import schedule
import time
from datetime import datetime

def DeleteEmptyFiles(directory):

    if not os.path.exists(directory):
        print("Directory does not exist.")
        return

    if not os.path.isdir(directory):
        print("Entered path is not a directory.")
        return

    logfile = "DeleteLog.txt"

    fobj =open(logfile, "a") 

    fobj.write("\n----------------------------------------\n")
    fobj.write("Delete Operation : " + datetime.now().strftime("%d-%m-%Y %H:%M:%S") + "\n")

    for FolderName, SubFolders, FileNames in os.walk(directory):

        for file in FileNames:

            filepath = os.path.join(FolderName, file)

            try:
                if os.path.getsize(filepath) == 0:

                    os.remove(filepath)

                    print(file, "Deleted Successfully")

                    fobj.write(filepath + " -Deleted\n")

            except PermissionError:

                print("Permission denied:", filepath)

                fobj.write(filepath + " -Permission Denied\n")

            except Exception as e:

                print("Error:", e)

                fobj.write(filepath + " - Failed : " + str(e) + "\n")


def main():

    directory = input("Enter directory: ")

    schedule.every(1).minutes.do(DeleteEmptyFiles, directory)

    print("Copying Files...")

    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    main()