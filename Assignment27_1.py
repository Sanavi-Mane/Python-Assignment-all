class BookStore:

    # Class Variable
    NoOfBooks = 0

    # Constructor
    def __init__(self, Name, Author):
        self.Name = Name
        self.Author = Author

        # Increment class variable whenever an object is created
        BookStore.NoOfBooks += 1

    # Display Method
    def Display(self):
        print(self.Name, "by", self.Author + ".",
              "No of books:", BookStore.NoOfBooks)


def main():

    Obj1 = BookStore("Linux System Programming", "Robert Love")
    Obj1.Display()

    Obj2 = BookStore("C Programming", "Dennis Ritchie")
    Obj2.Display()


if __name__ == "__main__":
    main()