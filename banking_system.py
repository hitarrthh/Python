class BankAccount:
    def __init__(self):
        self.customer_name = ""
        self.account_number = ""
        self.balance = 0.0
        self.rate_of_interest = 0.0
        self.contact_number = ""
        self.address = ""

    def createAccount(self):
        self.customer_name = input("Enter customer name: ")
        self.account_number = input("Enter account number: ")
        self.balance = float(input("Enter initial balance: "))
        self.rate_of_interest = float(input("Enter rate of interest: "))
        self.contact_number = input("Enter contact number: ")
        self.address = input("Enter address: ")
        print("Account created successfully.")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Deposited:", amount)
            self.displayBalance()
        else:
            print("Invalid deposit amount")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Withdrawn:", amount)
            self.displayBalance()
        else:
            print("Invalid withdrawal amount or insufficient balance")

    def computeInterest(self):
        interest = (self.balance * self.rate_of_interest) / 100
        print("Interest Earned:", interest)
        self.balance += interest

    def displayBalance(self):
        print("Account Balance:", self.balance)

if __name__ == "__main__":
    accounts = []
    
    while True:
        print("\nOptions:")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Compute Interest")
        print("5. Display Balance")
        print("6. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            account = BankAccount()
            account.createAccount()
            accounts.append(account)
        elif choice == 2:
            account_number = input("Enter account number: ")
            amount = float(input("Enter the deposit amount: "))
            for account in accounts:
                if account.account_number == account_number:
                    account.deposit(amount)
                    break
            else:
                print("Account not found.")
        elif choice == 3:
            account_number = input("Enter account number: ")
            amount = float(input("Enter the withdrawal amount: "))
            for account in accounts:
                if account.account_number == account_number:
                    account.withdraw(amount)
                    break
            else:
                print("Account not found.")
        elif choice == 4:
            account_number = input("Enter account number: ")
            for account in accounts:
                if account.account_number == account_number:
                    account.computeInterest()
                    break
            else:
                print("Account not found.")
        elif choice == 5:
            account_number = input("Enter account number: ")
            for account in accounts:
                if account.account_number == account_number:
                    account.displayBalance()
                    break   
            else:
                print("Account not found.")
        elif choice == 6:
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")
