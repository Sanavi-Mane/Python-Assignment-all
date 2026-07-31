import schedule 
import time

def DisplayLunch():
    print("Lunch Time ...")

def DisplayWrapup():
    print("Wrap up work...")

def main():

    print("Inside automation script ")

    schedule.every().day.at("13:00").do(DisplayLunch)

    schedule.every().day.at("18:00").do(DisplayWrapup)

    while True:
        schedule.run_pending()
        time.sleep(2)

if __name__ == "__main__":
    main()