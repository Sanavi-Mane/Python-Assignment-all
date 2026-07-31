import time
import schedule 

def Display(message):
    print(message)

def main():

    msg = input("Enter message :")

    interval = int(input("Enter interval in seconds : "))
    
    schedule.every(interval).seconds.do(Display, msg)

    while True :
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()