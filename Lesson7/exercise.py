def deposit(balance, amount):
    if amount <= 0:
        return balance

    return balance + amount


def withdraw(balance, amount):
    if amount <= 0 or amount > balance:
        return balance

    return balance - amount


# Main Program
balance = 2000

while True:
    print("\n===== ATM SYSTEM =====")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        print("Your Balance: $", balance)

    elif choice == "2":
        amount = float(input("Enter deposit amount: $"))

        balance = deposit(balance, amount)

        print("Deposit Successful!")
        print("New Balance: $", balance)

    elif choice == "3":
        amount = float(input("Enter withdraw amount: $"))

        if amount > balance:
            print("Insufficient Balance!")

        elif amount <= 0:
            print("Invalid Amount!")

        else:
            balance = withdraw(balance, amount)
            print("Withdraw Successful!")
            print("Remaining Balance: $", balance)

    elif choice == "4":
        print("Thank you for using our ATM!")
        break

    else:
        print("Invalid Option! Please try again.")

# Homework 6 
# create function with option using While 
# 1 deposit
# 2 withdraw