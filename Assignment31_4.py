import time 
import schedule 
from datetime import datetime

def createlog():

    filename = "MarvellousLog_"+datetime.now().strftime("%d-%m-%Y_%H-%M-%S" )+ ".txt"

    creation_time = datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")

    fobj = open(filename , "w")
    fobj.write("Log file is created successfully \n")
    fobj.write("Creation time : "+ creation_time)

    print(f"{filename}created successffully.")


    
def main():

    print("Log file schedular started ")

    schedule.every(1).minute.do(createlog)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
