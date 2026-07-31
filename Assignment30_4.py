import schedule 
import time

def Display():
    print("Namskar...")

def main():

    print("Inside Automation script")

    schedule.every().day.at("09:00").do(Display)

    while True:
        schedule.run_pending()
        time.sleep(2)
 
if __name__ == "__main__":
    main()