class ATM:
    def __init__(self):
        self.accounts = {}  # A dictionary to store account information {account_number: balance}
        self.current_user = None
        self.pin = ""

    def create_account(self, account_number, initial_balance, pin):
        
        # Check if the account number already exists
        if account_number in self.accounts:
            print("Account already exists.")
        else:
            # Create a new account with the given account number and initial balance
            self.accounts[account_number] = initial_balance
            print("Account created successfully.")
            self.pin = pin

    def login(self, account_number, pin):
        
        # Check if the account number exists in the accounts dictionary
        if account_number in self.accounts and pin == self.pin:
            self.current_user = account_number
            print(f"Logged in as account {account_number}.")
        else:
            print("Account not found. Please create an account.")

    def check_balance(self):
        
        if self.current_user:
            balance = self.accounts[self.current_user]
            print(f"Your balance is ${balance:.2f}")
        else:
            print("Please log in first.")

    def deposit(self, amount):
        """
        Deposit funds into the currently logged-in account.

        Args:
            amount (float): The amount to deposit.

        Returns:
            None
        """
        if self.current_user:
            if amount > 0:
                self.accounts[self.current_user] += amount
                print(f"Deposited ${amount:.2f} successfully.")
                self.check_balance()
            else:
                print("Invalid amount for deposit.")
        else:
            print("Please log in first.")

    def withdraw(self, amount):
    
        if self.current_user:
            if amount > 0:
                balance = self.accounts[self.current_user]
                if amount <= balance:
                    self.accounts[self.current_user] -= amount
                    print(f"Withdrew ${amount:.2f} successfully.")
                    self.check_balance()
                else:
                    print("Insufficient funds.")
            else:
                print("Invalid amount for withdrawal.")
        else:
            print("Please log in first.")

    def logout(self):
        
        self.current_user = None
        print("Logged out.")

    def exit(self):
        """
        Exit the ATM application.

        Returns:
            None
        """
        print("Thank you for using the ATM. Goodbye!")

def main():
    # Initialize the ATM object
    atm = ATM()

    while True:
        # Display the ATM menu
        print("\nATM Menu:")
        print("1. Create Account")
        print("2. Login")
        print("3. Check Balance")
        print("4. Deposit")
        print("5. Withdraw")
        print("6. Logout")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            # Create a new account
            account_number = input("Enter your account number: ")
            initial_balance = float(input("Enter initial balance: "))
            pin = input("Enter a PIN for your account: ")
            atm.create_account(account_number, initial_balance, pin)
            
        elif choice == "2":
            # Log in to an account
            account_number = input("Enter your account number: ")
            pin = input("Enter your PIN: ")
            atm.login(account_number, pin)
        elif choice == "3":
            # Check balance
            atm.check_balance()
        elif choice == "4":
            # Deposit funds
            amount = float(input("Enter the deposit amount: "))
            atm.deposit(amount)
        elif choice == "5":
            # Withdraw funds
            amount = float(input("Enter the withdrawal amount: "))
            atm.withdraw(amount)
        elif choice == "6":
            # Log out
            atm.logout()
        elif choice == "7":
            # Exit the ATM application
            atm.exit()
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
