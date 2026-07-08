import threading

def Small(string):
    count = 0

    for ch in string:
        if ch.islower():
            count += 1

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Lowercase Characters :", count)


def Capital(string):
    count = 0

    for ch in string:
        if ch.isupper():
            count += 1

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Uppercase Characters :", count)


def Digits(string):
    count = 0

    for ch in string:
        if ch.isdigit():
            count += 1

    print("Thread ID :", threading.get_ident())
    print("Thread Name :", threading.current_thread().name)
    print("Digits :", count)


def main():
    str1 = input("Enter a string : ")

    T1 = threading.Thread(target=Small, args=(str1,), name="Small")
    T2 = threading.Thread(target=Capital, args=(str1,), name="Capital")
    T3 = threading.Thread(target=Digits, args=(str1,), name="Digits")

    T1.start()
    T2.start()
    T3.start()

    T1.join()
    T2.join()
    T3.join()

if __name__ == "__main__":
    main()