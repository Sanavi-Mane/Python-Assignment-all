import schedule 
import time

def Display():
    print("Coding kar...")

def main():

    print("Inside Automation script")

    schedule.every(30).minutes.do(Display)

    while True:
        schedule.run_pending()
        time.sleep(30)
 
if __name__ == "__main__":
    main()