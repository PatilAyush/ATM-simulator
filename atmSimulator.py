#ATM simulator
amount = 0
balance = 0

while True:
  print("Welcome to the ATM\nWhat would you like to do today?\n  - Deposit\n  - Withdraw\n  - Balance\n  - Exit\n ")
  choice = input("")
  if choice.lower() == 'deposit':
    amount = float(input("Enter the amount of money you are going to be depositing: \n"))
    balance = balance + amount
    print("\nDone!\n")
  elif choice.lower() == 'withdraw':
    amount = float(input("Enter the amount of money you are going to be withdrawing: \n"))
    balance = balance - amount
    print("\nDone\n")
  elif choice.lower() == 'balance':
    print(balance,"\n")
  elif choice.lower() == 'exit':
    print("Thanks\n")
    break
