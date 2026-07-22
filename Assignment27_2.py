class BankAccount:

    # Class Variable
    ROI = 10.5

    # Constructor
    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    # Display account details
    def Display(self):
        print("\nAccount Holder :", self.Name)
        print("Current Balance :", self.Amount)

    # Deposit amount
    def Deposit(self):
        money = float(input("Enter amount to deposit : "))
        self.Amount = self.Amount + money
        print("Amount deposited successfully.")

    # Withdraw amount
    def Withdraw(self):
        money = float(input("Enter amount to withdraw : "))

        if money <= self.Amount:
            self.Amount = self.Amount - money
            print("Withdrawal successful.")
        else:
            print("Insufficient Balance!")

    # Calculate Interest
    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest


def main():

    size = int(input("Enter number of accounts : "))

    Accounts = []

    for i in range(size):
        print("\nEnter details for Account", i + 1)

        name = input("Enter Account Holder Name : ")
        amount = float(input("Enter Initial Balance : "))

        obj = BankAccount(name, amount)
        Accounts.append(obj)

    print("\n========== Account Details ==========")

    for obj in Accounts:

        obj.Display()

        obj.Deposit()
        obj.Display()

        obj.Withdraw()
        obj.Display()

        print("Interest :", obj.CalculateInterest())


if __name__ == "__main__":
    main()