import time
import schedule 

def DisplayMessage(message):
    print(message)

def main():

    msg = input("Enter a message : ")

    schedule.every(5).seconds.do(DisplayMessage , msg)

    print("---Displaying Message---")
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
    