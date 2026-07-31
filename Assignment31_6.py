import schedule
import time 

def mon():
    print("Start your weekly goal.")

def wed():
    print("Review your weekly progress.")

def fri():
    print("Weekly work completed ")

def main():

    print("Scheduling started")

    schedule.every().monday.at("09:00").do(mon)

    schedule.every().wednesday.at("17:00").do(wed)

    schedule.every().friday.at("18:00").do(fri)

    while True:
        schedule.run_pending()
        time.sleep(1)
        
if __name__ == "__main__":
    main()
