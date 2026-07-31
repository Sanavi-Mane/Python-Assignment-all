import time 
import schedule 
from datetime import datetime

def creation():

    filename = "file_"+datetime.now().strftime("%d-%m-%Y_%H-%M-%S") + ".txt"

    fobj = open(filename ,"w")

    fobj.write(f"filename is : {filename}\n")
    fobj.write(f"Creation date : {datetime.now().strftime('%d-%m-%Y')}\n")
    fobj.write(f"Creation time : {datetime.now().strftime('%H-%M-%S_%p')}\n")

    fobj.close()

    print(f"{filename}created successffully.")

def main():

    print("-scheduling started-")

    schedule.every(1).minutes.do(creation)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()