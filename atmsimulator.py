class ATM:
    def __init__(self, balance=0):
        self.balance = balance

    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"${amount} deposited successfully.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"${amount} withdrawn successfully.")

def main():
    atm = ATM()  # Initialize ATM with default balance of 0
    while True:
        print("\nATM Operations:")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        
        choice = input("Choose an operation (1-4): ")
        
        if choice == '1':
            atm.check_balance()
        elif choice == '2':
            amount = float(input("Enter the amount to deposit: "))
            atm.deposit(amount)
        elif choice == '3':
            amount = float(input("Enter the amount to withdraw: "))
            atm.withdraw(amount)
        elif choice == '4':
            print("Exiting ATM. Have a nice day!")
            break
        else:
            print("Invalid choice. Please enter 1-4.")

if __name__ == "__main__":
    main()
