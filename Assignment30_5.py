import time 
import schedule
from datetime import datetime

def Display():
    current_time = datetime.now().strftime("%d-%m-%Y_%H:%M:%S_%p")

    with open ("Marvellous.txt","a") as fobj:
        fobj.write(f"Task executed at : {current_time}\n")

    print("Task executed at : ",current_time)

def main():

    schedule.every(5).minutes.do(Display)

    print("Schedular started...")

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()