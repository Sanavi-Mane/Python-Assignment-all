import threading

counter = 0

lock = threading.Lock()


def Increment():
    global counter

    for i in range(1000):
        lock.acquire()
        counter += 1
        lock.release()


def main():
    T1 = threading.Thread(target=Increment)
    T2 = threading.Thread(target=Increment)
    T3 = threading.Thread(target=Increment)

    T1.start()
    T2.start()
    T3.start()

    T1.join()
    T2.join()
    T3.join()

    print("Final Counter : ", counter)


if __name__ == "__main__":
    main()