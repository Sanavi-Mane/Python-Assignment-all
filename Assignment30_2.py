import time
import datetime
import schedule

def Display():

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S_%p")
    print("Current Date and Time : ",timestamp)

def main():

    print("Displaying current Date and Time : ")

    schedule.every(1).minute.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()