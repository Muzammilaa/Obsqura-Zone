# --- Parent Class ---
class Bank:

  def __init__(
      self, customer_name, customer_ID, account_no, IFSC_code, min_balance
  ):
    self.customer_name = customer_name
    self.customer_ID = customer_ID
    self.account_no = account_no
    self.IFSC_code = IFSC_code
    self.min_balance = min_balance
    self.balance = min_balance  # Starting balance is set to minimum balance

  def display(self):
    print("Customer Name:", self.customer_name)
    print("Customer ID:", self.customer_ID)
    print("Account Number:", self.account_no)
    print("IFSC Code:", self.IFSC_code)
    print("Minimum Balance:", self.min_balance)
    print("Current Balance:", self.balance)


# --- Child Class (Inherits from Bank) ---
class BankAccount(Bank):

  def __init__(
      self, customer_name, customer_ID, account_no, IFSC_code, min_balance
  ):
    # Calling the parent class constructor
    super().__init__(
        customer_name, customer_ID, account_no, IFSC_code, min_balance
    )

  def deposit(self, amount):
    acc = input("Enter account number to deposit: ")
    if acc == self.account_no:
      self.balance += amount
      print(f"Deposited {amount}. New balance is {self.balance}.")
    else:
      print("Invalid account number.")

  def withdraw(self, amount):
    acc = input("Enter account number to withdraw: ")
    if acc == self.account_no:
      if self.balance - amount >= self.min_balance:
        self.balance -= amount
        print(f"Withdrew {amount}. New balance is {self.balance}.")
      else:
        print("Insufficient balance! Cannot go below minimum balance.")
    else:
      print("Invalid account number.")


# --- Main Program ---
print("Banking Application")

# Creating objects of the child class
muzammil = BankAccount("Muzammil", "C001", "1234567890", "IFSC001", 1000)
advait = BankAccount("Advait", "C002", "0987654321", "IFSC002", 500)

# Display details (Inherited from Bank class)
print("\n--- Account Details ---")
muzammil.display()

# Deposit Money
print("\n--- Deposit ---")
muzammil.deposit(500)

# Withdraw Money
print("\n--- Withdraw ---")
muzammil.withdraw(300)